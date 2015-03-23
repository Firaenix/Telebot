###########################################################################
# Uptime plugin for HexBot. Uses diffirential unixtime from bot.py to     #
# Determine how long the bot has been running                             #
# Author: Hexane & Firaenix                                               #
###########################################################################
import time
import datetime
import dateutil.relativedelta
from math import floor

etcDir = "plugin/etc/"

def help():
        return "!uptime : Returns how long the bot has been running."

def do():
	currentTime = float(time.time())
	f = open(etcDir+"unixfile","r")
	startTime = f.read()
	f.close()

	dt1 = datetime.datetime.fromtimestamp(int(startTime)) # 1973-11-29 22:33:09
	dt2 = datetime.datetime.fromtimestamp(int(currentTime)) # 1977-06-07 23:44:50
	rd = dateutil.relativedelta.relativedelta (dt2, dt1)

	message = "Uptime: "

	if rd.years > 0:
		message = message + "%d years, " % rd.years
	if rd.months > 0:
		message = message + "%d months, " % rd.months
	if rd.days > 0:
		message = message + "%d days, " % rd.days
	if rd.hours > 0:
		message = message + "%d hours, " % rd.hours
	if rd.minutes > 0:
		message = message + "%d minutes, " % rd.minutes
	message = message + "%d seconds" % rd.seconds
	return message

def getCmd():
	return ["!uptime"]

def getArgs():
	return 0

def hasEncodings():
        return False

