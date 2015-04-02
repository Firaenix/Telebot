# -*- coding: utf-8 -*-
###########################################################################
# Bing Search Plugin                                                      #
# Author: Hexane and Firaenix                                             #
###########################################################################
from libraries.pybingsearch import PyBingSearch
import time
import re

def help():
        return ( "!search \"[terms]\" [limit]  \n "
        		 "search the interwebs and return a specified number of results (3 by default)")

def do(args):
	apiKey = 'l3iLSqvL/7Yzn29rUsP7akKjyf9AZnTVlE8zAvnYp/k'
	bing = PyBingSearch(apiKey)

	errorString = "Syntax Error. See !help."

	argString = args

	termMatch = re.search('\"(.+)\"', argString)
	if termMatch:
		result = termMatch.group()
		query = result[1:-1]
		print('query is: ' + query)
	else:
		return errorString

	# better way to remove substring from a string?
	argString = argString.replace(result, '')

	limitMatch = re.search('\d+', argString)
	if limitMatch:
		limit = limitMatch.group()
		print('limit is: ' + limit)
	else:
		limit = 3

	result_list, next_uri = bing.search(query, limit=3, format='json')

	returnText = ""

	for i in range(0,len(result_list)):
		title = "%s" % result_list[i].title
		desc = "%s" % result_list[i].description
		url = "%s" % result_list[i].url
		returnText += title + "\n" + desc + "\n" + url + "\n\n"

	if len(returnText) == 0:
		return "No Results. \nWere you looking up "+args+" you filthy person?"
	
	return "%s" % returnText
	
def getCmd():
	return ["!search"]

def getArgs():
	return 1

def hasEncodings():
    return True