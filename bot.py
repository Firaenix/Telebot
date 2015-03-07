#!/usr/bin/python
###################################################################
# HexBot - a heavily modified version of asdofindia's telegram bot#
#							          #
# Author: Firaenix, Hexane                                        #
###################################################################

from threading import Thread
import time
import sys
import traceback
import subprocess
import os
from multiprocessing.pool import ThreadPool

from sdk import msg
#from sdk import stacktrace
import pluginComponent

_pathtotg='../tg/bin/'    #include trailing slash. I don't know if '~' notation works
lastmessage=''
_proc=None
tgin=None
spacer = "_____________________"
globalGroup = ""
#Set # of max threads at once 'processes=###'
pool = ThreadPool(processes=100)
errorGroup = ""
errorPeer = "Error"
etcDir = "plugin/etc/"


pluginCmds = []
plugins = []
helpString = 'All possible commands:'


#this function checks for spam by comparing current message to last message
def mymessage(message):
	global lastmessage

	if (message == lastmessage):
		return True
	else:
		return False

def AI(group,peer,message):
	
	#if using caps, plugin still called.
	messagelist = message.split(" ");
	if "!" in messagelist[0]:
		messagelist[0] = messagelist[0].lower()

	message = " ".join(messagelist)	

	try:
		if mymessage(message):
			return
		replyrequired=False
		reply=None
		if group is None:
			replyrequired=True
		
		#global proc
		#proc.stdin.flush()
		tgin = _proc.stdin
		reply= pluginComponent.callmodule(message, [tgin, group, peer])

		if reply is not None:
			tgin = _proc.stdin
			submit_msg(group,peer,reply, tgin)
	except:			
		print "Error occurred..."
                err = traceback.print_exc()
		tgin = _proc.stdin
		submit_msg(group, peer, err, tgin)
			
def spam(message):
	if (message == lastmessage):
		return True
	else:
		return False

#Returns the message back to the group.
def submit_msg(group,peer,message, tgin):
	global lastmessage
#	console.log('tgin: '+tgin)
#	global tgin
#	global _proc
	tgin = _proc.stdin
	lastmessage = msg.send_msg(group, peer, message, tgin)

#Reading all input, reads colours of text to determine where message is sent from.
def bot():

	COLOR_RED="\033[0;31m"
	COLOR_REDB="\033[1;31m"
	COLOR_NORMAL="\033[0m"
	COLOR_GREEN="\033[32;1m"
	COLOR_GREY="\033[37;1m"
	COLOR_YELLOW="\033[33;1m"
	COLOR_BLUE="\033[34;1m"
	COLOR_MAGENTA="\033[35;1m"
	COLOR_CYAN="\033[36;1m"
	COLOR_LCYAN="\033[0;36m"
	COLOR_INVERSE="\033[7m"
	
	#global pathtotg
	global _proc
	global _tgin
	_proc = subprocess.Popen([_pathtotg+'telegram-cli','-k',_pathtotg+'../tg-server.pub'],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
	tgin = _proc.stdin
	lastmessage=None
	multiline=False
	
	for line in iter(_proc.stdout.readline,''):
		if multiline and line != None and message != None:
			message+=line
			message = message.decode("UTF-8")
			if line.endswith('[0m\n'):
				message=message.rstrip('[0m\n')
				multiline=False
		else:
			if ((COLOR_YELLOW+" is now online" in line) or (COLOR_YELLOW+" is now offline" in line) or (COLOR_YELLOW+": 0 unread" in line)):
				pass
			#Outputs all text chat
			#NECESSARY FOR PROCESSING COMMANDS, ETC.
			print line.rstrip()
		with open('output','a') as fil:
			fil.write(line)
			group=None
			peer=None
			message=None
				
			try:                     	
				#Checks the colour of the stdout line
				if ((COLOR_BLUE+" >>>" in line) and (COLOR_BLUE+"[" in line) and ("!" in line)):
					peer=line.split(COLOR_RED)[1].split(COLOR_NORMAL)[0]
					message=line.split(COLOR_BLUE+" >>> ")[1].split("\033")[0]
					if not line.endswith("[0m\n"):
						multiline=True
				if ((COLOR_GREEN+" >>>" in line) and ("!" in line)):
					group=line.split(COLOR_MAGENTA)[2].split(COLOR_NORMAL)[0]
					#For change colour level
					#peer=line.split(COLOR_REDB)[1].split(COLOR_RED)[0]

					peer=line.split(COLOR_RED)[1].split(COLOR_NORMAL)[0]
					message=line.split(COLOR_GREEN+" >>> ")[1].strip(COLOR_NORMAL).split("\033")[0]
					if not line.endswith("[0m\n"):
						multiline=True
				if ((COLOR_BLUE+" >>>" in line) and (COLOR_MAGENTA+"[" in line)):
					group=line.split(COLOR_MAGENTA)[2].split(COLOR_NORMAL)[0]
					globalGroup = group	
					
					#Splits the line to display the user name.
					#The username is displayed after the group name, separated my the letter 'm' Always,
					#Then strip the " [0" Which is displayed after the username.
					#rstrip() to remove final whitespace

					peer=line.split(group)[1].split('m')[2].strip('[0').rstrip()

					message=line.split(COLOR_BLUE+" >>> ")[1].strip(COLOR_NORMAL).split("\033")[0]
					if not line.endswith("[0m\n"):
						multiline=True
				if COLOR_GREY in line and "*** Lost connection to server..." in line:
					print "Detected connection to server loss, restarting bot..."
                                	#If the bot loses connection, restart the bot.
					subprocess.call('killall python2.7; killall telegram-cli; python bot.py')

			except IndexError:
				print "Error: Change colour levels"
		#Calls the AI function to read the input, from there, calls the plugins
		if( ((group is not None) or (peer is not None)) and (message is not None)):
			#adds the command to a new thread
			pool.apply_async(AI, (group, peer, message,))

#Cleans up the root dir on startup of all logs.
def cleanupFiles():
	#clean up downloads directory
	folder = etcDir+'downloads/'
	for the_file in os.listdir(folder):
	        file_path = os.path.join(folder, the_file)
		print file_path
        	try:
        		if os.path.isfile(file_path):
				print 'deleting'
		        	os.remove(file_path)
		except Exception, e:
        		print e

	try:
		os.remove('output')
	except OSError:
	        pass
	

def help():
	print helpString
	return helpString
	
def main():
	#cleans up the files on every run
	cleanupFiles()

	botthread = Thread(target = bot)
	botthread.start()

	#Writes current unix time to file
	unixtime = str(int(time.time()))
	f = open(etcDir+"unixfile","w")
	f.write(unixtime)
	f.close()
	
	#Pass in True as this is only called on First Run
	pluginComponent.getPlugins(True)

	botthread.join()

if __name__ == "__main__":
    main()

