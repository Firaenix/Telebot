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
import os
import sdk.group
import sdk.media

etcDir = "plugin/etc/downloads/"
link = ""

def help():
        return "!http [link]: Paste a link preceded by ! to see the contents"

def do(message,  optionsList):
	#Plugins with multiple cmds return the message and the command which called it
	httpscheme = message[1]
	message = message[0]

	link = httpscheme+message
	data = None
	try:
                data = urllib2.urlopen(link)
        except urllib2.URLError, e:
                return "Please specify a valid URL."

	content_type = get_content_type(data)
	print content_type
	if content_type == "text":
		return title(link, data, optionsList)
	elif content_type == "image" :
		return send_pic(link, data, optionsList)
	elif content_type == "video":
		return send_video(link, data, optionsList)
	elif not "ERROR" in content_type: #Any other File type
		return send_doc(link, data, optionsList)

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

	return int(info['Content-Length'])

def title(urlLink, data, optionsList):
	page = BeautifulSoup(urllib2.urlopen(urlLink))
	try:
		return page.title.string
	except:
		#If recieve a text file or a file that doesnt have a title, send the file itself
		return send_doc(urlLink, data, optionsList)

def send_doc(urlLink, data, optionsList):
	file_size = get_file_size(data)
	if not file_size > 10485760:
	        #Get the file name+extension
	        saveDir = etcDir+urlLink.split('/')[-1]
	        #Save image to disk
	        imgData = urllib2.urlopen(urlLink).read()
	        output = open(saveDir, 'wb+')
	        if not output.closed:
	                output.write(imgData)
	                output.close()

	        sdk.group.send_doc(optionsList[1], saveDir, optionsList[0])
	        return "File Size: "+str(file_size)+" bytes\n\nDocument downloaded to: \n"+output.name
	
	return "Document is too large to download (> 10 MiB)"


def send_video(urlLink, data, optionsList):
        file_size = get_file_size(data)
        if not file_size > 10485760:
                #Get the file name+extension
                saveDir = etcDir+urlLink.split('/')[-1]
                #Save image to disk
                imgData = urllib2.urlopen(urlLink).read()
                output = open(saveDir, 'wb+')
                if not output.closed:
                        output.write(imgData)
                        output.close()

                sdk.group.send_video(optionsList[1], saveDir, optionsList[0])
                return "File Size: "+str(file_size)+" bytes\n\nVideo downloaded to: \n"+output.name

        return "Video is too large to download (> 10 MiB)"


def send_pic(urlLink, data, optionsList):
	file_size = get_file_size(data)
        if not file_size > 10485760:
	        #Get the file name, add png for case where url has no extension
	        saveDir = etcDir+urlLink.split('/')[-1].split('.')[0]+".png"		

	        #Save image to disk
	        imgData = urllib2.urlopen(urlLink).read()
	        output = open(saveDir, 'wb+')
	        if not output.closed:
	                output.write(imgData)
	                output.close()

	        sdk.group.send_image(optionsList[1], saveDir, optionsList[0])
	        return "File Size: "+str(file_size)+" bytes\n\nPicture downloaded to: \n"+output.name
	
	return "Picture is too large to download (> 10 MiB)"

def getCmd():
        return ["http://", "https://"]

def getArgs():
        return 2

def hasEncodings():
        return True
