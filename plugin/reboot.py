###########################################################################
# Kills all bot related processes and restarts the bot from scratch       #
# Author: Firaenix                                                        #
###########################################################################
import sys
import os

def help():
        return "!reboot : Restarts the bot"

def do(message, optionsList):
	temp_dev_list = ["Nick Carton", "Steve Ball"]
	if any(dev in optionsList[2] for dev in temp_dev_list):
		restart_program()

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

def getCmd():
        return ["!reboot"]

def getArgs():
        return 2

def hasEncodings():
	return False

