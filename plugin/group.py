# -*- coding: utf-8 -*-
###########################################################################
# Contains group commands                                                 #
# Author: Firaenix                                                        #
###########################################################################

import urllib2
import os
import sdk.group
import sdk.media

etcDir = "plugin/etc/downloads/"

def help():
        return "!group [cmd][args]: cmds:rename, setPic, args:newName,picURL"

def do(message, optionsList):
	print message
	cmd = message.split(' ')[0]
	args = " ".join(message.split(' ')[1:])

	print cmd
	print args
	if cmd == 'rename':
		return rename(args, optionsList)
	if cmd.lower() == 'set_pic' or cmd.lower() == 'setpic':
		return set_pic(args, optionsList)
	#optionsList[0] = tgin, optionsList[1] = group, optionsList[2] = peer/user
	return """Please specify a group command:
		!group rename [name]
		!group set_pic [url]
	       """

def rename(name, optionsList):
	print name
	print optionsList[1]
	sdk.group.rename(optionsList[1], name, optionsList[0])
        return "Renamed Group."

def set_pic(urlLink, optionsList):
	#Get the file name+extension
	saveDir = etcDir+urlLink.split('/')[-1]
	#Save image to disk
        imgData = urllib2.urlopen(urlLink).read()
        output = open(saveDir, 'wb+')
        if not output.closed:
                output.write(imgData)
                output.close()

	sdk.group.set_pic(optionsList[1], saveDir, optionsList[0])
	#os.remove(saveDir)
        return "Group picture changed."

def getCmd():
        return ["!group"]

def getArgs():
        return 2

def hasEncodings():
        return True

