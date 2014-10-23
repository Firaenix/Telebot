###########################################################################
# Gets a random image from imgur and returns the link                     #
# Author: Firaenix                                                        #
###########################################################################
import random
import urllib2

imgGalurl = "http://imgur.com/gallery/"
imgUrl = "http://i.imgur.com/"

def help():
        return "!imgur : Returns a random imgur link"

def getRandomLink():
	
	#gets the thread link and the direct image link
	galLink = imgGalurl
	urlLink = imgUrl
	for i in range(0, 5): #messy, but gets the job done.
		choices = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
		
		galLink = galLink + choices
		urlLink = urlLink + choices
	
	urlLink = urlLink+".jpg"
	checkedUrl = urllib2.urlopen(urlLink).geturl()

	if(urlLink == checkedUrl):
		return "Gallery: "+galLink+"\nImage: "+urlLink
	else:
		return getRandomLink() #recursively calls itself until gets to a valid imgur link

	return urlLink + ".jpg" #shouldnt ever hit

def do():
	#query imgur, return link.

        return getRandomLink()

def getCmd():
        return "!imgur"

def getArgs():
        return 0

def hasEncodings(): #Should only be links, no encodings, unless get title
        return False

