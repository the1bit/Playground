#!/usr/bin/python3

#----------------------------------------------
# Author: Tibor Kiss
# Version: 1.0
# Release date: 15.12.2017
#----------------------------------------------
# Azure module for Python 3
# collection of azure functions for python.
#----------------------------------------------

import pip  # to install pip packages
import os
import getpass  # only required for reading user password if not set


# FUNCTION: Cloud Environment list
def cloud_list(options):
	print("Please choose the right cloud (default: AZURE_GERMAN_CLOUD):")
	for idx, element in enumerate(options):
		print("{}) {}".format(idx+1,element))
	i = input("Enter number: ")
	try:
		if 0 < int(i) <= len(options):
			return int(i)-1
	except:
		pass
	return int(0)

# Manage login to Azure
# def manageLogin():
	# Prefered way for Azure connection is the use of ServicePrincipalCredentials
	# in environment variables
	# if they are not existing, then we ask for username and password
	#if os.getenv("AZURE_CLIENT_ID"):
	#	credentials = ServicePrincipalCredentials(
	#		client_id=os.environ['AZURE_CLIENT_ID'],
	#		secret=os.environ['AZURE_CLIENT_SECRET'],
	#		tenant=os.environ['AZURE_TENANT_ID'],
	#		cloud_environment=cloud_environment
	#	)
	#else:
	#	credentials = UserPassCredentials(
	#		username=os.environ.get('AZURE_USER', input('Username: ')),
	#		password=os.environ.get('AZURE_PASSWORD', getpass.getpass('Password: ')),
	#		tenant=os.environ.get('AZURE_TENANT_ID', input('Tenant (AD Identifier): ')),
	#		cloud_environment=cloud_environment
	#	)

	# Define subscription client
	#subscription_client = SubscriptionClient(
	#	credentials,
	#	base_url=cloud_environment.endpoints.resource_manager
	#)


# FUNCTION: Check VMs
def checkVMStartup(vm):
	if vm.tags is not None and len(vm.tags)>0:
		print('\t\t\t {0}'.format(vm.tags))
	else:
		print('\t\t\t No tags defined to this VM')

# FUNCTION: Get VMs by subscription id
def getVMs(subscription, compute_client):
	try:
		# List VMs in subscription
		print('\tVMs:')
		for vm in compute_client.virtual_machines.list_all():
			print("\t\tVM: {0} - {1}".format(vm.name,vm.hardware_profile.vm_size))
			checkVMStartup(vm)
	except Exception as e:
		print(e)
		raise
	finally:
		print ('\tdone for {0}'.format(subscription))

# FUNCTION: List VM by subscription list
def listVMs(subscription_list):
	# Manage login to Azure
	# manageLogin()

	# subscription_list = subscription_client.subscriptions.list()
	for subsc in subscription_list:
		print("---> Subscription: '{0}' - {1}".format(subsc.display_name, subsc.subscription_id))
		getVMs(subsc.subscription_id)

# FUNCTION: Check whether a subscription id is in the current subscription list.
def checkSubscription(requiredID, subscription_list):
	subscription_list = subscription_client.subscriptions.list()
	for subsc in subscription_list:
		if requiredID == subsc.subscription_id:
			print("{} exists in subscription list".format(subsc.subscription_id))
			return True
	return False

# FUNCTION: Get the available metrics of this specific resource
def listAvailableMetrics(monitoringClient, resource_id, start_time, end_time):
	#resource_id = "/subscriptions/{0}/resourceGroups/{1}/providers/Microsoft.Compute/virtualMachines/{2}".format(monitoringClient.config.subscription_id, resourcegroup_name, object_name)
	result = False
	try:
		for metric in monitoringClient.metric_definitions.list(resource_id): 
			# azure.monitor.models.MetricDefinition
			print("Definition ----- {}: id={}, unit={}".format(metric.name.localized_value,metric.name.value,metric.unit))
			getMerticDataforInterval(monitoringClient, resource_id, metric.name.value, start_time, end_time, 'PT1H', 'Maximum')
		result = True

	except:
		print("Metric not found")
		result = False
	finally: 
		print("_________________________________")
		return result
	

# FUNCTION: Get required metric related data for the specified interval
def getMerticDataforInterval(monitoringClient, resource_id, metric_name, start_time, end_time, time_interval, aggregation_type):
	# time_interval: 
	#   PT1M - minutes 
	#   PT1H - hourly
	# aggergation_type: 
	#   Total   
	#   Maximum 
	#   Minimum 
	#   Average
	try:
		from azure.mgmt.monitor.models import RuleMetricDataSource;
		metrics_data = monitoringClient.metrics.list(resource_id, timespan="{}/{}".format(start_time, end_time), interval='{0}'.format(time_interval), metric='{0}'.format(metric_name), aggregation='{0}'.format(aggregation_type));
		for values in metrics_data.value:
			# azure.mgmt.monitor.models.Metric
			print("METRIC ---------- {} ({})".format(values.name.localized_value, values.unit.name))
			for timeserie in values.timeseries:
				for data in timeserie.data:
					# azure.mgmt.monitor.models.MetricData
					print("VALUE -------------------- {0}: {1}".format(data.time_stamp, data.total))
		return True
	except Exception as e:
		print(e)
		return False



##################################
##### Clients for Classes ########
# FUNCTION: Create Monitoring client
def newMonitoringClient(subscription_id):
	# Load Monitoring client from Azure
	try:
		from azure.mgmt.monitor import MonitorManagementClient;
		client = MonitorManagementClient(credentials,str(subscription_id), base_url=cloud_environment.endpoints.resource_manager)
		return client
	except:
		return False

# FUNCTION: Create Compute client
def newComputeClient(subscription_id):
	# Load Compute client from Azure
	try:
		from azure.mgmt.compute import ComputeManagementClient;
		compute_client = ComputeManagementClient(credentials, str(subscription_id), base_url=cloud_environment.endpoints.resource_manager);
		return compute_client
	except:
		return False

# FUNCTION: Create Resource Manager client
def newResourceManagerClient(subscription_id):
	# Load Compute client from Azure
	try:
		from azure.mgmt.resource import ResourceManagementClient;
		resourcemanager_client = ResourceManagementClient(credentials, str(subscription_id), base_url=cloud_environment.endpoints.resource_manager);
		return resourcemanager_client
	except:
		return False

# FUNCTION: Create RecoveryServicesClient client
def newRecoveryServicesClient(subscription_id):
	# Load Compute client from Azure
	try:
		from azure.mgmt.recoveryservices import RecoveryServicesClient;
		resourcemanager_client = RecoveryServicesClient(credentials, str(subscription_id), base_url=cloud_environment.endpoints.resource_manager);
		return resourcemanager_client
	except:
		return False
##### End of Clients for Classes ########
#########################################
#########################################################################
#########################################################################
### This part will be executed every time when the file is included #####
# List of CLOUDS
choices=['AZURE_GERMAN_CLOUD', 'AZURE_PUBLIC_CLOUD', 'AZURE_CHINA_CLOUD', 'AZURE_US_GOV_CLOUD']


global cloudName
cloudName = choices[cloud_list(choices)]
print("%s has been choosen by you" %(cloudName))

# Import Azure packages
## MSREST for different clouds
if cloudName == "AZURE_GERMAN_CLOUD":
	try:
		from msrestazure.azure_cloud import AZURE_GERMAN_CLOUD as cloud_environment
	except:
		pip.main(['install', '--user', 'msrestazure'])
		from msrestazure.azure_cloud import AZURE_GERMAN_CLOUD as cloud_environment
elif cloudName == "AZURE_PUBLIC_CLOUD":
	try:
		from msrestazure.azure_cloud import AZURE_PUBLIC_CLOUD as cloud_environment
	except:
		pip.main(['install', '--user', 'msrestazure'])
		from msrestazure.azure_cloud import AZURE_PUBLIC_CLOUD as cloud_environment
elif cloudName == "AZURE_CHINA_CLOUD":
	try:
		from msrestazure.azure_cloud import AZURE_CHINA_CLOUD as cloud_environment
	except:
		pip.main(['install', '--user', 'msrestazure'])
		from msrestazure.azure_cloud import AZURE_CHINA_CLOUD as cloud_environment
elif cloudName == "AZURE_US_GOV_CLOUD":
	try:
		from msrestazure.azure_cloud import AZURE_US_GOV_CLOUD as cloud_environment
	except:
		pip.main(['install', '--user', 'msrestazure'])
		from msrestazure.azure_cloud import AZURE_US_GOV_CLOUD as cloud_environment
else:
	try:
		from msrestazure.azure_cloud import AZURE_GERMAN_CLOUD as cloud_environment
	except:
		pip.main(['install', '--user', 'msrestazure'])
		from msrestazure.azure_cloud import AZURE_GERMAN_CLOUD as cloud_environment
## MS REST Credentials
from msrestazure.azure_active_directory import UserPassCredentials
from msrestazure.azure_active_directory import ServicePrincipalCredentials
try:
	# Try to load SubscriptionClient
	from azure.mgmt.resource.subscriptions import SubscriptionClient
except:
	# Install SubscriptionClient
	pip.main(['install', '--user', 'azure'])
	from azure.mgmt.resource.subscriptions import SubscriptionClient

## Load Clients
### Resource client
#from azure.mgmt.resource import ResourceManagementClient
### Computer client
#from azure.mgmt.compute import ComputeManagementClient


################# Manage login to Azure
global credentials
# Prefered way for Azure connection is the use of ServicePrincipalCredentials
# in environment variables
# if they are not existing, then we ask for username and password
if os.getenv("AZURE_CLIENT_ID"):
	credentials = ServicePrincipalCredentials(
		client_id=os.environ['AZURE_CLIENT_ID'],
		secret=os.environ['AZURE_CLIENT_SECRET'],
		tenant=os.environ['AZURE_TENANT_ID'],
		cloud_environment=cloud_environment
	)
else:
	credentials = UserPassCredentials(
		username=os.environ.get('AZURE_USER', input('Username: ')),
		password=os.environ.get('AZURE_PASSWORD', getpass.getpass('Password: ')),
		tenant=os.environ.get('AZURE_TENANT_ID', input('Tenant (AD Identifier): ')),
		cloud_environment=cloud_environment
	)

# Get subscription list
global subscription_client 
# subscription_client = ""
# Define subscription client
subscription_client = SubscriptionClient(
	credentials,
	base_url=cloud_environment.endpoints.resource_manager
	)
subscription_list = subscription_client.subscriptions.list()

#########################################################################