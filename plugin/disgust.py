# -*- coding: utf-8 -*-
###########################################################################
# Absolutely Disgusting                                                   #
# Author: Firaenix                                                        #
###########################################################################

import urllib2
import os
import sdk.group
from random import randint

etcDir = "plugin/etc/downloads/"

def help():
        return "disgusting: displays disgust"

def do(message, optionsList):
        return disgusting(optionsList);

def disgusting(optionsList):
	urlLinks = ["http://i1.kym-cdn.com/entries/icons/original/000/014/350/137593505136.jpg",
		    "http://i0.kym-cdn.com/photos/images/newsfeed/000/710/681/371.jpg",
		    "http://i1.kym-cdn.com/photos/images/original/000/676/738/7bf.jpg",
		    "http://i1.kym-cdn.com/photos/images/original/000/649/615/5cf.jpg"]
	
	urlLink = urlLinks[randint(0, len(urlLinks)-1)]
	
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
#        return "Absolutely disgusting."

def getCmd():
        return ["disgubbin","disgusting"]

def getArgs():
        return 2

def hasEncodings():
        return False
