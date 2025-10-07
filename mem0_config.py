"""
Mem0 Azure AI Configuration Helper

This module provides configuration for Mem0 using Azure AI Search and Azure OpenAI.
Based on: https://devblogs.microsoft.com/foundry/azure-ai-mem0-integration/
"""

import os
import json
from typing import Dict, Any, Optional


def get_mem0_config_azure() -> Dict[str, Any]:
    """
    Get Mem0 configuration for Azure AI Search + Azure OpenAI.
    
    Uses Azure AI Search as vector store and Azure OpenAI for embeddings/LLM.
    Reference: https://devblogs.microsoft.com/foundry/azure-ai-mem0-integration/
    
    Returns:
        Dictionary with Mem0 configuration for Azure services
    """
    
    # Get Azure OpenAI configuration
    azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    azure_openai_api_key = os.getenv("AZURE_OPENAI_API_KEY")
    azure_openai_api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-10-21")
    chat_model = os.getenv("AZURE_OPENAI_CHAT_COMPLETION_DEPLOYED_MODEL_NAME", "gpt-4.1")
    embedding_model = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYED_MODEL_NAME", "text-embedding-3-small")
    
    # Get Azure AI Search configuration
    search_service_name = os.getenv("AZURE_SEARCH_SERVICE_NAME") or os.getenv("SEARCH_SERVICE_NAME")
    search_api_key = os.getenv("AZURE_SEARCH_ADMIN_KEY") or os.getenv("SEARCH_SERVICE_API_KEY")
    
    config = {
        "vector_store": {
            "provider": "azure_ai_search",
            "config": {
                "service_name": search_service_name,
                "api_key": search_api_key,
                "collection_name": "competitive_intelligence_memories",
                "embedding_model_dims": 1536,
            },
        },
        "embedder": {
            "provider": "azure_openai",
            "config": {
                "model": embedding_model,
                "embedding_dims": 1536,
                "azure_kwargs": {
                    "api_version": azure_openai_api_version,
                    "azure_deployment": embedding_model,
                    "azure_endpoint": azure_openai_endpoint,
                    "api_key": azure_openai_api_key,
                },
            },
        },
        "llm": {
            "provider": "azure_openai",
            "config": {
                "model": chat_model,
                "temperature": 0.1,
                "max_tokens": 2000,
                "azure_kwargs": {
                    "azure_deployment": chat_model,
                    "api_version": azure_openai_api_version,
                    "azure_endpoint": azure_openai_endpoint,
                    "api_key": azure_openai_api_key,
                },
            },
        },
        "version": "v1.1",
    }
    
    return config


def init_mem0_azure() -> Optional[Any]:
    """
    Initialize Mem0 with Azure AI Search + Azure OpenAI.
    
    This is the recommended approach for Azure-based deployments.
    Uses Azure AI Search for vector storage and Azure OpenAI for embeddings/LLM.
    
    Returns:
        Mem0 Memory instance or None if initialization fails
    """
    try:
        from mem0 import Memory
        
        config = get_mem0_config_azure()
        
        # Save config to environment for agent-framework-mem0
        os.environ["MEM0_CONFIG"] = json.dumps(config)
        
        # Initialize and return Memory instance
        memory = Memory.from_config(config)
        print("✅ Mem0 initialized with Azure AI Search + Azure OpenAI")
        return memory
        
    except Exception as e:
        print(f"⚠️  Mem0 initialization failed: {e}")
        import traceback
        traceback.print_exc()
        return None


def check_azure_mem0_services() -> Dict[str, bool]:
    """
    Check if required Azure services for Mem0 are configured.
    
    Returns:
        Dictionary with service availability status
    """
    
    status = {
        "azure_openai": False,
        "azure_search": False,
        "embedding_model": False,
    }
    
    # Check Azure OpenAI configuration
    if (os.getenv("AZURE_OPENAI_ENDPOINT") and 
        os.getenv("AZURE_OPENAI_API_KEY") and
        os.getenv("AZURE_OPENAI_CHAT_COMPLETION_DEPLOYED_MODEL_NAME")):
        status["azure_openai"] = True
    
    # Check Azure AI Search configuration
    search_name = os.getenv("AZURE_SEARCH_SERVICE_NAME") or os.getenv("SEARCH_SERVICE_NAME")
    search_key = os.getenv("AZURE_SEARCH_ADMIN_KEY") or os.getenv("SEARCH_SERVICE_API_KEY")
    if search_name and search_key:
        status["azure_search"] = True
    
    # Check embedding model deployment
    if os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYED_MODEL_NAME"):
        status["embedding_model"] = True
    
    return status


def print_azure_mem0_status():
    """Print Mem0 Azure AI setup status."""
    
    status = check_azure_mem0_services()
    
    print("\n" + "="*70)
    print("🔧 MEM0 AZURE AI STATUS")
    print("="*70)
    
    # Azure OpenAI
    if status["azure_openai"]:
        endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        model = os.getenv("AZURE_OPENAI_CHAT_COMPLETION_DEPLOYED_MODEL_NAME")
        print(f"✅ Azure OpenAI configured")
        print(f"   Endpoint: {endpoint}")
        print(f"   Chat Model: {model}")
    else:
        print(f"❌ Azure OpenAI not configured")
        print(f"   Required: AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_KEY,")
        print(f"            AZURE_OPENAI_CHAT_COMPLETION_DEPLOYED_MODEL_NAME")
    
    # Embedding Model
    if status["embedding_model"]:
        embed_model = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYED_MODEL_NAME")
        print(f"✅ Embedding model: {embed_model}")
    else:
        print(f"❌ Embedding model not configured")
        print(f"   Required: AZURE_OPENAI_EMBEDDING_DEPLOYED_MODEL_NAME")
        print(f"   Note: You may need to deploy 'text-embedding-3-small' in Azure")
    
    # Azure AI Search
    if status["azure_search"]:
        search_name = os.getenv("AZURE_SEARCH_SERVICE_NAME") or os.getenv("SEARCH_SERVICE_NAME")
        search_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT") or os.getenv("SEARCH_SERVICE_ENDPOINT")
        print(f"✅ Azure AI Search configured")
        print(f"   Service: {search_name}")
        print(f"   Endpoint: {search_endpoint}")
    else:
        print(f"❌ Azure AI Search not configured")
        print(f"   Required: AZURE_SEARCH_SERVICE_NAME, AZURE_SEARCH_ADMIN_KEY")
    
    print("="*70)
    
    if all(status.values()):
        print("✅ All Azure services ready for Mem0!")
    else:
        print("⚠️  Some services are not configured - see messages above")
    
    print("="*70 + "\n")
    
    return all(status.values())


# Quick start example
if __name__ == "__main__":
    # Load environment variables
    from dotenv import load_dotenv
    load_dotenv()
    
    # Check status
    all_ready = print_azure_mem0_status()
    
    if all_ready:
        print("\n🚀 Initializing Mem0 with Azure AI Search + Azure OpenAI...\n")
        
        # Initialize Mem0
        memory = init_mem0_azure()
        
        if memory:
            print("\n✅ Mem0 initialized successfully!")
            
            # Test memory operations
            print("\n📝 Testing memory operations...")
            test_user = "test_competitive_intel"
            
            # Add a test memory
            memory.add(
                "User is analyzing Haworth and Knoll furniture pricing for competitive intelligence.",
                user_id=test_user
            )
            
            # Search for it
            results = memory.search("competitive intelligence", user_id=test_user)
            print(f"\n� Test search results: {len(results.get('results', []))} memories found")
            
            if results.get('results'):
                for i, result in enumerate(results['results'][:3], 1):
                    print(f"   {i}. {result['memory']} (Score: {result.get('score', 0):.4f})")
        else:
            print("\n❌ Mem0 initialization failed")
    else:
        print("\n⚠️  Please configure Azure services in .env file")
        print("    See .env for required environment variables")
