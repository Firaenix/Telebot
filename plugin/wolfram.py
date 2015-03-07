# -*- coding: utf-8 -*-
###########################################################################
# Queries Wolfram Alpha                                                   #
# Author: Firaenix                                                        #
###########################################################################
import tungsten

def help():
        return "!wolf [query]: New wolfram alpha query in testing"

def do(query):
	#plugins with multiple cmds get passed the query+which command was called
	query = query[0]
	
	client = tungsten.Tungsten('49RXE9-H5QE4L98V5')
	result_obj = client.query(query)
	message = ""
	for pod in result_obj.pods:
		print pod.scanner
		message = message+"\n"+str(pod.format['plaintext'])
		
	#Formatting
	message = message.replace('[', '').replace("'", '').replace(']', '').replace(r'\xd7',' x ')
	return message

def getCmd():
        return ["!wolfram", "!wolf"]

def getArgs():
        return 1

def hasEncodings():
        return True


