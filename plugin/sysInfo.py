###########################################################################
# Prints System Info							  #
# Author: Hexane		                                          #
###########################################################################
import subprocess

def help():
        return "!sysinfo: Returns system info"

def do():
        cpustring = subprocess.check_output("cat /proc/cpuinfo | grep 'model name' | tail -n 1 | cut -d: -f2 | cut -c 2-', shell=True")
	kernstring = subprocess.check_output('uname -r', shell=True) 
	return "CPU: " + cpustring + "\n"
	return "Kernel: " + kernstring

def getCmd():
        return "!sysinfo"

def getArgs():
        return 0

def hasEncodings():
	return True
