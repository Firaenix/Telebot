###########################################################################
# This is the credits plugin for Telebot				  #
# Author: Firaenix                                                        #
###########################################################################

def help():
        return "!credits: Displays the credits for Telebot"

def do():
	credits = """Original Source Code: asdofindia \n
		     Authors of HexBot: Firaenix and Hexane \n
		     Beta testers: CH23, jstrcrws, Char_Kie \n"""
        return credits

def getCmd():
        return "!credits"

def getArgs():
        return 0

def hasEncodings():
	return False
