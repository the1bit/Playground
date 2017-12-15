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


# Cloud Environment list
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
def ManageLogin():
	global credentials
	global subscription_client 
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

	# Define subscription client
	subscription_client = SubscriptionClient(
		credentials,
		base_url=cloud_environment.endpoints.resource_manager
	)


# Check VMs
def checkVMStartup(vm):
	if vm.tags is not None and len(vm.tags)>0:
		print('\t\t\t {0}'.format(vm.tags))
	else:
		print('\t\t\t No tags defined to this VM')

# Get VMs
def getVMs(subscription):
	print(subscription)
	compute_client = ComputeManagementClient(
		credentials,
		str(subscription),
		base_url=cloud_environment.endpoints.resource_manager
	)

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


def listVMs(cloud):
	# Manage login to Azure
	ManageLogin()

	subscription_list = subscription_client.subscriptions.list()
	for subsc in subscription_list:
		print("---> Subscription: '{0}' - {1}".format(subsc.display_name, subsc.subscription_id))
		getVMs(subsc.subscription_id)


#########################################################################
### This part will be executed every time when the file is included #####
# List of CLOUDS
choices=['AZURE_GERMAN_CLOUD', 'AZURE_PUBLIC_CLOUD', 'AZURE_CHINA_CLOUD', 'AZURE_US_GOV_CLOUD']


global cloud
cloud = choices[cloud_list(choices)]
print("%s has been choosen by you" %(cloud))

# Import Azure packages
if cloud == "AZURE_GERMAN_CLOUD":
	try:
		from msrestazure.azure_cloud import AZURE_GERMAN_CLOUD  as cloud_environment
	except:
		pip.main(['install', '--user', 'msrestazure'])
		from msrestazure.azure_cloud import AZURE_GERMAN_CLOUD as cloud_environment
elif cloud == "AZURE_PUBLIC_CLOUD":
	try:
		from msrestazure.azure_cloud import AZURE_PUBLIC_CLOUD  as cloud_environment
	except:
		pip.main(['install', '--user', 'msrestazure'])
		from msrestazure.azure_cloud import AZURE_PUBLIC_CLOUD as cloud_environment
elif cloud == "AZURE_CHINA_CLOUD":
	try:
		from msrestazure.azure_cloud import AZURE_CHINA_CLOUD  as cloud_environment
	except:
		pip.main(['install', '--user', 'msrestazure'])
		from msrestazure.azure_cloud import AZURE_CHINA_CLOUD as cloud_environment
elif cloud == "AZURE_US_GOV_CLOUD":
	try:
		from msrestazure.azure_cloud import AZURE_US_GOV_CLOUD  as cloud_environment
	except:
		pip.main(['install', '--user', 'msrestazure'])
		from msrestazure.azure_cloud import AZURE_US_GOV_CLOUD as cloud_environment
else:
	try:
		from msrestazure.azure_cloud import AZURE_GERMAN_CLOUD  as cloud_environment
	except:
		pip.main(['install', '--user', 'msrestazure'])
		from msrestazure.azure_cloud import AZURE_GERMAN_CLOUD as cloud_environment

from msrestazure.azure_active_directory import UserPassCredentials
from msrestazure.azure_active_directory import ServicePrincipalCredentials
try:
	from azure.mgmt.resource.subscriptions import SubscriptionClient
except:
	pip.main(['install', '--user', 'azure'])
	from azure.mgmt.resource.subscriptions import SubscriptionClient

from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient

#########################################################################