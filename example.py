import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient
from azure.identity import ClientSecretCredential


subscription_id='b7dbff07-d686-4eb9-8f9c-e9d64701f837'
azure_tenant_id='d25717e8-e3fd-4d3e-98a3-e889601485b3'
azure_client_id='5930eb5e-51fe-49c6-b22c-06764d6c4092'
azure_secret_id='USC8Q~f_9MuAoCPYr4SdMemsBT4hfIwvlEP1Zbm0'

#subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")
#credentials= DefaultAzureCredential()
credentials = ClientSecretCredential(
    client_id=azure_client_id,
    client_secret=azure_secret_id,
    tenant_id=azure_tenant_id
)
compute_client = ComputeManagementClient(credential=credentials, subscription_id=subscription_id)

#print(credentials,subscription_id)
client = ResourceManagementClient(credentials, subscription_id)
#resource_group_params = {'location':'eastus'}
#client.resource_groups.create_or_update('azure-sample-group', resource_group_params)
#vminstanceview['properties']['instanceView']['statuses'][1]['displayStatus']
def list_virtual_machines():
    for vm in compute_client.virtual_machines.list_all():
        #print({vm.hardware_profile.vm_size})
        print(vm.name)
        print(vm.vm_id)
        
       # print(vm['properties']['instanceView']['statuses'][1]['displayStatus'])
        

list_virtual_machines()
#resource_group_params = {'location':'eastus'}

for item in client.resource_groups.list():
    print(item)
    

 

    

 