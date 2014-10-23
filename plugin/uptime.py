###########################################################################
# Uptime plugin for HexBot. Uses diffirential unixtime from bot.py to     #
# Determine how long the bot has been running                             #
# Author: Hexane                                                          #
###########################################################################
import time
import datetime
import dateutil.relativedelta
from math import floor

def help():
        return "!uptime : Returns how long the bot has been running."

def do():
	currentTime = float(time.time())
	f = open("/etc/unixfile","r")
	startTime = f.read()
	f.close()


	dt1 = datetime.datetime.fromtimestamp(int(startTime)) # 1973-11-29 22:33:09
	dt2 = datetime.datetime.fromtimestamp(int(currentTime)) # 1977-06-07 23:44:50
	rd = dateutil.relativedelta.relativedelta (dt2, dt1)

	print "%d years, %d months, %d days, %d hours, %d minutes and %d seconds" % (rd.years, rd.months, rd.days, rd.hours, rd.minutes, rd.seconds)

	#timeDiff = (float(currentTime) - float(startTime) ) / (60) #Seconds = Minute	
	#time_hours = float(timeDiff) 
	#time_minutes = float(time_hours) * 60
	#time_seconds = float(time_minutes) * 60
	#time_ms = float(time_seconds) * 60

	#hoursSec = floor(time_hours % 60)
	#minutesSec = floor(time_minutes % 60)
	#secondsSec = floor(time_seconds % 60)
	#msSec = floor(time_ms % 60)
	
	return "Uptime: " + "%d hours, %d minutes and %d seconds" % (rd.hours, rd.minutes, rd.seconds)

def getCmd():
	return "!uptime"

def getArgs():
	return 0

def hasEncodings():
        return False

