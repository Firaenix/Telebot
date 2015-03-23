###########################################################################
# Prints System Info							  #
# Author: Hexane		                                          #
###########################################################################
import subprocess
import os
import math
import time
import platform
import psutil

def help():
        return "!sysinfo: Returns system info"

def do():
	cpustring = subprocess.check_output("sysctl hw.model | cut -d ':' -f2", shell=True)
	
	return "System: " + platform.platform() + "\nCPU:" + cpustring + "CPU Utilisation: {0} \n\nDisk Usage: {1}".format(get_cputil(), get_freespace()) + memory_usage() + "\n\n" + get_server_time() 

def get_cputil():
	return str(psutil.cpu_percent()) + "%"

def memory_usage():
	used = str(int((psutil.virtual_memory().used)*2**-20))
	total = str(int((psutil.virtual_memory().total)*2**-20))
	percentage = str(int(psutil.virtual_memory().percent))
        return "\nMemory Usage: " + used  + "MB / " + total + "MB (" + percentage + "%)"

def get_freespace():	
	dir = "/"
	s = os.statvfs(dir)
	#return megabytes
	space = ((s.f_bavail * s.f_frsize)*2**-20)
	total = ((s.f_blocks * s.f_frsize)*2**-20)

	percentage = ((space/total)*100)	
	output = round(percentage,2)
	return str(int(space)) + "MB/" + str(int(total)) + "MB  (Usage: " + str(output) + "%)"

def get_server_time():
	return "Current Server Date: "+time.strftime("%A %d, %B %Y")+"\n"+"Current Server Time: " + time.strftime("%H:%M:%S")

def getCmd():
        return ["!sysinfo"]

def getArgs():
        return 0

def hasEncodings():
	return True
