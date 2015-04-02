# -*- coding: utf-8 -*-
###########################################################################
# Bing Search Plugin                                                      #
# Author: Hexane and Firaenix                                             #
###########################################################################
from libraries.pybingsearch import PyBingSearch
import time
import re

def help():
        return ( "!search [terms] #[limit]: search the interwebs (default limit: 3)")

def do(query):
	apiKey = 'l3iLSqvL/7Yzn29rUsP7akKjyf9AZnTVlE8zAvnYp/k'
	bing = PyBingSearch(apiKey)
	resultLimit = 3

	# "#\d+$" = Match # followed by 1 or more numbers, no characters
	if len(re.findall(r"#\d+$", query)) > 0:
		resultLimit = re.search(r"#\d+$", query).group(0).replace("#", "")
		query = re.split(r"#\d+$", query)[0]

	result_list, next_uri = bing.search(query, limit=resultLimit, format='json')

	returnText = ""
	for i in range(0,len(result_list)):
		title = "%s" % result_list[i].title
		desc = "%s" % result_list[i].description
                url = "%s" % result_list[i].url
		returnText += title + "\n"  + desc + "\n" + url + "\n\n"

	if len(returnText) == 0:
		return "No Results. \nWere you looking up " + query + " you filthy person?"
	
	return "%s" % returnText

def getCmd():
	return ["!search"]

def getArgs():
	return 1

def hasEncodings():
    return True
