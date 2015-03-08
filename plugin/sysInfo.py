###########################################################################
# Prints System Info							  #
# Author: Hexane		                                          #
###########################################################################
import subprocess
import os
import math
import psutil

def help():
        return "!sysinfo: Returns system info"

def do():
	systring = subprocess.check_output('uname', shell=True)
	kernstring = subprocess.check_output('uname -r', shell=True) 
	cpustring = subprocess.check_output("sysctl hw.model | cut -d ':' -f2", shell=True)
	
	return "System: " + systring  + "Kernel: " + kernstring + "CPU:" + cpustring + "CPU Utilisation: {0} \nDisk Usage: {1}".format(get_cputil(), get_freespace())

def get_cputil():
	return str(psutil.cpu_percent()) + "%"


def get_freespace():#	
	dir = "/"
	s = os.statvfs(dir)
	#return megabytes
	space = ((s.f_bavail * s.f_frsize)*2**-20)
	total = ((s.f_blocks * s.f_frsize)*2**-20)

	percentage = ((space/total)*100)	
	output = round(percentage,2)
	return str(int(space)) + "MB/" + str(int(total)) + "MB  (Usage: " + str(output) + "%)"


def getCmd():
        return ["!sysinfo"]

def getArgs():
        return 0

def hasEncodings():
	return True
