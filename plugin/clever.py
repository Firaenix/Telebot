###########################################################################
# CleverBot Plugin							  #
# Hexane								  #
###########################################################################
import cleverbot

def help():
        return "!cb [message]: Returns response from cleverbot"

def do(msg):
	cb = cleverbot.Cleverbot()	
        return cb.ask(msg)

def getCmd():
        return ["!cb"]

def getArgs():
        return 1

def hasEncodings():
	return True
