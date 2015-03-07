import json, re, requests, urllib


def do(terms):
  if(terms == ""):
	return "Please enter some search terms"
  args = terms.split("@")
	
  #When the arguments array only has one element
  if len(args) is 1:
        terms = args[0]
        index = 1
  else: # When the array has more than one element (0 elements should not get here)
        terms = args[0]
	try:
		index = long(args[1])	
	except ValueError:
		return "Improper value"

  data = doreq(terms)
  total = len(data['list'])
  defn = define(terms, data, index)
  example = define(terms, data, index, 'example')
  if index <10:
	return '{0} e.g.: {1} [{2}/{3}]'.format(defn, example, index, total)
  else:
	return 'index btfo'	

def doreq(terms):
  api = 'http://api.urbandictionary.com/v0/define?term='
  response = requests.get(api + terms)
  if response.status_code != 200:
      raise Exception('Error status code returned: ' + str(response.status_code))
  response_json = json.loads(response.content)
  if not response_json:
      raise Exception('Response falsy for given term: ' + term)
  return response_json

def define(terms, data, index=1, action='definition'):
  try:
	return data['list'][index-1][action]
  except IndexError:
	return "cunt, fuck off."
	sys.exit(0)
    
def help():
  return "!ud string: returns urban dictionary definition of a word"

def getCmd():
  return ["!ud"]

def getArgs():
  return 1

def hasEncodings():
  return False
