# -*- coding: utf-8 -*-
#################################################
# Urban Dictionary Plugin			#
# Author Hexane 				#
#################################################
import urbandict

def do(terms): 
	results = urbandict.define(terms)
	word = results[0]["word"]
	definition = results[0]["def"]
	example = results[0]["example"]
	return word.title() + definition + example
    
def help():
	return "!ud string: returns urban dictionary definition of a word"

def getCmd():
	return "!ud"

def getArgs():
	return 1

def hasEncodings():
        return True

