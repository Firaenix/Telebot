###########################################################
# change group options Wrapper SDK for the telegram cli   #
#                                                 	  #
# Author: Firaenix                                	  #
###########################################################

import subprocess
pathtotg='../tg/bin/'

spacer = "_____________________"
import sys

def rename(group, topic, tgin):
        if (group is not None):
		print "Group: "+group
		print "topic: "+topic
		tgin.flush()
                tgin.write('rename_chat '+group+' '+topic)


