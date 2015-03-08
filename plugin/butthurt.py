###########################################################################
# Returns a link to a butthurt gif                                        #
# Author: Firaenix                                                        #
###########################################################################
import time
import urllib2
import sdk.media
import os

etcDir = "plugin/etc/downloads/"
dlFile = "butthurt.gif"


def help():
        return "!butthurt: Returns a link to the butthurt gif"


def do(msg, optionsList):
	#Save image to disk
	if not os.path.isfile(etcDir+dlFile):
        	imgData = urllib2.urlopen("https://i.imgur.com/wKdzqtX.gif").read()
        	output = open(etcDir+dlFile, 'wb+')
        	output.write(imgData)
        	output.close()

	#optionsList[0] == tgin, [1] = group [2] = peer/user
        sdk.media.send_doc(optionsList[1], etcDir+dlFile, optionsList[0])

#        return "Butthurt!\nhttps://i.imgur.com/wKdzqtX.gif"

def getCmd():
        return ["!butthurt"]

def getArgs():
        return 2

def hasEncodings():
        return False

