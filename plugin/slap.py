###########################################################################
# Simple port of the IRC trout slap command                               #
# Author: Firaenix                                                        #
###########################################################################

def help():
        return "!slap [user] : Slaps the user with a large trout"

def do(username, optionsList):
	user = optionsList[2]
        message = u"*"+user+" slaps "+username+" around a bit with a large trout*"
        return message.encode("UTF-8")

def getCmd():
        return ["!slap"]

def getArgs():
        return 2

def hasEncodings():
	return True
