#################################################
# Bastard Google Command                        #
# Author: ???		                        #
#################################################
import urllib
import json as m_json

def do(terms): # google <search term>
    '''Returns the link and the description of the first result from a google
    search
    '''
    query=terms.encode("UTF-8")
    print "going to google %s" % query

    try:
    	query = urllib.urlencode ( { 'q' : query } )
    	response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
    	json = m_json.loads ( response )
    	results = json [ 'responseData' ] [ 'results' ]
   
    except UnicodeEncodeError:
	print "Some unicode error occurred"	 
    returnval=""

    for result in results:
        title = result['title'].strip()
        url = result['url']   # was URL in the original and that threw a name error exception
	
	title = title.replace("&#39;", "'")	
	title = title.replace("&quot", '"')
	title = title.replace("<b>", "")
	title = title.replace("</b>", "")
	title = title.replace("&amp", "&")

	url = url.replace("%3F", "?")
	url = url.replace("%3D", "=")
        
        returnval += title + ': ' +  url + '\n\n'

    if not returnval:
        print "no returned JSON"
        returnval = "No data returned, did you enter the correct search terms?"
    else:
        print "returning %s" %returnval.encode("UTF-8")
    
    return returnval
    
def help():
	return "!google [query]: Searches google for given search term"

def getCmd():
	return "!google"

def getArgs():
	return 1

def hasEncodings():
	return True
