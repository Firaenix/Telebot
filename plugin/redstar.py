###########################################################################
# North Korea OS Keygen                                                   #
# Author: Hexane                                                          #
###########################################################################
import md5

def help():
        return "!redstar [reg_code]: returns redstar key"

def do(reg_code):

	return "-".join(("%020X"%(int(md5 .new(reg_code).hexdigest()[:20],16)&0xff1f4f8fff1f4f8fff1f))[i:i+4] for i in range(0,20,4))

def getCmd():
        return ["!redstar"]

def getArgs():
        return 1

def hasEncodings():
	return True
