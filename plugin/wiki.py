# -*- coding: utf-8 -*-
###########################################################################
# Wikipedia plugin for TeleBot                                            #
# Author: Firaenix                                                        #
###########################################################################
import wikipedia

def help():
        return "!wiki [term]: Searches wikipedia for the given term"


def do(term):
	try:
		wikiPage = wikipedia.page(term)        	
	except wikipedia.exceptions.DisambiguationError as e:
		disList = '\n'.join(e.options)
		return 'Found more than one page matching "'+term+'".\nDid you mean:\n\n'+disList
	
	summary = wikipedia.summary(term, sentences=5)

	if "\""+term+"\""+" redirects here." in summary:
		summary = ''
		wikiSummary = wikiPage.summary
		summaryList = wikiSummary.split(". ") #split on .+space to ensure not just an acronym like U.S.A
		for i in range(0, 4):
			summary = summary+summaryList[i]	

	response = wikiPage.url + "\n\n" + summary

        return response

def getCmd():
        return ["!wiki"]

def getArgs():
        return 1

def hasEncodings():
        return True

