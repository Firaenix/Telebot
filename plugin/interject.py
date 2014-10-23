#################################################
#						#
#						#
#################################################

def do(terms): 

	if terms == "":
		terms = "Linux"
	else:
		terms = terms.rstrip('\n')

	interjection = "I'd just like to interject for moment. What you're refering to as " + terms + ", is in fact, GNU/" + terms + ", or as I've recently taken to calling it, GNU plus " + terms + ". " + terms + " is not an operating system unto itself, but rather another free component of a fully functioning GNU system made useful by the GNU corelibs, shell utilities and vital system components comprising a full OS as defined by POSIX.\n\nMany computer users run a modified version of the GNU system every day, without realizing it. Through a peculiar turn of events, the version of GNU which is widely used today is often called " + terms + ", and many of its users are not aware that it is basically the GNU system, developed by the GNU Project.\n\nThere really is a " + terms + ", and these people are using it, but it is just a part of the system they use. " + terms + " is the kernel: the program in the system that allocates the machine's resources to the other programs that you run. The kernel is an essential part of an operating system, but useless by itself; it can only function in the context of a complete operating system. " + terms + " is normally used in combination with the GNU operating system: the whole system is basically GNU with " + terms + " added, or GNU/" + terms + ". All the so-called " + terms + " distributions are really distributions of GNU/" + terms + "!"
	return interjection
    
def help():
	return "!interject string: returns interjection"

def getCmd():
	return "!interject"

def getArgs():
	return 1

def hasEncodings():
        return True

