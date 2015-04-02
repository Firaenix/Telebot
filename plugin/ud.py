##########################################
# Urban Dictionary plugin                #
#                                        #
# Author: Hexane                         # 
##########################################
import json, re, requests, urllib

def do(terms):
	if(terms == ""):
		return "Please enter some search terms"
	index = 1	

	if len(re.findall(r"#\d+$", terms)) > 0:
		index = int(re.search(r"#\d+$", terms).group(0).replace("#", ""))
		terms = re.split(r"#\d+$", terms)[0]

	data = request(terms)
	total = len(data['list'])
	defn = get_definition(terms, data, index)
	example = get_definition(terms, data, index, 'example')

	if index < 10:
		return '{0} e.g.: {1} [{2}/{3}]'.format(defn, example, index, total)
	else:
		return 'Index out of bounds.'	

def request(terms):
	api = 'http://api.urbandictionary.com/v0/define?term='
	response = requests.get(api + terms)

	if response.status_code != 200:
        	raise Exception('Error status code returned: ' + str(response.status_code))
	
	response_json = json.loads(response.content)
	
	if not response_json:
      		raise Exception('Response falsy for given term: ' + term)
	
	return response_json

def get_definition(terms, data, index, action='definition'):
	try:
		return data['list'][index][action]
	except IndexError:
		return "Fuck off, Cunt"
    
def help():
	return "!ud string: returns urban dictionary definition of a word"

def getCmd():
	return ["!ud"]

def getArgs():
	return 1

def hasEncodings():
	return False
