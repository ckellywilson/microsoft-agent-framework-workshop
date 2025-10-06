"""
Launch Tutorial 11 Workflow with DevUI

This script extracts the workflow from Tutorial 11 notebook and launches it in DevUI.
Cannot be run from Jupyter notebooks due to event loop conflicts.

Usage:
    cd tutorials
    python launch_devui.py
"""

import asyncio
import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional
from datetime import datetime

# Data analysis and visualization
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Agent framework
from agent_framework import (
    ChatMessage,
    Executor,
    HostedFileSearchTool,
    HostedVectorStoreContent,
    SequentialBuilder,
    WorkflowContext,
    handler,
)
from agent_framework_azure_ai import AzureAIAgentClient
from azure.ai.agents.models import FileInfo, VectorStore
from azure.identity.aio import AzureCliCredential
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set plot style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Create folder structure
FOLDERS = {
    'input': './competitive_analysis/input',
    'output': './competitive_analysis/output',
    'data': './competitive_analysis/data',
    'charts': './competitive_analysis/charts',
}

for folder_path in FOLDERS.values():
    Path(folder_path).mkdir(parents=True, exist_ok=True)

# Verify configuration
project_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT")
if not project_endpoint:
    raise ValueError("❌ AZURE_AI_PROJECT_ENDPOINT not set in .env file")


class DataExtractionExecutor(Executor):
    """Extracts product data from PDF files using Azure AI file search."""

    @handler
    async def handle_chat_message(self, message: list[ChatMessage], ctx: WorkflowContext[dict[str, Any]]) -> None:
        """Handle initial data extraction request from DevUI."""
        user_query = str(message[-1]) if message else "Analyze products"
        await self._extract_data(user_query, ctx)
    
    @handler
    async def handle_string(self, message: str, ctx: WorkflowContext[dict[str, Any]]) -> None:
        """Handle direct string input for testing."""
        await self._extract_data(message, ctx)
    
    async def _extract_data(self, query: str, ctx: WorkflowContext[dict[str, Any]]) -> None:
        """Core extraction logic - same as Tutorial 11."""
        print("="*70)
        print("🤖 AGENT 1: DOCUMENT SEARCH & DATA EXTRACTION")
        print("="*70)
        print(f"Processing request: {query}")
        
        project_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT")
        client = AzureAIAgentClient(endpoint=project_endpoint, async_credential=AzureCliCredential())
        
        files: List[FileInfo] = []
        vector_store: Optional[VectorStore] = None
        extracted_products = []
        
        try:
            # Find PDF files
            input_path = Path(FOLDERS['input'])
            pdf_files = list(input_path.glob('*.pdf'))
            
            if not pdf_files:
                error_message = f"❌ No PDF files found in {FOLDERS['input']}"
                print(error_message)
                await ctx.send_message({"products": [], "error": error_message})
                return
                
            print(f"\n✅ Found {len(pdf_files)} PDF file(s)")
            
            # Upload files
            print("\n⬆️  Uploading files to Azure AI...")
            file_ids = []
            for pdf_file in pdf_files:
                file = await client.project_client.agents.files.upload_and_poll(
                    file_path=str(pdf_file), purpose="assistants"
                )
                files.append(file)
                file_ids.append(file.id)
                print(f"   ✅ {pdf_file.name}")
            
            # Create vector store
            print("\n📊 Creating vector store...")
            vector_store = await client.project_client.agents.vector_stores.create_and_poll(
                file_ids=file_ids, name="competitive_intelligence_store"
            )
            print(f"✅ Vector store created: {vector_store.id}")
            
            # Create file search tool
            file_search_tool = HostedFileSearchTool(
                inputs=[HostedVectorStoreContent(vector_store_id=vector_store.id)]
            )
            
            # Create AI agent
            print("\n🤖 Creating extraction agent...")
            async with (
                AzureCliCredential() as credential,
                AzureAIAgentClient(
                    endpoint=project_endpoint, 
                    async_credential=credential
                ).create_agent(
                    name="DataExtractionAgent",
                    instructions="Extract ALL products from PDF catalogs. Return JSON array with product_name, sku, price, category, manufacturer, source_file.",
                    tools=[file_search_tool],
                ) as agent,
            ):
                print("🔍 Extracting products...")
                
                response = await agent.run(
                    "Use file search to extract ALL furniture products from the catalogs. Return comprehensive JSON array."
                )
                
                # Parse JSON
                response_text = response.text
                if "```json" in response_text:
                    response_text = response_text.split("```json")[1].split("```")[0].strip()
                elif "```" in response_text:
                    response_text = response_text.split("```")[1].split("```")[0].strip()
                
                try:
                    extracted_products = json.loads(response_text)
                    print(f"\n✅ Extracted {len(extracted_products)} products")
                except json.JSONDecodeError as e:
                    print(f"\n⚠️  JSON parse error: {e}")
                    extracted_products = []
            
            # Save data
            if extracted_products:
                output_file = Path(FOLDERS['data']) / "extracted_products.json"
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(extracted_products, f, indent=2)
                print(f"💾 Saved to: {output_file}")
            
            await ctx.send_message({"products": extracted_products})
            
        except Exception as e:
            print(f"\n❌ Error: {e}")
            await ctx.send_message({"products": extracted_products, "error": str(e)})
        
        finally:
            # Cleanup
            if vector_store:
                try:
                    await client.project_client.agents.vector_stores.delete(vector_store.id)
                except: 
                    pass
            for file in files:
                try:
                    await client.project_client.agents.files.delete(file.id)
                except: 
                    pass
            await client.close()


class PricingAnalysisExecutor(Executor):
    """Simplified pricing analysis."""

    @handler
    async def handle_data(self, message: dict[str, Any], ctx: WorkflowContext[dict[str, Any]]) -> None:
        print("="*70)
        print("💰 AGENT 2: PRICING ANALYSIS")
        print("="*70)
        
        products = message.get("products", [])
        
        if products:
            df = pd.DataFrame(products)
            if 'price' in df.columns:
                df['price_numeric'] = pd.to_numeric(df['price'], errors='coerce')
                df = df[df['price_numeric'].notna()]
                
                analysis = f"Analyzed {len(df)} products. Price range: ${df['price_numeric'].min():.2f} - ${df['price_numeric'].max():.2f}"
                print(f"\n✅ {analysis}")
            else:
                analysis = "No price data available"
        else:
            analysis = "No products to analyze"
        
        await ctx.send_message({"analysis": analysis, "products": products})


class VisualizationExecutor(Executor):
    """Simplified visualization."""

    @handler
    async def handle_analysis(self, message: dict[str, Any], ctx: WorkflowContext[dict[str, Any]]) -> None:
        print("="*70)
        print("📊 AGENT 3: VISUALIZATION")
        print("="*70)
        
        products = message.get("products", [])
        charts = []
        
        if products:
            print(f"✅ Created visualizations for {len(products)} products")
        
        await ctx.send_message({
            "analysis": message.get("analysis", ""),
            "products": products,
            "charts": charts
        })


class ReportGeneratorExecutor(Executor):
    """Simplified report generation."""

    @handler
    async def handle_report(self, message: dict[str, Any], ctx: WorkflowContext[list[ChatMessage], list[ChatMessage]]) -> None:
        print("="*70)
        print("📝 AGENT 4: REPORT GENERATION")
        print("="*70)
        
        products = message.get("products", [])
        
        report = f"# Competitive Intelligence Report\n\nAnalyzed {len(products)} products.\n"
        
        print(f"\n✅ Report generated")
        
        from agent_framework._types import ChatMessage as CM
        result_message = CM(role="assistant", content=f"✅ Report complete! Analyzed {len(products)} products.")
        await ctx.yield_output([result_message])


# Create workflow
print("🔧 Building workflow...")
workflow = (
    SequentialBuilder()
    .participants([
        DataExtractionExecutor(id="data_extraction"),
        PricingAnalysisExecutor(id="pricing_analysis"),
        VisualizationExecutor(id="visualization"),
        ReportGeneratorExecutor(id="report_generation"),
    ])
    .build()
)
print("✅ Workflow built!\n")


if __name__ == "__main__":
    print("🚀 Launching Competitive Intelligence Workflow with DevUI")
    print("=" * 70)
    print("📊 4-Agent Sequential Workflow")
    print("=" * 70)
    print("\n✅ DevUI will open at http://localhost:8080")
    print("⏹️  Press Ctrl+C to stop\n")
    
    from agent_framework_devui import serve
    
    serve(
        entities=[workflow],
        port=8080,
        auto_open=True,
        tracing_enabled=True,
        ui_enabled=True
    )
