# Testing Logic Apps MCP Server in VS Code

## Step 1: Add MCP Server

1. Open VS Code
2. Open Command Palette: `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows)
3. Type and select: **MCP: Add Server**
4. Choose: **HTTP (HTTP or Server-Sent Events)**
5. Enter your MCP server URL (copied from API Center Portal)
6. Enter Server ID: `travel-email-assistant` (or your server name)
7. Choose storage location:
   - **Global** - Available across all workspaces
   - **Workspace** - Only for current workspace

## Step 2: Authenticate

1. VS Code creates/opens an `mcp.json` file
2. Click **Start** or **Restart** link in the file
3. When prompted, click **Allow**
4. Select your Azure account
5. Sign in and grant consent
6. Status should show **Running**

## Step 3: Test with GitHub Copilot

1. Open Copilot Chat: `Cmd+Option+I` (Mac) or `Ctrl+Alt+I` (Windows)
2. Click the mode dropdown and select **Agent**
3. Click **Configure Tools**
4. Enable your MCP server tools
5. Try these test prompts:

### Test Prompts

**Email Test:**
```
Send a travel confirmation email to john@example.com for a trip to 
London from November 15-18. Include flight details and hotel info.
```

**Calendar Test:**
```
Check my calendar availability for next Monday and schedule a 
pre-trip planning meeting at 2pm.
```

**Multi-step Test:**
```
I need to plan a team trip to Paris. Create a calendar event for 
March 15th and send an email to the team with the details.
```

## Sample mcp.json Configuration

```json
{
  "mcpServers": {
    "travel-email-assistant": {
      "type": "http",
      "url": "YOUR_MCP_ENDPOINT_URL_HERE",
      "headers": {}
    }
  }
}
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Authentication fails | Check Azure permissions and role assignments |
| Tools not appearing | Verify Logic App is running and MCP server is registered |
| Tool execution fails | Check connector authentication in Logic App |
| Timeout errors | Increase timeout in Logic App configuration |
| "Server not responding" | Click Restart in mcp.json file |
