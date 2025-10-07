# Microsoft Agent Framework Workshop# Microsoft Agent Framework Workshop



Comprehensive hands-on workshop for building AI agents using Microsoft's Agent Framework. This repository contains progressive tutorials covering everything from basic agent creation to advanced multi-agent workflows and production monitoring.Comprehensive hands-on workshop for building AI agents using Microsoft's Agent Framework. This repository contains progressive tutorials covering everything from basic agent creation to advanced multi-agent workflows and production monitoring.



## Tutorial Series## Tutorial Series



| # | Tutorial | Topics Covered | Duration || # | Tutorial | Topics Covered | Duration |

|---|----------|----------------|----------||---|----------|----------------|----------|

| 01 | [Basic Agent](./01_basic_agent.ipynb) | Agent creation, responses, OpenAI setup | 15 min || 01 | [Basic Agent](./01_basic_agent.ipynb) | Agent creation, responses, OpenAI setup | 15 min |

| 01b | [Azure AI Foundry](./01b_azure_ai_foundry.ipynb) | Azure deployment, model endpoints | 20 min || 01b | [Azure AI Foundry](./01b_azure_ai_foundry.ipynb) | Azure deployment, model endpoints | 20 min |

| 02 | [Agent with Tools](./02_agent_with_tools.ipynb) | Function calling, tool integration | 25 min || 02 | [Agent with Tools](./02_agent_with_tools.ipynb) | Function calling, tool integration | 25 min |

| 03 | [Multi-turn Conversations](./03_multi_turn_conversations.ipynb) | Context management, conversation flow | 30 min || 03 | [Multi-turn Conversations](./03_multi_turn_conversations.ipynb) | Context management, conversation flow | 30 min |

| 04 | [Context & Memory](./04_context_and_memory.ipynb) | Memory systems, retrieval patterns | 35 min || 04 | [Context & Memory](./04_context_and_memory.ipynb) | Memory systems, retrieval patterns | 35 min |

| 05 | [Middleware & Filters](./05_middleware_and_filters.ipynb) | Request/response pipelines, telemetry | 30 min || 05 | [Middleware & Filters](./05_middleware_and_filters.ipynb) | Request/response pipelines, telemetry | 30 min |

| 06 | [Multi-Agent Workflows](./06_multi_agent_workflows.ipynb) | Agent collaboration, orchestration | 40 min || 06 | [Multi-Agent Workflows](./06_multi_agent_workflows.ipynb) | Agent collaboration, orchestration | 40 min |

| 07 | [Advanced Workflows](./07_advanced_workflows.ipynb) | Complex patterns, state management | 45 min || 07 | [Advanced Workflows](./07_advanced_workflows.ipynb) | Complex patterns, state management | 45 min |

| 08 | [Human-in-the-Loop](./08_human_in_the_loop.ipynb) | Approval workflows, feedback loops | 30 min || 08 | [Human-in-the-Loop](./08_human_in_the_loop.ipynb) | Approval workflows, feedback loops | 30 min |

| 09 | [Error Handling](./09_error_handling_recovery.ipynb) | Retry logic, fault tolerance | 25 min || 09 | [Error Handling](./09_error_handling_recovery.ipynb) | Retry logic, fault tolerance | 25 min |

| 10 | [Azure File Search](./10_azure_file_search_demo.ipynb) | Vector search, RAG patterns | 35 min || 10 | [Azure File Search](./10_azure_file_search_demo.ipynb) | Vector search, RAG patterns | 35 min |

| 10b | [Competitive Intelligence](./10_competitive_intelligence_workflow.ipynb) | Multi-agent workflow, document analysis | 45 min || 10b | [Competitive Intelligence](./10_competitive_intelligence_workflow.ipynb) | Multi-agent workflow, document analysis | 45 min |

| 11 | [DevUI Integration](./11_devui_competitive_intelligence.ipynb) | Development UI, testing workflows | 20 min || 11 | [DevUI Integration](./11_devui_competitive_intelligence.ipynb) | Development UI, testing workflows | 20 min |

| 12 | [Azure Monitor Integration](./12_azure_monitor_alerts.ipynb) | Monitoring, alerting, Log Analytics | 40 min || 12 | [Azure Monitor Integration](./12_azure_monitor_alerts.ipynb) | Monitoring, alerting, Log Analytics | 40 min |

| 13 | [Multi-Agent Pricing Analysis](./13_Pricing-Competitive-Intelligence-multiagent.ipynb) | Advanced orchestration, pricing intelligence | 50 min || 13 | [Multi-Agent Pricing Analysis](./13_Pricing-Competitive-Intelligence-multiagent.ipynb) | Advanced orchestration, pricing intelligence | 50 min |

| 14 | [Unified Web App Monitoring](./14_unified_webapp_agent_monitoring.ipynb) | Log correlation, unified dashboards | 35 min || 14 | [Unified Web App Monitoring](./14_unified_webapp_agent_monitoring.ipynb) | Log correlation, unified dashboards | 35 min |



**Total Learning Time**: ~7 hours**Total Learning Time**: ~7 hours



## Getting Started



### Prerequisites### Special Topics### 🚀 Getting Started



- Python 3.11+- **[OPENAI_VS_AZURE.md](./OPENAI_VS_AZURE.md)** - Choosing between OpenAI and Azure OpenAI

- Azure subscription (for Azure AI Foundry tutorials)

- OpenAI API key or Azure OpenAI endpoint- **[launch_devui.py](./launch_devui.py)** - Development UI for testing agents1. **Install the framework:**



### Setup   ```bash



```bash## 🚀 Quick Start   pip install agent-framework

# Clone the repository

git clone https://github.com/gokoner/microsoft-agent-framework-workshop.git   ```

cd microsoft-agent-framework-workshop

### Prerequisites

# Create virtual environment

python -m venv venv- Python 3.11+2. **Set up your API keys** (create `.env` file):

source venv/bin/activate  # On Windows: venv\Scripts\activate

- Azure subscription (for Azure AI Foundry tutorials)   ```bash

# Install dependencies

pip install azure-ai-projects azure-identity python-dotenv openai mem0ai plotly- OpenAI API key or Azure OpenAI endpoint   OPENAI_API_KEY=sk-...



# Copy environment template   OPENAI_CHAT_MODEL_ID=gpt-4

cp .env.example .env  # Edit with your API keys

```### Setup   ```



### Environment Configuration



Create a `.env` file with the following variables:```bash3. **Start with Notebook 01** and progress sequentially!



```bash# Clone the repository

# OpenAI Configuration

OPENAI_API_KEY=sk-...git clone <your-repo-url>### 📖 What You'll Build

OPENAI_CHAT_MODEL_ID=gpt-4

cd agent-framework-tutorials

# Azure AI Foundry Configuration (for Azure tutorials)

AZURE_OPENAI_ENDPOINT=https://...By the end, you'll have a production-ready Travel Assistant that can:

AZURE_OPENAI_API_KEY=...

AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4# Create virtual environment- ✈️ Research destinations and provide recommendations



# Azure Monitor Configuration (for monitoring tutorials)python -m venv venv- 🌤️ Check weather and local conditions

WORKSPACE_ID=...

WORKSPACE_NAME=...source venv/bin/activate  # On Windows: venv\Scripts\activate- 💱 Convert currencies and estimate costs

```

- 📅 Create detailed itineraries

### Run Your First Agent

# Install dependencies- 🏨 Search for accommodations (simulated)

```bash

jupyter notebook 01_basic_agent.ipynbpip install azure-ai-agent-framework python-dotenv- 👥 Coordinate multiple specialized agents

```

- ✅ Request human approval for bookings

## Documentation

# Copy environment template- 💾 Save and resume long planning sessions

- [Official Documentation](https://learn.microsoft.com/en-us/azure/ai-services/agents/)

- [API Reference](https://learn.microsoft.com/python/api/overview/azure/ai-projects)cp .env.example .env  # Edit with your API keys- 📊 Monitor performance and debug issues

- [GitHub Repository](https://github.com/microsoft/azure-sdk-for-python/tree/main/sdk/ai/azure-ai-projects)

```- 🚀 Deploy to production on Azure

## Special Topics



- [OPENAI_VS_AZURE.md](./OPENAI_VS_AZURE.md) - Choosing between OpenAI and Azure OpenAI

- [START_HERE.md](./START_HERE.md) - Detailed setup guide### Run Your First Agent### 💡 Learning Philosophy

- [LEARNING_PATH.md](./LEARNING_PATH.md) - Structured curriculum

- [launch_devui.py](./launch_devui.py) - Development UI for testing agents



## Azure Resources Included```bash- **Progressive Enhancement**: Each notebook adds 1-2 new concepts



### Azure Workbooksjupyter notebook 01_basic_agent.ipynb- **Real Use Case**: Everything ties back to the Travel Assistant

- **ai_agent_monitoring_workbook_openai_style.json** - Production-ready Azure Monitor workbook with:

  - Service health overview```- **Runnable Code**: Every cell is executable and well-documented

  - Performance trends

  - Cost and usage insights- **Best Practices**: Learn the right patterns from the start

  - Error correlation

  - Built-in monitoring guide## 📖 Documentation



### Sample Data### 🔗 Additional Resources

- **sample_data/competitive_analysis/** - Example data for pricing intelligence workflows

  - Input PDF documents- **Azure AI Agent Framework**: [Official Docs](https://learn.microsoft.com/azure/ai-services/agents/)

  - Extracted product data

  - Generated analysis reports- **API Reference**: [Python SDK](https://learn.microsoft.com/python/api/overview/azure/ai-agent-framework)- [Official Documentation](https://learn.microsoft.com/en-us/agent-framework/)



## Real-World Applications- **Samples**: [GitHub Examples](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/ai/azure-ai-agent-framework)- [GitHub Repository](https://github.com/microsoft/agent-framework)



The tutorials in this workshop demonstrate patterns used in production systems:- [More Samples](../agent-framework/python/samples/)



- Multi-agent orchestration for complex workflows## 🎯 Real-World Applications

- Azure Document Intelligence integration

- Persistent memory with Mem0---

- Azure Monitor integration for observability

- Log correlation across multiple servicesAfter completing these tutorials, check out the **[Competitive Intelligence Project](https://github.com/gkoneru/microsoft-agent-framework-samples)** for a production example using:

- Cost optimization and performance monitoring

- Multi-agent workflows**Ready to start?** Open `01_basic_agent.ipynb` and begin your journey! 🚀

## Contributing

- Azure Document Intelligence

Contributions welcome! Please:- Microsoft Fabric integration

1. Fork the repository- Mem0 persistent memory

2. Create a feature branch

3. Add your tutorial or improvements## 🤝 Contributing

4. Submit a pull request

Contributions welcome! Please:

## License1. Fork the repository

2. Create a feature branch

MIT License - See LICENSE file for details3. Add your tutorial or improvements

4. Submit a pull request

## Related Projects

## 📝 License

- [Azure AI Samples](https://github.com/Azure-Samples/azure-ai-samples) - Official Azure AI examples

- [Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python) - Azure SDK repositoryMIT License - See LICENSE file for details



---## 🔗 Related Projects



**Last Updated**: October 2025  - **[Competitive Intelligence Agent](https://github.com/gkoneru/microsoft-agent-framework-samples)** - Production multi-agent system for pricing analysis

**Repository**: https://github.com/gokoner/microsoft-agent-framework-workshop- **[Azure AI Samples](https://github.com/Azure-Samples/azure-ai-samples)** - Official Azure AI examples


---

**Last Updated**: October 2025  
**Maintained by**: Community Contributors
