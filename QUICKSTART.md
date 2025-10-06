# 🚀 Quick Start Guide

## Welcome to the Microsoft Agent Framework Tutorial Series!

This tutorial series will teach you everything about building AI agents using the Microsoft Agent Framework, from basics to production deployment.

## 📦 What I've Created For You

### Tutorial Structure
I've set up a comprehensive learning path with **12 progressive notebooks** that build a real-world **Personal Travel Assistant**:

**✅ Ready Now:**
- `01_basic_agent.ipynb` - Your first agent (START HERE!)
- `01b_azure_ai_foundry.ipynb` - Azure AI Foundry agents (enterprise)
- `02_agent_with_tools.ipynb` - Add tools and function calling

**🚧 Coming Soon** (I can create these as you progress):
- `03_multi_turn_conversations.ipynb` - Stateful conversations with threads
- `04_context_and_memory.ipynb` - Agent memory and preferences
- `05_middleware_and_filters.ipynb` - Safety and logging
- `06_multimodal_input.ipynb` - Process images
- `07_basic_workflows.ipynb` - Multi-step workflows
- `08_multi_agent_orchestration.ipynb` - Multiple agents working together
- `09_human_in_the_loop.ipynb` - Approval flows
- `10_checkpointing_and_state.ipynb` - Save and resume workflows
- `11_observability.ipynb` - Monitoring and tracing
- `12_deployment_patterns.ipynb` - Deploy to Azure

## 🎯 How to Use This Tutorial

### 🚀 Getting Started

#### Choose Your Path

**Option A: OpenAI (Recommended for Learning)**
- ✅ Fastest setup - just need an API key
- ✅ Great for prototypes and learning
- Start with Tutorial 01

**Option B: Azure AI Foundry (Recommended for Production)**
- ✅ Enterprise security and compliance
- ✅ Built-in monitoring and content safety
- ✅ Advanced tools (code interpreter, Bing search)
- Start with Tutorial 01b

You can use both! The code is very similar.

#### Setup Instructions

1. **Install the framework:**
   ```bash
   # For OpenAI
   pip install agent-framework
   
   # For Azure AI Foundry (includes core)
   pip install agent-framework-azure-ai
   ```

2. **Set up authentication** (create `.env` file):
   
   **For OpenAI:**
   ```bash
   OPENAI_API_KEY=sk-...
   OPENAI_CHAT_MODEL_ID=gpt-4o-mini
   ```
   
   **For Azure AI Foundry:**
   ```bash
   # Run this first: az login
   AZURE_AI_PROJECT_ENDPOINT=https://your-project.api.azureml.ms
   AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
   ```

3. **Start learning:**
   - OpenAI users → `01_basic_agent.ipynb`
   - Azure users → `01b_azure_ai_foundry.ipynb`
   - Both? Do both! 🚀

## 💡 Learning Philosophy

Each notebook:
- **Adds 1-2 new concepts** - Not overwhelming
- **Uses the same use case** - Everything builds on the Travel Assistant
- **Has runnable code** - Every cell works
- **Includes exercises** - Practice what you learn
- **Shows best practices** - Learn the right way from the start

## 📖 What You'll Learn

### Level 1: Foundations
- How to create and configure agents
- Adding tools for real-world capabilities
- Managing conversations and state

### Level 2: Intermediate
- Agent memory and context
- Safety with middleware and filters
- Processing different input types (images, etc.)

### Level 3: Advanced
- Building complex workflows
- Multi-agent orchestration patterns
- Human-in-the-loop scenarios

### Level 4: Production
- State management and checkpointing
- Observability and monitoring
- Deployment to Azure

## 🎓 Recommended Path

1. **Complete tutorials in order** - Each builds on previous concepts
2. **Do the exercises** - Practice reinforces learning
3. **Experiment** - Modify code, break things, learn!
4. **Build your own** - Apply concepts to your use case

## 🆘 Need Help?

- **Documentation**: https://learn.microsoft.com/en-us/agent-framework/
- **GitHub**: https://github.com/microsoft/agent-framework
- **Samples**: Check `/agent-framework/python/samples/`

## 🎉 Ready to Start?

**Open `01_basic_agent.ipynb` now!**

The first two tutorials are complete and ready for you. As you progress, let me know and I'll create the next ones!

---

**Pro Tip**: Run each cell sequentially and read the explanations. The notebooks are designed to be self-contained learning experiences.
