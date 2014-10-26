###########################################################################
# Notes plugin for Hexbot, saves input to a text file                     #
#                                                                         #
# Author: Firaenix                                                        #
###########################################################################

import os.path

etcDir = "plugin/etc/"
notesdir = etcDir+"notes"

def help():
        return "!notes [input]/read: saves the input to the notes file"

def do(input):
	if input == "read":
		#If input is empty, check if notes file exists		
		if not os.path.isfile(notesdir):
			#Creates a new blank file
			with open(notesdir, "w") as file:
				print "Created new notes file"
		#Read all lines out to screen.
		lines = ""
		with open(notesdir, "r") as file:
			for line in file:
				lines = lines+line
		return lines
			
	elif not input == "":
		#Save input to notes file
		#check if notes file exists
                if not os.path.isfile(notesdir):
                        #Creates a new blank file
                        with open(notesdir, "w") as file:
                                print "Created new notes file"

		with open(notesdir, "a") as notesfile:
   			 notesfile.write(input+"\n")
		return "Saved note."

        return "Failed to read/save note, idk why lol ask gaben."

def getCmd():
        return "!notes"

def getArgs():
        return 1

def hasEncodings():
        return False

