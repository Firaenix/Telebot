# -*- coding: utf-8 -*-
###########################################################################
# Handles any http request passed to the server                           #
# Author: Hexane and Firaenix                                             #
###########################################################################
#optionsList[0] = tgin, optionsList[1] = group, optionsList[2] = peer/user

from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError
import urllib2
import ssl
import os

import sdk.group
import sdk.media

etcDir = "plugin/etc/downloads/"
link = ""
sslCxt = ssl._create_unverified_context()

def help():
        return "!http [link]: Paste a link preceded by ! to see the contents"

def do(message,  optionsList):
	#Plugins with multiple cmds return the message and the command which called it
	httpscheme = message[1].lower()
	message = message[0].split(' ')[0]
	
	link = httpscheme+message
	data = None
	
	try:
		header = {'User-Agent' : "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)"}
		request = urllib2.Request(link, None ,header)
                data = urllib2.urlopen(request, context=sslCxt)
        except urllib2.URLError, e:
		return e
	except urllib2.HTTPError, e:
		return e

	content_type = get_content_type(data)
	print content_type
	if content_type == "text":
		return title(link, request, data, optionsList)
	elif content_type == "image" :
		return send_pic(link, request, data, optionsList)
	elif content_type == "video":
		return send_video(link, request, data, optionsList)
	elif not "ERROR" in content_type: #Any other File type
		return send_doc(link, request, data, optionsList)

	return content_type

def get_content_type(data):
        try:
		info = data.info()
		if info['Content-type'].endswith("gif"):
			return "gif"

	        return info.maintype
        except urllib2.HTTPError, e:
                return "ERROR \n" + str(e.code)

def get_file_size(data):
        info = data.info()
	print "Content-Length: "+info['Content-Length']
	# Super ugly way of converting to float to 2 decimal places
	return round((((int(info['Content-Length']))/1000.0)/1000.0), 2)

def title(urlLink, request, data, optionsList):
	try:
		page = BeautifulSoup(urllib2.urlopen(request, context=sslCxt))
	except urllib2.HTTPError, e:
		return e
	try:
		return page.title.string
	except:
		#If recieve a text file or a file that doesnt have a title, send the file itself
		return send_doc(urlLink, request, data, optionsList)

def send_doc(urlLink, request, data, optionsList):
	file_size = get_file_size(data)

	if not file_size > 10:
	        #Get the file name+extension
	        saveDir = etcDir+urlLink.split('/')[-1]

	        #Save image to disk
	        imgData = urllib2.urlopen(request, context=sslCxt).read()
	        output = open(saveDir, 'wb+')

	        if not output.closed:
	                output.write(imgData)
	                output.close()

	        sdk.group.send_doc(optionsList[1], saveDir, optionsList[0])
	        return "File Size: "+str(file_size)+" MB\n\nDocument downloaded to: \n"+output.name
	
	return "Document is too large to download (" + file_size + " MiB)"


def send_video(urlLink, request, data, optionsList):
        file_size = get_file_size(data)

        if not file_size > 10:
                #Get the file name+extension
                saveDir = etcDir+urlLink.split('/')[-1]

                #Save image to disk
                imgData = urllib2.urlopen(request, context=sslCxt).read()
                output = open(saveDir, 'wb+')

                if not output.closed:
                        output.write(imgData)
                        output.close()

                sdk.group.send_video(optionsList[1], saveDir, optionsList[0])
                return "File Size: "+str(file_size)+" MB\n\nVideo downloaded to: \n"+output.name

        return "Video is too large to download (" + file_size + " MiB)"


def send_pic(urlLink, request, data, optionsList):
	file_size = get_file_size(data)

        if not file_size > 10:
	        #Get the file name, add png for case where url has no extension
	        saveDir = etcDir+urlLink.split('/')[-1].split('.')[0]+".png"		

	        #Save image to disk
	        imgData = urllib2.urlopen(request, context=sslCxt).read()
	        output = open(saveDir, 'wb+')

	        if not output.closed:
	                output.write(imgData)
	                output.close()

	        sdk.group.send_image(optionsList[1], saveDir, optionsList[0])
	        return "File Size: "+str(file_size)+" MB\n\nPicture downloaded to: \n"+output.name
	
	return "Picture is too large to download (" + file_size + " MiB)"

def getCmd():
        return ["http://", "https://"]

def getArgs():
        return 2

def hasEncodings():
        return True
