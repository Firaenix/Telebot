###########################################################################
# Queries Wolfram Alpha                                                   #
# Author: Firaenix                                                        #
###########################################################################
import tungsten

def help():
        return "!wolf [query]: New wolfram alpha query in testing"

def do(query):
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
        return "!wolf"

def getArgs():
        return 1

def hasEncodings():
        return True


