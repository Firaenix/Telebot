###########################################################################
# Gets a random image from imgur and returns the link                     #
# Author: Firaenix                                                        #
###########################################################################
import random
import urllib2
import os
import sdk.media


imgGalurl = "http://imgur.com/gallery/"
imgUrl = "http://i.imgur.com/"

etcDir = "plugin/etc/downloads/"
dlFile = ".png"

def help():
        return "!imgur : Returns a random imgur link"

def getRandomLink(optionsList):
	valid = False

	randImgurId = ''
	while not valid:	
		#gets the thread link and the direct image link
		galLink = ''
		urlLink = imgUrl
		for i in range(0, 5): #messy, but gets the job done.
			choices = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
		
			galLink = galLink + choices
			urlLink = urlLink + choices
	
		randImgurId = galLink
		galLink = imgGalurl+galLink
		urlLink = urlLink+".jpg"
		checkedUrl = urllib2.urlopen(urlLink).geturl()

		if(urlLink == checkedUrl):
			valid = True

	#Save image to disk
	imgData = urllib2.urlopen(urlLink).read()
	output = open(etcDir+randImgurId+dlFile, 'wb+')
	if not output.closed:
		output.write(imgData)
		output.close()
		
	#Set image as profile photo and upload photo to group
	#optionsList[0] == tgin, [1] = group [2] = peer/user
	sdk.media.send_image(optionsList[1], etcDir+randImgurId+dlFile, optionsList[0])
	sdk.media.set_profile_pic(etcDir+randImgurId+dlFile, optionsList[0])

	#os.remove(etcDir+randImgurId+dlFile)
	return "Gallery: "+galLink+"\nImage: "+urlLink

def do(msg, optionsList):
	#msg is not used

	#query imgur, return link.

        return getRandomLink(optionsList)

def getCmd():
        return ["!imgur"]

def getArgs():
        return 2

def hasEncodings(): #Should only be links, no encodings, unless get title
        return False

