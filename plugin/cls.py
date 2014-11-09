# -*- coding: utf-8 -*-
###########################################################################
# Simulates the clearing of the chat screen                               #
# Author: Hexane                                                          #
###########################################################################

def help():
        return "!cls : Clear the chat screen"

def do():
	#A Whole bunch of new line characters between invisible unicode characters
        message = u"\u200B\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\u200B"
        return message

def getCmd():
        return "!cls"

def getArgs():
        return 0

def hasEncodings():
        return True

