###########################################################################
# Notes plugin for Hexbot, saves input to a text file                     #
#                                                                         #
# Author: Firaenix                                                        #
###########################################################################

import os.path
import datetime

dt = datetime.datetime.now()
date = str(dt.day)+"/"+str(dt.month)+"/"+str(dt.year)
etcDir = "plugin/etc/"
notesdir = etcDir+"notes"

def help():
        return "!notes [input]/read: saves the input to the notes file"

def do(input):
	if len(input) > 120:
		return "Message too long. Try again with a shorter sentence."
	output = ""

	#check for remove command
	list = input.split(" ")
	if list[0] == "rm":
		try:
			value = int(list[1])
			output = removeNote(value)
			
		except Exception as e:
			output = "Specified value was not a number, please try again.\n\n"

	elif not input == "":
		#Save input to notes file
		output = saveNote(input)		

        #Everything done, print out contents.
	output = output+printOut()
	return output

def saveNote(input):
	#Save input to notes file
        checkExists()
	#appends file
        with open(notesdir, "a") as notesfile:
        	notesfile.write(date+": "+input+"\n")
                return "Note Saved.\n\n"
	
	return "Failed to save note, try again."

def removeNote(noteInt):
	checkExists()
	output = ""
	
	#Read all lines into a list
	linelist = []
	with open(notesdir, "r") as file:
		linelist = file.readlines()
	
	#Check int is valid, output all contents of the list 
	#back into the file, excluding noteInt	
	if noteInt >= 1 and noteInt <= len(linelist):
		#removes line at given int
		for x in range(0, len(linelist)):
			if x+1 == noteInt:
				print "Skipping line: %i",noteInt
			else:
				output = output+linelist[x]

		with open(notesdir, "w") as notesfile:
			notesfile.write(output)
	
	else:
		return "Input number is out of bounds.\n\n"
	
	return "Note at positon "+str(noteInt)+" removed.\n\n"


def printOut():
	#Make sure file exists before printing
	checkExists()
	output = ""
	#Read all lines out to screen
        with open(notesdir, "r") as file:
                for line in file:
                        output = output+line
        return output


def checkExists():
	#check if notes file exists
        if not os.path.isfile(notesdir):
	        #Creates a new blank file
                with open(notesdir, "w") as file:
         	       print "Created new notes file"

def getCmd():
        return "!notes"

def getArgs():
        return 1

def hasEncodings():
        return False

