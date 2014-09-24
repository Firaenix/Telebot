# -*- coding: utf-8 -*-
###########################################################################
# Displays a cute message                                                 #
# 									  #
# Author: Hexane                                                          #
###########################################################################

import time
import os

def help():
        return "!pat : Send the bot some love"

def do():
	qtmessage = u"( ^▽^) thank yuu~~~~"
	return qtmessage.encode("UTF-8")

def getCmd():
	return "!pat"

def getArgs():
	return 0

def hasEncodings():
        return True

