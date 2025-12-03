# Microsoft Agent Framework - Progressive Tutorial Series

Comprehensive learning path for building AI agents using Microsoft's Azure AI Agent Framework.

## 🎯 Learning Path: Personal Travel Assistant

This tutorial series teaches you Microsoft Agent Framework by building a **Personal Travel Assistant** that grows in capability with each lesson. You'll learn all major features through hands-on, practical examples.

## 📚 Tutorial Structure

Each notebook builds on the previous one, introducing new concepts while enhancing our Travel Assistant.


### Tutorial Series

#### **Level 1: Foundations** (Notebooks 01-03)

| # | Tutorial | Topics Covered | Duration |
|---|----------|----------------|----------|
| 01 | [Basic Agent](./01_basic_agent.ipynb) | Agent creation, responses, OpenAI setup | 15 min |
| 01b | [Azure AI Foundry](./01b_azure_ai_foundry.ipynb) | Azure deployment, model endpoints | 20 min |
| 02 | [Agent with Tools](./02_agent_with_tools.ipynb) | Function calling, tool integration | 25 min |
| 03 | [Multi-turn Conversations](./03_multi_turn_conversations.ipynb) | Context management, conversation flow | 30 min |

#### **Level 2: Intermediate** (Notebooks 04-06)

| # | Tutorial | Topics Covered | Duration |
|---|----------|----------------|----------|
| 04 | [Context & Memory](./04_context_and_memory.ipynb) | Memory systems, retrieval patterns | 35 min |
| 05 | [Middleware & Filters](./05_middleware_and_filters.ipynb) | Request/response pipelines, telemetry | 30 min |
| 06 | [Multi-Agent Workflows](./06_multi_agent_workflows.ipynb) | Agent collaboration, orchestration | 40 min |

#### **Level 3: Advanced** (Notebooks 07-09)

| # | Tutorial | Topics Covered | Duration |
|---|----------|----------------|----------|
| 07 | [Advanced Workflows](./07_advanced_workflows.ipynb) | Complex patterns, state management | 45 min |
| 08 | [Human-in-the-Loop](./08_human_in_the_loop.ipynb) | Approval workflows, feedback loops | 30 min |
| 09 | [Error Handling](./09_error_handling_recovery.ipynb) | Retry logic, fault tolerance | 25 min |

#### **Level 4: Production & Integration** (Notebooks 10-14)

| # | Tutorial | Topics Covered | Duration |
|---|----------|----------------|----------|
| 10 | [Azure File Search](./10_azure_file_search_demo.ipynb) | Vector search, RAG patterns | 35 min |
| 12 | [Azure Monitor Alerts](./12_azure_monitor_alerts.ipynb) | Monitoring, alerting, observability | 30 min |
| 14 | [Unified WebApp Monitoring](./14_unified_webapp_agent_monitoring.ipynb) | Production monitoring, dashboards | 35 min |

#### **Level 5: Enterprise MCP Server Pattern** (Notebooks 15-20)

| # | Tutorial | Topics Covered | Duration |
|---|----------|----------------|----------|
| 15 | [FastMCP Server Basics](./15_fastmcp_server_basics.ipynb) | Building MCP servers, local tools, Azure AI observability | 45 min |
| 16 | [Deploy FastMCP to Azure](./16_deploy_fastmcp_to_aca.ipynb) | Docker, Azure Container Apps, hosted MCP tools | 60 min |
| 17 | [Logic Apps MCP Server](./17_logic_app_mcp_server.ipynb) | No-code MCP tools, Azure API Center | 50 min |
| 18 | [API Management Integration](./18_apim_mcp_integration.ipynb) | Enterprise gateway, security policies | 45 min |
| 19 | [MCP Authentication & Security](./19_orchestrating_agent_with_mcp.ipynb) | Entra ID auth, APIM security, observability | 60 min |
| 20 | [Multi-User MCP with APIM OAuth](./20_DESIGN.md) | APIM Credential Manager, user-delegated auth, RLS, RBAC | 75 min |

**Total Learning Time**: ~10 hours

> **Note**: Tutorials 16-20 are work in progress



### 🌟 What's in the Enterprise MCP Pattern?

The **Enterprise MCP Server Pattern** (Tutorials 15-19) teaches you how to build production-ready tool servers using the **Model Context Protocol (MCP)**:

- **Tutorial 15**: Build MCP servers in Python with FastMCP framework
- **Tutorial 16**: Containerize and deploy to Azure Container Apps with auto-scaling
- **Tutorial 17**: Create no-code MCP tools using Azure Logic Apps (1,400+ connectors)
- **Tutorial 18**: Secure and monitor tools with Azure API Management
- **Tutorial 19**: Build an orchestrating agent that coordinates multiple MCP servers

**Why MCP?** The Model Context Protocol is an open standard that lets AI agents securely connect to any tool or data source. By the end of this series, you'll have:

- ✅ Custom Python MCP tools (flights, hotels, currency conversion)
- ✅ Enterprise integration MCP tools (Office 365, SharePoint, Teams)
- ✅ Production-grade API gateway with security and monitoring
- ✅ An orchestrating AI agent that intelligently uses multiple tool servers

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- Azure subscription with Azure OpenAI service
- Azure OpenAI deployment (gpt-4, gpt-4o, or gpt-35-turbo)

### Setup

#### Option 1: Using Dev Container (Recommended)

The easiest way to get started is using the pre-configured dev container, which includes all tools and dependencies.

**Requirements:**
- [Docker Desktop](https://www.docker.com/products/docker-desktop) (Windows/Mac/Linux)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

**Installing Docker Desktop:**

- **Windows**: 
  1. Download [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop)
  2. Run the installer and follow the setup wizard
  3. Docker Desktop will use WSL 2 by default (recommended)
  4. If WSL 2 is not installed, Docker will prompt you to install it:
     - Open PowerShell as Administrator and run:
       ```powershell
       wsl --install
       ```
     - Restart your computer when prompted
     - Set WSL 2 as default: `wsl --set-default-version 2`
  5. Start Docker Desktop from the Start menu

- **Mac**:
  1. Download [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop) (choose Apple Silicon or Intel chip)
  2. Open the `.dmg` file and drag Docker to Applications
  3. Launch Docker from Applications folder

- **Linux**:
  1. Follow the [official installation guide](https://docs.docker.com/desktop/install/linux-install/) for your distribution
  2. Or install Docker Engine: [Ubuntu](https://docs.docker.com/engine/install/ubuntu/), [Debian](https://docs.docker.com/engine/install/debian/), [Fedora](https://docs.docker.com/engine/install/fedora/)

**Steps:**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/gokoner/microsoft-agent-framework-workshop.git
   cd microsoft-agent-framework-workshop
   ```

2. **Open in VS Code:**

   ```bash
   code .
   ```

3. **Reopen in Container:**
   - **Windows**: Press `F1` → Type "Dev Containers: Reopen in Container" → Press Enter
   - **Mac/Linux**: Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Linux) → Type "Dev Containers: Reopen in Container" → Press Enter
   
   Alternatively, when VS Code detects the dev container configuration, click **"Reopen in Container"** in the notification popup.

4. **Wait for container to build** (first time only, ~2-5 minutes)

5. **The environment is ready!** All dependencies are pre-installed including:
   - Python 3.12 with pip packages
   - Node.js and npm
   - Azure CLI
   - GitHub CLI
   - Jupyter notebooks support

#### Option 2: Using venv (Standard Python)

1. **Clone the repository:**

   ```bash
   git clone https://github.com/gokoner/microsoft-agent-framework-workshop.git
   cd microsoft-agent-framework-workshop
   ```

2. **Create and activate virtual environment:**

   **Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   **Mac/Linux:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

#### Option 3: Using uv (Faster Package Manager)

1. **Install uv** (if not already installed):

   **Windows (PowerShell):**
   ```powershell
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

   **Mac/Linux:**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone and setup:**

   ```bash
   git clone https://github.com/gokoner/microsoft-agent-framework-workshop.git
   cd microsoft-agent-framework-workshop
   
   # Create virtual environment and install dependencies
   uv venv
   ```

3. **Activate virtual environment:**

   **Windows:**
   ```bash
   .venv\Scripts\activate
   ```

   **Mac/Linux:**
   ```bash
   source .venv/bin/activate
   ```

4. **Install dependencies:**

   ```bash
   uv pip install -r requirements.txt
   ```

### Configure Azure OpenAI

Create a `.env` file with your Azure OpenAI credentials:

```bash
# Azure OpenAI Configuration
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-api-key-here
MODEL_DEPLOYMENT_NAME=gpt-4  # or gpt-4o, gpt-35-turbo

# Optional: Azure AI Foundry (for Tutorials 01b, 10-14)
AZURE_AI_PROJECT_CONNECTION_STRING=your-project-connection-string
```

**How to get these values:**

- **Endpoint & API Key**: [Azure Portal](https://portal.azure.com) → Azure OpenAI → Keys and Endpoint
- **Deployment Name**: Azure OpenAI Studio → Deployments → Your deployment name

### Start Learning

Open the first tutorial:

```bash
jupyter notebook 01_basic_agent.ipynb
```

## 📖 What You'll Build

By the end, you'll have a production-ready Travel Assistant that can:

- ✈️ Research destinations and provide recommendations
- 🌤️ Check weather and local conditions
- 💱 Convert currencies and estimate costs
- 📅 Create detailed itineraries
- 🏨 Search for accommodations (simulated)
- 👥 Coordinate multiple specialized agents
- ✅ Request human approval for bookings
- 💾 Save and resume long planning sessions
- 📊 Monitor performance and debug issues
- 🚀 Deploy to production on Azure

## 💡 Learning Philosophy

- **Progressive Enhancement**: Each notebook adds 1-2 new concepts
- **Real Use Case**: Everything ties back to the Travel Assistant
- **Runnable Code**: Every cell is executable and well-documented
- **Best Practices**: Learn the right patterns from the start

## Additional Resources

- [Azure AI Agent Service Documentation](https://learn.microsoft.com/azure/ai-services/agents/)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)
- [Azure API Management](https://learn.microsoft.com/azure/api-management/)
- [Microsoft Entra ID Authentication](https://learn.microsoft.com/entra/identity-platform/)

---

**Ready to start?** Open `01_basic_agent.ipynb` and begin your journey! 🚀

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Add your tutorial or improvements
4. Submit a pull request

## 📝 License

MIT License - See LICENSE file for details

---

**Last Updated**: December 2025  
**Maintained by**: Community Contributors
