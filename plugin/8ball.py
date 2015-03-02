###########################################################################
# An 8ball function							  #
# Author: Hexane		                                          #
###########################################################################
import random

answers = ["It is certain.",
"It is decidedly so",
"Without a doubt",
"Yes definitely.",
"You may rely on it.",
"As I see it, yes.",
"Most likely.",
"Outlook good.",
"Yes.",
"Signs point to yes.",
"Reply hazy try again.",
"Ask again later.",
"Better not tell you now.",
"Cannot predict now.",
"Concentrate and ask again.",
"Dont count on it.",
"My reply is now.",
"My sources say no.",
"Outlook not so good.",
"Very doubtful."
]

def help():
        return "!8ball: answers arbitrary questions."

def do(args):
	if args == "":
		return "You got a question? You ask the 8ball"
	if "am i ever gonna see your face again" in args.lower():
		return "NO WAY GET FUCKED FUCK OFF"
	else:
		random.seed()
		shaker = random.randint(0,19)
		return answers[shaker]


def getCmd():
        return "!8ball"

def getArgs():
        return 1

def hasEncodings():
	return True
