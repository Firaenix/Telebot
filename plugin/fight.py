# -*- coding: utf-8 -*-
###########################################################################
# Dukes it out between 2 people in the chat                               #
# Author: Firaenix                                                        #
###########################################################################
from random import randrange

def help():
        return "!fight [person1]vs[person 2]: Initiates a fight between 2 people IRL."

def do(input):
	args = input.split(" vs ")
	nonelist = ["The Terminator", "The Invisible Man", "The Rock", "Jim Carrey", "Powdered ToastMan", "Oasis", "Mike Oldfield", "Tom and Jerry", "Goku", "Vegeta", "A Ham Sandwich", "Spaghetti"]

	if len(args[0]) is 0:
		args[0] = nonelist[randrange(len(nonelist))]

	if len(args) == 1:
		args.append(nonelist[randrange(len(nonelist))])

	randWin = randrange(3)


	message = "A fight has broken out between "+args[0].title() +" and "+args[1].title()+" IRL.\n"
	message = message +"The tension between the two is palpable...\n"+args[randrange(2)].title()+" is staring intensely at his opponent.\n"
	message = message +args[randrange(2)].title()+" strikes!\n"
	message = message +"Punches are flying in all directions! Onlookers are stunned!\n"

	if randWin == 2:
		message = message +"As the dust settles, both fighters are lying in a pool of blood,\nneither fighter is moving...\n\n"	
	        message = message + "=============\nNO ONE WINS!!\n============="
	
	else:
		message = message +"As the dust settles, one person walks out on top...\n"
		message = message + "Of course, it could only be "+args[randWin].title()+"!\n\n"
	        message = message + "=============\n"+args[randWin].upper()+" WINS!!\n============="



        return message

def getCmd():
        return ["!fight"]

def getArgs():
        return 1

def hasEncodings():
        return True

