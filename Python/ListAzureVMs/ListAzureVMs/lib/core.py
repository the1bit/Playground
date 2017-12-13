#!/usr/bin/python

#----------------------------------------------
# Author: Tibor Kiss
# Version: 1.0
# Release date: 11.12.2017
#----------------------------------------------
# collection of core functions for python.
#----------------------------------------------


# FUNCTION: Check OS
def checkOS():
	import platform
	result = platform.system()

	return result.lower()

# FUNCTION: Validate if an IP range is valid IPv4 range or not
def  ipRangeValidation(ipRange, requiredSubnet = "24"):
	# Split range
	ipAddress = ipRange.split('/')[0]
	subnet = ipRange.split('/')[1]

	# If required is * it accepts everything
	if requiredSubnet == "*":
		requiredSubnet = subnet

	# Validate IP
	if ipValidation(ipAddress):
		# Validate required subnet
		if int(subnet) == int(requiredSubnet):
			return True
		else:
			return False
	else:
		return False

# FUNCTION: Check connection via customized port
def checkConnection(ipAddress, port, logger, retry = 5):
	import socket
	import time
	
	result = False
	exceptionCount = 0
	successCount = 0
	# Validate retry value
	if int(retry) > 0 and int(retry) < 128:
		# Validate IP
		if ipValidation(ipAddress):
			# Start trying to connect
			tryings = 0
			while int(retry) > tryings and successCount == 0  :
				
				try:
					# Create socket
					s = socket.socket()
					# Set time out
					s.settimeout(10)
					# Show tryings
					logger.debug("Connection tryings to %s: %s", ipAddress, tryings)
					# Check connection
					res = s.connect((ipAddress, port)) 
					successCount += 1
				except Exception as e: 
					exceptionCount += 1 
				finally:
					# Close connection
					s.close()
					#  Wait some seconds
					time.sleep(3)
				# Increase tryings
				tryings += 1
			## End of While
			
			# Drop errormessage if exceprion has been occurred
			if exceptionCount == int(retry):
				logger.debug("Something's wrong with %s:%d. Exception is %s" % (ipAddress, port, e))
				result = False
			elif successCount > 0:
				# Result is OK if there were one or more success connection
				result = True
	return result

# FUNCTION:obfuscate pasword from parameter file
def hidePassword(filename, old_string, new_string):
	# Safely read the input filename using 'with'
	with open(filename) as f:
		s = f.read()
		if old_string not in s:
			return

	# Safely write the changed content, if found in the file
	with open(filename, 'w') as f:
		s = s.replace(old_string, new_string)
		f.write(s)

# FUNCTION: Check and Install missing packages
def managePackage(package):
	import pip
	try:
		pip.main(['install', '--user', '{0}'.format(package)])
		return True
	except Exception as e:
		print(e)
		raise
		quit('Installation error: {0}'.format(e))


#############################    END OF FILE ############################