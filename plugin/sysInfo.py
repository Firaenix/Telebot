###########################################################################
# Prints System Info							  #
# Author: Hexane		                                          #
###########################################################################
import subprocess

def help():
        return "!sysinfo: Returns system info"

def do():

	sh = subprocess.Popen(["/bin/uname -r"], shell=False, stdout=subprocess.PIPE)
	kernstring = sh.stdout.read()
        
	return "Kernel: " + kernstring

def getCmd():
        return "!sysinfo"

def getArgs():
        return 0

def hasEncodings():
	return True
