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
		message = message + getDate(rd.years, "year") + ", "
	if rd.months > 0:
		message = message + getDate(rd.months, "month") + ", "
	if rd.days >= 7:
		message = message + getDate((rd.days / 7), "week") + ", "
	if rd.days > 0:
		message = message + getDate((rd.days % 7), "day") + ", "
	if rd.hours > 0:
		message = message + getDate(rd.hours, "hour") + ", "
	if rd.minutes > 0:
		message = message + getDate(rd.minutes, "minute") + ", "
	message = message + getDate(rd.seconds, "second")
	return message

def getDate(time, dateType):
	if time > 1 or time == 0:
		dateType = dateType + "s"

	return "{0} {1}".format(time, dateType)

def getCmd():
	return ["!uptime"]

def getArgs():
	return 0

def hasEncodings():
        return False

