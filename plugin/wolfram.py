#################################################
# Wolfram|Alpha Plugin				#
# Queries Wolfram|Alpha for supplied text	#
#################################################

import xml.etree.ElementTree as ET
import plugin.google
import requests

spacer = "_____________________"

def do(query):
	appid='49RXE9-H5QE4L98V5'
	results = requests.get("http://api.wolframalpha.com/v2/query", params={'input':query,'appid': appid}, headers={'User-Agent': "Mozilla"})
	results = results.text
	results = results
	root=ET.fromstring(results)
	reply=None
	print "querying wolfram for "+query
	for pod in root.findall('pod'):
		if (pod.attrib['id']=="Result"):
			reply=pod[0][0].text
			print reply
	if not reply:
		reply="NO_RESPONSE"
	if reply == "NO_RESPONSE":
		reply = "Wolfram|Alpha did not have an answer, defaulting to Google.\n"+spacer+"\n"+plugin.google.do(query)
	return reply


def help():
	return "!wolf [query]: Will search Wolfram|Alpha for a solution to a query"

def getCmd():
	return "!wolf"

def getArgs():
	return 1

def hasEncodings():
        return True
