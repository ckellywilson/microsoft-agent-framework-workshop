# Tutorial 20: Multi-User MCP with Azure API Management OAuth

## Design Document

**Status**: Planning Phase  
**Date**: October 2025  
**Estimated Duration**: 75 minutes  
**Prerequisites**: Tutorial 19 (API Management Integration)

---

## 1. Overview

### Building Upon Tutorial 19

Tutorial 19 introduced Azure API Management (APIM) as an enterprise gateway for MCP servers, covering:
- Load balancing across MCP server instances
- Rate limiting and token quotas
- Circuit breaker patterns
- Monitoring and observability

**Tutorial 20 extends this foundation** by adding user identity and authorization using APIM's native OAuth capabilities.

### Problem Statement

Enterprise AI agents must respect user identity, roles, and permissions when accessing data and systems. Instead of building custom authentication middleware in the MCP server, we leverage APIM's built-in **Credential Manager** to:

- Authenticate users via Azure AD/Entra ID
- Manage OAuth 2.0 connections and token refresh automatically
- Pass user context to MCP servers through APIM policies
- Enforce role-based access control (RBAC) on MCP tools
- Use Row-Level Security (RLS) in Azure SQL Database
- Maintain audit trails for compliance

### Architecture Advantage

By using APIM's Credential Manager, we avoid building custom OAuth plumbing:
- **No custom token validation** - APIM handles JWT validation
- **No token refresh logic** - APIM automatically refreshes access tokens
- **No token caching** - APIM caches tokens internally
- **Centralized policy management** - OAuth policies apply to all APIs/MCP servers
- **Developer portal integration** - Self-service OAuth consent flow

### Learning Objectives

By the end of this tutorial, you will:

1. Configure APIM Credential Manager for OAuth 2.0 connections
2. Set up user-delegated (attended) authentication scenarios
3. Use `get-authorization-context` policy to attach user tokens
4. Pass user identity to MCP servers via custom headers
5. Implement role-based MCP tools in FastMCP
6. Configure Azure SQL Database with Azure AD and RLS
7. Implement secure multi-tenant patterns with APIM as the authorization layer

---

## 2. Use Case: Enterprise Travel Management System

### Business Scenario

A company needs an AI-powered travel assistant where different employees have different access levels:

**User Roles:**

1. **Employee** (`employee`)
   - Search flights and hotels
   - Submit travel requests for approval
   - View own bookings
   - Cancel own pending requests

2. **Manager** (`manager`)
   - All employee capabilities
   - Approve/reject team member travel requests
   - View team bookings and budgets
   - Reallocate team travel budget

3. **Travel Administrator** (`admin`)
   - All manager capabilities
   - View all company bookings
   - Modify travel policies
   - Override approvals
   - Access system configuration

4. **Finance Analyst** (`finance`)
   - View all bookings (read-only)
   - Generate cost reports by department
   - Export financial data
   - View budget utilization

### Data Access Patterns

| Role | Own Bookings | Team Bookings | All Bookings | Financial Reports |
|------|-------------|---------------|--------------|-------------------|
| Employee | Read/Write | ❌ | ❌ | ❌ |
| Manager | Read/Write | Read/Approve | ❌ | Team Only |
| Admin | Read/Write | Read/Write | Read/Write | ✅ Full Access |
| Finance | Read-Only | Read-Only | Read-Only | ✅ Full Access |

---

## 3. Architecture Design

### High-Level Flow with APIM Credential Manager

```
┌──────────────────────────────────────────────────────────────────────┐
│ 1. User authenticates with Azure AD                                  │
│    - AI agent/app gets user JWT token with claims (oid, email, etc.) │
└────────────────────────────┬─────────────────────────────────────────┘
                             │
                             ↓
┌──────────────────────────────────────────────────────────────────────┐
│ 2. User interacts with Azure AI Foundry Agent                        │
│    - Agent configured with user-delegated APIM connection            │
└────────────────────────────┬─────────────────────────────────────────┘
                             │
                             ↓
┌──────────────────────────────────────────────────────────────────────┐
│ 3. Agent → APIM Gateway (MCP Server endpoint)                        │
│    - Authorization: Bearer <user_jwt_token>                          │
│    - APIM receives user token from agent                             │
└────────────────────────────┬─────────────────────────────────────────┘
                             │
                             ↓
┌──────────────────────────────────────────────────────────────────────┐
│ 4. APIM Credential Manager (Inbound Policy)                          │
│    ┌──────────────────────────────────────────────────────────┐     │
│    │ <get-authorization-context>                               │     │
│    │   - Validates user JWT token                              │     │
│    │   - Extracts user identity (oid, email, roles)           │     │
│    │   - Retrieves/refreshes user's OAuth connection          │     │
│    │   - Stores access token in context variable              │     │
│    │ </get-authorization-context>                              │     │
│    └──────────────────────────────────────────────────────────┘     │
│                             │                                         │
│    ┌──────────────────────────────────────────────────────────┐     │
│    │ <set-header> (Add user context headers)                  │     │
│    │   - X-User-Id: @(context.Request.Headers.GetValueOrDefault(   │
│    │                    "oid", "anonymous"))                   │     │
│    │   - X-User-Email: @(context.Request.Headers.GetValueOrDefault( │
│    │                       "email", ""))                       │     │
│    │   - Authorization: Bearer <managed_access_token>         │     │
│    │ </set-header>                                             │     │
│    └──────────────────────────────────────────────────────────┘     │
└────────────────────────────┬─────────────────────────────────────────┘
                             │
                             ↓
┌──────────────────────────────────────────────────────────────────────┐
│ 5. FastMCP Server (Azure Container Apps)                             │
│    ┌──────────────────────────────────────────────────────────┐     │
│    │ MCP Server receives requests with user context:          │     │
│    │   - X-User-Id header → identifies user                   │     │
│    │   - X-User-Email header → for display/logging            │     │
│    │   - Authorization header → APIM-managed token            │     │
│    │                                                           │     │
│    │ MCP Tool Implementation:                                  │     │
│    │   1. Extract user_id from X-User-Id header               │     │
│    │   2. Query Users table to get role                       │     │
│    │   3. Check tool permission matrix                        │     │
│    │   4. Execute tool with user context                      │     │
│    │   5. Database queries filtered by RLS                    │     │
│    └──────────────────────────────────────────────────────────┘     │
└────────────────────────────┬─────────────────────────────────────────┘
                             │
                             ↓
┌──────────────────────────────────────────────────────────────────────┐
│ 6. Azure SQL Database with Azure AD Authentication                   │
│    ┌──────────────────────────────────────────────────────────┐     │
│    │ Connection:                                               │     │
│    │   - Managed identity or service principal auth           │     │
│    │   - MCP server sets SESSION_CONTEXT('user_id', ...)     │     │
│    │                                                           │     │
│    │ Row-Level Security (RLS):                                │     │
│    │   - Employee: See only own bookings                      │     │
│    │   - Manager: See team bookings                           │     │
│    │   - Admin/Finance: See all bookings                      │     │
│    └──────────────────────────────────────────────────────────┘     │
└──────────────────────────────────────────────────────────────────────┘
```

### Component Details

#### A. APIM Credential Manager Configuration

**1. Credential Provider Setup**
- **Provider Type**: Azure AD (Microsoft Entra ID)
- **Grant Type**: Authorization Code (user-delegated)
- **Client ID**: MCP Server App Registration
- **Scopes**: User.Read, database access scope
- **Redirect URI**: APIM callback endpoint

**2. APIM Inbound Policy (OAuth + User Context)**

```xml
<inbound>
    <!-- Validate and get user's OAuth connection -->
    <get-authorization-context 
        provider-id="azure-ad-provider" 
        authorization-id="@(context.Request.Headers.GetValueOrDefault("oid", ""))"
        context-variable-name="auth-context" 
        identity-type="user" 
        ignore-error="false">
    </get-authorization-context>
    
    <!-- Extract user identity from JWT claims -->
    <set-variable name="user-id" 
        value="@(context.Request.Headers.GetValueOrDefault("oid", "anonymous"))" />
    <set-variable name="user-email" 
        value="@(context.Request.Headers.GetValueOrDefault("email", ""))" />
    <set-variable name="user-roles" 
        value="@(context.Request.Headers.GetValueOrDefault("roles", ""))" />
    
    <!-- Add user context headers for MCP server -->
    <set-header name="X-User-Id" exists-action="override">
        <value>@((string)context.Variables["user-id"])</value>
    </set-header>
    <set-header name="X-User-Email" exists-action="override">
        <value>@((string)context.Variables["user-email"])</value>
    </set-header>
    <set-header name="X-User-Roles" exists-action="override">
        <value>@((string)context.Variables["user-roles"])</value>
    </set-header>
    
    <!-- Replace Authorization header with managed OAuth token -->
    <set-header name="Authorization" exists-action="override">
        <value>@("Bearer " + ((JObject)context.Variables["auth-context"])["AccessToken"])</value>
    </set-header>
    
    <!-- Apply rate limiting per user -->
    <rate-limit-by-key calls="100" renewal-period="60" 
        counter-key="@((string)context.Variables["user-id"])" />
    
    <!-- Token metrics for monitoring -->
    <llm-emit-token-metric namespace="mcp-travel">
        <dimension name="User" value="@((string)context.Variables["user-email"])" />
        <dimension name="Tool" value="@(context.Request.Url.Path)" />
    </llm-emit-token-metric>
</inbound>
```

#### B. Simplified FastMCP Server (No Auth Middleware Needed!)

The MCP server becomes much simpler since APIM handles all OAuth complexity:

**1. Extract User Context from Headers**

```python
from fastapi import Request, HTTPException

def get_user_context(request: Request) -> dict:
    """Extract user context from APIM-injected headers"""
    user_id = request.headers.get("X-User-Id")
    user_email = request.headers.get("X-User-Email")
    user_roles = request.headers.get("X-User-Roles", "").split(",")
    
    if not user_id or user_id == "anonymous":
        raise HTTPException(status_code=401, detail="Unauthorized: Missing user context")
    
    return {
        "user_id": user_id,
        "email": user_email,
        "roles": user_roles
    }
```

**2. Role-Based Tool Decorator**

```python
from functools import wraps

def require_role(*allowed_roles):
    """Decorator to enforce role-based access on MCP tools"""
    def decorator(func):
        @wraps(func)
        async def wrapper(request: Request, *args, **kwargs):
            user_ctx = get_user_context(request)
            
            # Check if user has required role
            if not any(role in user_ctx["roles"] for role in allowed_roles):
                raise HTTPException(
                    status_code=403, 
                    detail=f"Forbidden: Requires one of {allowed_roles}"
                )
            
            # Add user context to function kwargs
            return await func(request, user_ctx=user_ctx, *args, **kwargs)
        return wrapper
    return decorator
```

**3. MCP Tool with RBAC**

```python
@mcp.tool()
@require_role("manager", "admin")
async def approve_travel_request(request: Request, booking_id: int) -> Dict[str, Any]:
    """Approve a team member's travel request (managers and admins only)"""
    user_ctx = get_user_context(request)
    
    # Database query with user context
    async with get_db_connection(user_ctx) as conn:
        # Set SESSION_CONTEXT for RLS
        await conn.execute(f"EXEC sp_set_session_context 'user_id', '{user_ctx['user_id']}'")
        
        # Update booking (RLS ensures manager can only approve their team's requests)
        result = await conn.execute(
            "UPDATE TravelBookings SET status='approved', approved_by=@user_id WHERE booking_id=@id",
            {"user_id": user_ctx["user_id"], "id": booking_id}
        )
        
        if result.rowcount == 0:
            return {"error": "Booking not found or access denied"}
        
        return {"success": True, "booking_id": booking_id, "approved_by": user_ctx["email"]}
```

#### B. Database Schema

**Users Table:**
```sql
CREATE TABLE Users (
    user_id NVARCHAR(100) PRIMARY KEY,  -- Azure AD object_id
    email NVARCHAR(255) NOT NULL UNIQUE,
    display_name NVARCHAR(255),
    role NVARCHAR(50) NOT NULL CHECK (role IN ('employee', 'manager', 'admin', 'finance')),
    department NVARCHAR(100),
    manager_id NVARCHAR(100) FOREIGN KEY REFERENCES Users(user_id),
    created_at DATETIME2 DEFAULT GETDATE(),
    updated_at DATETIME2 DEFAULT GETDATE()
);
```

**TravelBookings Table:**
```sql
CREATE TABLE TravelBookings (
    booking_id INT PRIMARY KEY IDENTITY,
    user_id NVARCHAR(100) NOT NULL FOREIGN KEY REFERENCES Users(user_id),
    manager_id NVARCHAR(100) FOREIGN KEY REFERENCES Users(user_id),
    
    -- Booking details
    origin NVARCHAR(100),
    destination NVARCHAR(100),
    departure_date DATE,
    return_date DATE,
    
    -- Financial
    estimated_cost DECIMAL(10,2),
    actual_cost DECIMAL(10,2),
    currency NVARCHAR(3) DEFAULT 'USD',
    
    -- Workflow
    status NVARCHAR(50) CHECK (status IN ('pending', 'approved', 'rejected', 'completed', 'cancelled')),
    submitted_at DATETIME2 DEFAULT GETDATE(),
    approved_at DATETIME2,
    approved_by NVARCHAR(100) FOREIGN KEY REFERENCES Users(user_id),
    
    -- Audit
    created_at DATETIME2 DEFAULT GETDATE(),
    updated_at DATETIME2 DEFAULT GETDATE()
);
```

**Row-Level Security:**
```sql
-- Security function
CREATE FUNCTION dbo.fn_TravelBookingSecurity(@user_id NVARCHAR(100), @user_role NVARCHAR(50))
RETURNS TABLE
WITH SCHEMABINDING
AS
RETURN
    SELECT 1 AS result
    WHERE 
        @user_role IN ('admin', 'finance')  -- Admin/Finance see all
        OR user_id = @user_id                -- Users see own bookings
        OR manager_id = @user_id;            -- Managers see team bookings

-- Security policy
CREATE SECURITY POLICY TravelBookingSecurityPolicy
    ADD FILTER PREDICATE dbo.fn_TravelBookingSecurity(user_id, SESSION_CONTEXT(N'user_role'))
    ON dbo.TravelBookings
WITH (STATE = ON);
```

#### C. MCP Tools with RBAC

**Tool Permission Matrix:**

| Tool | Employee | Manager | Admin | Finance |
|------|----------|---------|-------|---------|
| `search_flights` | ✅ | ✅ | ✅ | ✅ |
| `search_hotels` | ✅ | ✅ | ✅ | ✅ |
| `submit_travel_request` | ✅ | ✅ | ✅ | ❌ |
| `view_my_bookings` | ✅ | ✅ | ✅ | ❌ |
| `cancel_my_booking` | ✅ | ✅ | ✅ | ❌ |
| `view_team_bookings` | ❌ | ✅ | ✅ | ✅ |
| `approve_travel_request` | ❌ | ✅ | ✅ | ❌ |
| `view_all_bookings` | ❌ | ❌ | ✅ | ✅ |
| `generate_cost_report` | ❌ | ✅ (team) | ✅ | ✅ |
| `modify_travel_policy` | ❌ | ❌ | ✅ | ❌ |

---

## 4. OAuth On-Behalf-Of Flow Details

### Token Exchange Process

```
┌──────────────────────────────────────────────────────────────────┐
│ Step 1: User Authentication                                       │
│ User → Azure AD: Login with credentials                          │
│ Azure AD → User: JWT access token (audience: AI Foundry)        │
└──────────────────────────────────────────────────────────────────┘
                             │
                             ↓
┌──────────────────────────────────────────────────────────────────┐
│ Step 2: Agent Request                                             │
│ User → Agent: "Show my travel bookings"                          │
│ Agent attaches user token to HostedMCPTool request               │
│ Request Header: Authorization: Bearer <user_jwt_token>           │
└──────────────────────────────────────────────────────────────────┘
                             │
                             ↓
┌──────────────────────────────────────────────────────────────────┐
│ Step 3: MCP Server Token Exchange (OBO)                          │
│                                                                   │
│ POST https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token│
│ Body:                                                             │
│   grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer        │
│   client_id={mcp_server_client_id}                              │
│   client_secret={mcp_server_secret}                             │
│   assertion={user_jwt_token}                                     │
│   requested_token_use=on_behalf_of                               │
│   scope=https://database.windows.net/.default                    │
│                                                                   │
│ Response:                                                         │
│   {                                                               │
│     "access_token": "<obo_token_for_sql>",                       │
│     "token_type": "Bearer",                                       │
│     "expires_in": 3600                                            │
│   }                                                               │
└──────────────────────────────────────────────────────────────────┘
                             │
                             ↓
┌──────────────────────────────────────────────────────────────────┐
│ Step 4: Database Access with OBO Token                           │
│ MCP Server → Azure SQL: Connect with OBO token                   │
│ Connection String:                                                │
│   Server=tcp:{server}.database.windows.net,1433;                │
│   Database={db};                                                  │
│   Authentication=Active Directory Access Token;                  │
│   AccessToken={obo_token};                                       │
│                                                                   │
│ SET CONTEXT_INFO:                                                 │
│   EXEC sp_set_session_context 'user_id', @user_id;              │
│   EXEC sp_set_session_context 'user_role', @user_role;          │
│                                                                   │
│ Query executes with RLS automatically enforced                   │
└──────────────────────────────────────────────────────────────────┘
```

### Required Azure AD App Registrations

**1. AI Agent Application**
- **App Name**: `travel-assistant-agent`
- **Redirect URIs**: Azure AI Foundry endpoints
- **API Permissions**: 
  - User.Read (Microsoft Graph)
  - Access to MCP Server API
- **Token Claims**: email, roles, oid

**2. MCP Server Application**
- **App Name**: `travel-mcp-server`
- **Expose an API**: `api://travel-mcp-server`
- **API Permissions**:
  - SQL Database (https://database.windows.net/.default)
  - Microsoft Graph (optional for profile lookups)
- **Client Secret**: For OBO token exchange
- **Pre-authorized applications**: AI Agent app

**3. Database Access**
- Azure SQL configured with Azure AD authentication
- MCP Server service principal added as database user
- Users added as database users (automatic via Azure AD)

---

## 5. Implementation Plan

### Part 1: APIM Credential Manager Setup (20 min)
- Configure OAuth credential provider in APIM
- Set up user-delegated authorization
- Create test connection and consent flow
- Configure access policies for user identities

### Part 2: APIM Policy Configuration (15 min)
- Implement inbound policy with `get-authorization-context`
- Add custom headers for user context propagation
- Configure rate limiting per user
- Add token metrics for monitoring

### Part 3: Database Setup with RLS (20 min)
- Create Azure SQL Database with Azure AD auth
- Create database schema (Users, TravelBookings)
- Implement Row-Level Security policies
- Seed sample data (users with different roles)

### Part 4: FastMCP Server with RBAC (15 min)
- Add user context extraction from headers
- Implement role-based tool decorators
- Build role-aware MCP tools
- Connect to database with SESSION_CONTEXT

### Part 5: Testing Multi-User Scenarios (15 min)
- Test employee access (view own bookings)
- Test manager access (approve team requests)
- Test admin access (system-wide view)
- Verify RLS enforcement
- Check audit logs in APIM Analytics

---

## 6. Security Considerations

### Authentication Security
- JWT signature validation using Azure AD public keys
- Token expiration checks
- Replay attack prevention
- Secure token storage (in-memory cache only)

### Authorization Security
- Principle of least privilege
- Role validation on every request
- Database-level security (RLS) as defense-in-depth
- Audit logging for sensitive operations

### Database Security
- Azure AD authentication (no SQL passwords)
- Row-Level Security enforced at database layer
- Encrypted connections (TLS)
- Column-level encryption for sensitive data

### Network Security
- Container Apps with VNET integration
- Private endpoint for SQL Database
- API Management for additional security layer
- Rate limiting and throttling

---

## 7. Testing Scenarios

### Scenario 1: Employee Access
```
User: alice@contoso.com (role: employee)
Action: "Show my travel bookings"
Expected: See only Alice's bookings
Expected: Cannot see Bob's bookings
Expected: Cannot approve requests
```

### Scenario 2: Manager Access
```
User: bob@contoso.com (role: manager, manages Alice)
Action: "Show team travel requests pending my approval"
Expected: See Alice's pending requests
Expected: Can approve/reject Alice's requests
Expected: Cannot see other team's bookings
```

### Scenario 3: Finance Analyst Access
```
User: charlie@contoso.com (role: finance)
Action: "Generate cost report for Q4 2024"
Expected: See all bookings (read-only)
Expected: Generate financial reports
Expected: Cannot modify bookings
Expected: Cannot approve requests
```

### Scenario 4: Unauthorized Access Attempt
```
User: alice@contoso.com (role: employee)
Action: "Approve Bob's travel request"
Expected: 403 Forbidden error
Expected: Error message: "Insufficient permissions for tool 'approve_travel_request'"
```

---

## 8. Tutorial Structure

### Tutorial 20 Outline (Building on Tutorial 19)

**Part 1: APIM Credential Manager Introduction**
- Overview of APIM OAuth capabilities
- User-delegated vs unattended scenarios
- Credential providers and connections
- Benefits over custom auth middleware

**Part 2: Configuring OAuth in APIM**
- Set up Azure AD credential provider
- Configure user-delegated access policies
- Implement consent flow
- Test OAuth connection

**Part 3: APIM Policy for User Context**
- Write `get-authorization-context` policy
- Extract user claims and add custom headers
- Implement per-user rate limiting
- Add token usage metrics

**Part 4: Database Design with RLS**
- Create Azure SQL schema with user roles
- Implement Row-Level Security policies
- Configure SESSION_CONTEXT for filtering
- Test RLS with different users

**Part 5: FastMCP Server with RBAC**
- Extract user context from APIM headers
- Implement role-based decorators
- Build role-aware MCP tools
- Connect to database with user context

**Part 6: End-to-End Testing**
- Test employee scenario (own bookings only)
- Test manager scenario (approve team requests)
- Test admin scenario (system-wide access)
- Verify audit logs in APIM Analytics

**Part 7: Production Best Practices**
- Token refresh and caching (handled by APIM)
- Monitoring user access patterns
- Compliance and audit requirements
- Scaling considerations

---

## 9. Key Takeaways

After completing Tutorial 20, learners will understand:

1. **APIM as OAuth Gateway**: Leverage APIM's Credential Manager instead of building custom auth middleware
2. **User-Delegated Access**: Configure user-specific OAuth connections that maintain individual identity
3. **Policy-Based Security**: Use APIM policies to inject user context into backend requests
4. **Database-Level Security**: Implement Row-Level Security (RLS) for defense-in-depth
5. **Enterprise RBAC**: Build role-based MCP tools without complex authentication code
6. **Compliance & Audit**: Use APIM Analytics for comprehensive access logging

### Why This Approach Matters

**Compared to Custom Auth Middleware (Tutorial 20 Alternative)**:
- ❌ Custom: Build JWT validation, token refresh, caching, error handling
- ✅ APIM: All OAuth complexity handled by platform

**Production Benefits**:
- Zero-code OAuth flows and token management
- Centralized policy enforcement across all APIs/MCP servers
- Built-in monitoring and analytics
- Developer self-service through APIM portal

This tutorial demonstrates how **Azure API Management** transforms from a simple gateway (Tutorial 19) into a complete **identity-aware API platform** for enterprise AI agents.

---

## 10. Next Steps

After Tutorial 20, learners can explore:
- Tutorial 21: Integrating with Microsoft Graph (access user's calendar, email)
- Tutorial 22: Multi-tenant SaaS patterns (org-level isolation)
- Tutorial 23: Advanced compliance (GDPR, data residency)
- Tutorial 24: Performance at scale (caching, connection pooling)

---

## Summary

Tutorial 20 extends Tutorial 19 by adding **user identity and authorization** to MCP servers using **Azure API Management's native OAuth capabilities**. Instead of building custom authentication middleware in the MCP server, we leverage APIM's **Credential Manager** to handle all OAuth complexity (token validation, refresh, caching). 

The MCP server becomes simpler - it just reads user context from APIM-injected headers (`X-User-Id`, `X-User-Email`, `X-User-Roles`) and enforces role-based access control. Database security is handled through **Row-Level Security (RLS)** in Azure SQL, providing defense-in-depth.

This architecture demonstrates how APIM transforms from a simple gateway into a complete **identity-aware AI agent platform** - perfect for enterprise scenarios requiring multi-user access, role-based permissions, and compliance auditing.

---

**Document Status**: Ready for Review  
**Next Action**: Review design, then proceed with implementation
