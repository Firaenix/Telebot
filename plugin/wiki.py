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
		summary = ''
		wikiSummary = wikiPage.summary
		summaryList = wikiSummary.split(". ") #split on .+space to ensure not just an acronym like U.S.A
		for i in range(0, 4):
			summary = summary+summaryList[i]	

	response = wikiPage.url + "\n\n" + summary

        return response

def getCmd():
        return "!wiki"

def getArgs():
        return 1

def hasEncodings():
        return True

