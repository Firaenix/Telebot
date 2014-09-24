###########################################################################
# This is a module for HexBot. Must have a description in a help() method #
#									  #
# Author: Firaenix							  #
###########################################################################
import time


def help():
	return "!time : Returns the current Server System Date/Time"


def do():
   	return "Current Server Date: "+time.strftime("%A %d, %B %Y")+"\n"+"Current Server Time: " + time.strftime("%H:%M:%S")

def getCmd():
	return "!time"

def getArgs():
	return 0

def hasEncodings():
        return False

