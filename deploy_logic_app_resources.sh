#!/bin/bash
set -e

echo "================================================================"
echo "Creating Azure Resources for Logic Apps MCP Server"
echo "================================================================"

# Variables - use unique suffix for globally unique names
UNIQUE_SUFFIX=$(echo $RANDOM | md5 | head -c 6)
RESOURCE_GROUP="rg-mcp-servers"
LOCATION="eastus"
API_CENTER_NAME="gk-mcp-apicenter-${UNIQUE_SUFFIX}"
LOGIC_APP_NAME="travel-assistant-mcp-${UNIQUE_SUFFIX}"
STORAGE_ACCOUNT="mcplogicapp${UNIQUE_SUFFIX}"

echo ""
echo "Using the following resource names:"
echo "  Resource Group:   $RESOURCE_GROUP"
echo "  API Center:       $API_CENTER_NAME"
echo "  Logic App:        $LOGIC_APP_NAME"
echo "  Storage Account:  $STORAGE_ACCOUNT"

# 1. Create Resource Group (if not exists)
echo ""
echo "Step 1: Creating resource group..."
az group create \
  --name $RESOURCE_GROUP \
  --location $LOCATION \
  --output table

# 2. Create Azure API Center
echo ""
echo "Step 2: Creating Azure API Center..."
az apic create \
  --name $API_CENTER_NAME \
  --resource-group $RESOURCE_GROUP \
  --location $LOCATION \
  --output table

# 3. Create Storage Account for Logic App
echo ""
echo "Step 3: Creating storage account for Logic App..."
az storage account create \
  --name $STORAGE_ACCOUNT \
  --resource-group $RESOURCE_GROUP \
  --location $LOCATION \
  --sku Standard_LRS \
  --output table

# 4. Create Standard Logic App (Workflow Service Plan)
echo ""
echo "Step 4: Creating Standard Logic App..."
az logicapp create \
  --name $LOGIC_APP_NAME \
  --resource-group $RESOURCE_GROUP \
  --storage-account $STORAGE_ACCOUNT \
  --output table

echo ""
echo "================================================================"
echo "Resources Created Successfully!"
echo "================================================================"
echo ""
echo "API Center Portal: https://${API_CENTER_NAME}.${LOCATION}.azure-apicenter.ms"
echo ""
echo "Next Steps:"
echo "1. Open Azure Portal: https://portal.azure.com"
echo "2. Navigate to API Center: $API_CENTER_NAME"
echo "3. Go to: Discovery > MCP (Preview)"
echo "4. Click 'Register' on the Azure Logic Apps tile"
echo "5. Select Logic App: $LOGIC_APP_NAME"
echo "6. Add connector actions as MCP tools"
echo ""
echo "Save these values to your .env file:"
echo "  API_CENTER_NAME=$API_CENTER_NAME"
echo "  LOGIC_APP_NAME=$LOGIC_APP_NAME"
echo ""
echo "================================================================"
