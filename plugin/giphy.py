###########################################################################
# Downloads a gif from giphy                                              #
# Author: Firaenix                                                        #
###########################################################################
import os
import urllib2
import sdk.media
import giphypop

etcDir = "plugin/etc/downloads/"

def help():
        return "!giphy/gif [terms]: Searches giphy and uploads first result"


def do(msg, optionsList):
	#Gets the first giphy result, downloads and uploads to chat
	gif = giphypop.translate(msg[0])

	if gif == None:
		return "No Results."

	while gif.filesize > 5000000:
		gif = giphypop.translate(msg[0])

	url = gif.media_url
	dlFile = gif.id + ".gif"

        #Save image to disk
        if not os.path.isfile(etcDir+dlFile):
                imgData = urllib2.urlopen(url).read()
                output = open(etcDir+dlFile, 'wb+')
                output.write(imgData)
                output.close()

        sdk.media.send_doc(optionsList[1], etcDir+dlFile, optionsList[0])
	return "Uploading " + msg[0] + "\n" + gif.media_url + "\n" + str(gif.filesize) + " Bytes"	

def getCmd():
        return ["!giphy", "!gif"]

def getArgs():
        return 2

def hasEncodings():
        return False

