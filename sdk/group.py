###########################################################
# change group options Wrapper SDK for the telegram cli   #
#                                                 	  #
# Author: Firaenix                                	  #
###########################################################

import subprocess
import cliInput
import sys

def rename(group, topic, tgin):
        if (group is not None):
		print group
                cliInput.write(tgin, 'rename_chat', ' '.join([group.replace(' ', '_'), topic])+'\n')


