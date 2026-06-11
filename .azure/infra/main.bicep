param location string = resourceGroup().location
param aiProjectName string
param containerRegistryName string

resource aiProject 'Microsoft.MachineLearningServices/workspaces@2024-01-01-preview' existing = {
  name: aiProjectName
}

resource containerRegistry 'Microsoft.ContainerRegistry/registries@2023-07-01' existing = {
  name: containerRegistryName
}

output projectEndpoint string = aiProject.properties.discoveryUrl