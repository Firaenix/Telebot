###########################################################################
# Queries an IP to get back details using a webservice                    #
# Author: Firaenix                                                        #
###########################################################################
import urllib2
import json

apicall = "http://ip-api.com/json/{0}"

def help():
        return "!ip [ip/host]: returns details on a given ip or host"

def do(msg):
	if not msg == "":		
	        response = urllib2.urlopen(apicall.format(msg)).read()		
		response = json.loads(response)
		
		output = ""
		for key, value in response.iteritems():
			output = output + str(key).capitalize() + ": " + str(value) + "\n"

		return output
	return "Please enter a valid IP or Hostname"

def getCmd():
        return ["!ip"]

def getArgs():
        return 1

def hasEncodings():
        return True


