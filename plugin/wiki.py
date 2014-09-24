###########################################################################
# Wikipedia plugin for HexBot                                             #
#                                                                         #
# Author: Firaenix                                                        #
###########################################################################

import wikipedia

def help():
        return "!wiki [term]: Searches wikipedia for the given term"


def do(term):
	wikiPage = wikipedia.page(term)        
	
	summary = wikipedia.summary(term, sentences=5)
	
	if "\""+term+"\""+" redirects here." in summary:
		summary = wikiPage.summary

	response = wikiPage.url + "\n\n" + summary

        return response

def getCmd():
        return "!wiki"

def getArgs():
        return 1

def hasEncodings():
        return True

