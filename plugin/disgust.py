# -*- coding: utf-8 -*-
###########################################################################
# Absolutely Disgusting                                                   #
# Author: Firaenix                                                        #
###########################################################################

import urllib2
import os
import sdk.group

etcDir = "plugin/etc/downloads/"

def help():
        return "disgusting: displays disgust"

def do(message, optionsList):
        return disgusting(optionsList);

def disgusting(optionsList):
	urlLink = "http://i1.kym-cdn.com/entries/icons/original/000/014/350/137593505136.jpg"
        #Get the file name+extension
        saveDir = etcDir+urlLink.split('/')[-1]
        #Save image to disk
        imgData = urllib2.urlopen(urlLink).read()
        output = open(saveDir, 'wb+')
        if not output.closed:
                output.write(imgData)
                output.close()

        sdk.group.send_image(optionsList[1], saveDir, optionsList[0])
        #os.remove(saveDir)
        return "Absolutely disgusting."

def getCmd():
        return ["disgusting"]

def getArgs():
        return 2

def hasEncodings():
        return True
