# Azure AI Agent Framework - Tutorials# Microsoft Agent Framework - Progressive Tutorial Series



Comprehensive learning path for building AI agents using Microsoft's Azure AI Agent Framework (`azure-ai-agent-framework`).## 🎯 Learning Path: Personal Travel Assistant



## 📚 Learning PathThis tutorial series teaches you Microsoft Agent Framework by building a **Personal Travel Assistant** that grows in capability with each lesson. You'll learn all major features through hands-on, practical examples.



This repository contains hands-on tutorials covering everything from basic agent creation to advanced multi-agent workflows.### 📚 Tutorial Structure



### Getting StartedEach notebook builds on the previous one, introducing new concepts while enhancing our Travel Assistant:

1. **[START_HERE.md](./START_HERE.md)** - Setup guide and prerequisites

2. **[QUICKSTART.md](./QUICKSTART.md)** - Quick 5-minute agent#### **Level 1: Foundations** (Notebooks 01-03)

3. **[LEARNING_PATH.md](./LEARNING_PATH.md)** - Structured curriculum- **01_basic_agent.ipynb** - Your first agent: Simple travel recommendations

- **01b_azure_ai_foundry.ipynb** - Azure AI Foundry: Enterprise-ready agents

### Tutorial Series- **02_agent_with_tools.ipynb** - Add function calling: Weather, currency converter

- **03_multi_turn_conversations.ipynb** - Stateful conversations with threads

| # | Tutorial | Topics Covered | Duration |

|---|----------|----------------|----------|#### **Level 2: Intermediate** (Notebooks 04-06)

| 01 | [Basic Agent](./01_basic_agent.ipynb) | Agent creation, responses, OpenAI setup | 15 min |- **04_context_and_memory.ipynb** - Add memory: Remember user preferences

| 01b | [Azure AI Foundry](./01b_azure_ai_foundry.ipynb) | Azure deployment, model endpoints | 20 min |- **05_middleware_and_filters.ipynb** - Add safety: Content filtering, logging

| 02 | [Agent with Tools](./02_agent_with_tools.ipynb) | Function calling, tool integration | 25 min |- **06_multimodal_input.ipynb** - Process images: Landmark identification

| 03 | [Multi-turn Conversations](./03_multi_turn_conversations.ipynb) | Context management, conversation flow | 30 min |

| 04 | [Context & Memory](./04_context_and_memory.ipynb) | Memory systems, retrieval patterns | 35 min |#### **Level 3: Advanced** (Notebooks 07-09)

| 05 | [Middleware & Filters](./05_middleware_and_filters.ipynb) | Request/response pipelines, telemetry | 30 min |- **07_basic_workflows.ipynb** - Multi-step planning: Itinerary creation

| 06 | [Multi-Agent Workflows](./06_multi_agent_workflows.ipynb) | Agent collaboration, orchestration | 40 min |- **08_multi_agent_orchestration.ipynb** - Agent collaboration: Research + Planning + Booking

| 07 | [Advanced Workflows](./07_advanced_workflows.ipynb) | Complex patterns, state management | 45 min |- **09_human_in_the_loop.ipynb** - Approval flows: Budget and booking confirmations

| 08 | [Human-in-the-Loop](./08_human_in_the_loop.ipynb) | Approval workflows, feedback loops | 30 min |

| 09 | [Error Handling](./09_error_handling_recovery.ipynb) | Retry logic, fault tolerance | 25 min |#### **Level 4: Production** (Notebooks 10-12)

| 10 | [Azure File Search](./10_azure_file_search_demo.ipynb) | Vector search, RAG patterns | 35 min |

#### **Level 5: Enterprise MCP Server Pattern** (Notebooks 15-19)

| # | Tutorial | Topics Covered | Duration |
|---|----------|----------------|----------|
| 15 | [FastMCP Server Basics](./15_fastmcp_server_basics.ipynb) | Building MCP servers, local tools, Azure AI observability | 45 min |
| 16 | [Deploy FastMCP to Azure](./16_deploy_fastmcp_to_aca.ipynb) | Docker, Azure Container Apps, hosted MCP tools | 60 min |
| 17 | [Logic Apps MCP Server](./17_logic_app_mcp_server.ipynb) | No-code MCP tools, Azure API Center | 50 min |
| 18 | [API Management Integration](./18_apim_mcp_integration.ipynb) | Enterprise gateway, security policies | 45 min |
| 19 | [Orchestrating Agent with MCP](./19_orchestrating_agent_with_mcp.ipynb) | Multi-server workflows, production patterns | 60 min |

**Total Learning Time**: ~11 hours



### Special Topics### 🌟 What's in the Enterprise MCP Pattern?

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

### 🚀 Getting Started

- **[OPENAI_VS_AZURE.md](./OPENAI_VS_AZURE.md)** - Choosing between OpenAI and Azure OpenAI

- **[launch_devui.py](./launch_devui.py)** - Development UI for testing agents

1. **Install the framework:**

   ```bash

## 🚀 Quick Start   pip install agent-framework

   ```

### Prerequisites

- Python 3.11+2. **Set up your API keys** (create `.env` file):

- Azure subscription (for Azure AI Foundry tutorials)   ```bash

- OpenAI API key or Azure OpenAI endpoint   OPENAI_API_KEY=sk-...

   OPENAI_CHAT_MODEL_ID=gpt-4

### Setup   ```



```bash3. **Start with Notebook 01** and progress sequentially!

# Clone the repository

git clone <your-repo-url>### 📖 What You'll Build

cd agent-framework-tutorials

By the end, you'll have a production-ready Travel Assistant that can:

# Create virtual environment- ✈️ Research destinations and provide recommendations

python -m venv venv- 🌤️ Check weather and local conditions

source venv/bin/activate  # On Windows: venv\Scripts\activate- 💱 Convert currencies and estimate costs

- 📅 Create detailed itineraries

# Install dependencies- 🏨 Search for accommodations (simulated)

pip install azure-ai-agent-framework python-dotenv- 👥 Coordinate multiple specialized agents

- ✅ Request human approval for bookings

# Copy environment template- 💾 Save and resume long planning sessions

cp .env.example .env  # Edit with your API keys- 📊 Monitor performance and debug issues

```- 🚀 Deploy to production on Azure



### Run Your First Agent### 💡 Learning Philosophy



```bash- **Progressive Enhancement**: Each notebook adds 1-2 new concepts

jupyter notebook 01_basic_agent.ipynb- **Real Use Case**: Everything ties back to the Travel Assistant

```- **Runnable Code**: Every cell is executable and well-documented

- **Best Practices**: Learn the right patterns from the start

## 📖 Documentation

### 🔗 Additional Resources

- **Azure AI Agent Framework**: [Official Docs](https://learn.microsoft.com/azure/ai-services/agents/)

- **API Reference**: [Python SDK](https://learn.microsoft.com/python/api/overview/azure/ai-agent-framework)- [Official Documentation](https://learn.microsoft.com/en-us/agent-framework/)

- **Samples**: [GitHub Examples](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/ai/azure-ai-agent-framework)- [GitHub Repository](https://github.com/microsoft/agent-framework)

- [More Samples](../agent-framework/python/samples/)

## 🎯 Real-World Applications

---

After completing these tutorials, check out the **[Competitive Intelligence Project](https://github.com/gkoneru/microsoft-agent-framework-samples)** for a production example using:

- Multi-agent workflows**Ready to start?** Open `01_basic_agent.ipynb` and begin your journey! 🚀

- Azure Document Intelligence
- Microsoft Fabric integration
- Mem0 persistent memory

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Add your tutorial or improvements
4. Submit a pull request

## 📝 License

MIT License - See LICENSE file for details

## 🔗 Related Projects

- **[Competitive Intelligence Agent](https://github.com/gkoneru/microsoft-agent-framework-samples)** - Production multi-agent system for pricing analysis
- **[Azure AI Samples](https://github.com/Azure-Samples/azure-ai-samples)** - Official Azure AI examples

---

**Last Updated**: October 2025  
**Maintained by**: Community Contributors
