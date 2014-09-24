# -*- coding: utf-8 -*-
###########################################################################
# Displays a cute message                                                 #
# 									  #
# Author: Hexane                                                          #
###########################################################################


def help():
        return "!flip: flip some fuckin' tables"

def do():
	qtmessage = u"(╯°□°）╯︵ ┻━┻)"
	return qtmessage.encode("UTF-8")

def getCmd():
	return "!flip"

def getArgs():
	return 0

def hasEncodings():
        return True

