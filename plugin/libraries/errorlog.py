#Telebot logging tool. 
#To be used by bot.py or plugins, logs to same location.

import os.path
import datetime

logdir = "plugin/etc/log/"

def logError(error, filename):
	dt = datetime.datetime.now()
	date = str(dt.day)+"/"+str(dt.month)+"/"+str(dt.year)
	
	print "Error: "+error	

	if not os.path.isfile(logdir+filename):
		print "log file does not exist, creating new file"
		file = open(logdir+filename, "w+")
		file.close()
	
	with open(logdir+filename, "a") as file:
		print "Writing to log file.."
		print os.path.abspath(file.name)
		file.write("\n\n"+date+": "+str(error));
	
	print "Written to log file "+filename+"...."
