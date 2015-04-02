# -*- coding: utf-8 -*-
###########################################################################
# Bing Search Plugin                                                      #
# Author: Hexane and Firaenix                                             #
###########################################################################
from libraries.pybingsearch import PyBingSearch
import time

def help():
        return "!search [terms]: search the interwebs"

def do(args):
	api = 'l3iLSqvL/7Yzn29rUsP7akKjyf9AZnTVlE8zAvnYp/k'
	bing = PyBingSearch(api)
	result_list, next_uri = bing.search(args, limit=5, format='json')

	returnText = ""

	for i in range(0,len(result_list)):
		title = "%s" % result_list[i].title
		desc = "%s" % result_list[i].description
                url = "%s" % result_list[i].url
		returnText += title + "\n"  + desc[:65].strip() + "...\n" + url + "\n\n"

	if len(returnText) == 0:
		return "No Results. \nWere you looking up "+args+" you filthy person?"
	
	return "%s" % returnText
	
def getCmd():
	return ["!search"]

def getArgs():
	return 1

def hasEncodings():
        return True
