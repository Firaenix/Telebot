# -*- coding: utf-8 -*-
###########################################################################
# Adds some much needed desu to the chat                                  #
#                                                                         #
# Author: Firaenix                                                        #
###########################################################################
import time
from random import randrange


def help():
        return "!desu : Adds some much needed desu to the chat"


def do():
	desuList = ["Desu~", "DESU DESU DESU DESU DESU DESU", "NEEDS MORE DESU\nDESU DESU DESU DESU DESU DESU DESU DESU DESU", "Ask desu?\nGet desu.", "Moshi Moshi\ndesu desu desu desu~"]
        randomInt = randrange(5);
	
	return desuList[randomInt]

def getCmd():
        return "!desu"

def getArgs():
        return 0

def hasEncodings():
        return True

