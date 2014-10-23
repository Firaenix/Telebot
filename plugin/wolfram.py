# -*- coding: utf-8 -*-
###########################################################################
# Queries Wolfram Alpha                                                   #
#                                                                         #
# Author: Firaenix                                                        #
###########################################################################

import tungsten

def help():
        return "!wolf : New wolfram alpha query in testing"

def do(query):
	client = tungsten.Tungsten('49RXE9-H5QE4L98V5')
	result_obj = client.query(query)
	#print result_obj
	#print result_obj.results
	message = ""
	for pod in result_obj.pods:
		print pod.scanner
		message = message+"\n"+str(pod.format['plaintext'])
		
	
	#Fixes multiplication sign
	message = message.replace('[', '').replace("'", '').replace(']', '').replace(r'\xd7',' x ')
	return message

def getCmd():
        return "!wolf"

def getArgs():
        return 1

def hasEncodings():
        return True


