# -*- coding: utf-8 -*-
###########################################################################
# Renames the chat                                                        #
# Author: Firaenix                                                        #
###########################################################################

import sdk.group

def help():
        return "!rename [New Group Name]: BROKEN AS FUCK PLS NO"

def do(name, optionsList):

        sdk.group.rename(optionsList[1], name, optionsList[0])

def getCmd():
        return "!rename"

def getArgs():
        return 2

def hasEncodings():
        return True

