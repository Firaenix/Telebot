####################################################
# handles all the messages that get sent to the CLI#
#                                                  #
# Author: Firaenix                                 #
####################################################

def write(tgin, cmd, message):
	#Grabs the desired command, out puts it to the CLI
	if (tgin is not None):
		tgin.write(' '.join([cmd, message])+'\n')
                tgin.flush()
	else:
		raise Exception('tgin is None!')

