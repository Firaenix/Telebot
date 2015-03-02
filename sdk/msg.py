###################################################
# send message Wrapper SDK for the telegram cli   #
#                                    		  #
# Author: Firaenix                   		  #
##################################################

import traceback
import cliInput

spacer = "_____________________"

def send_msg(group,peer,message, tgin):
        if (group is not None):
                message=peer + ": \n" + spacer +"\n" + message
                #4100 is the Telegram limit, make sure that we dont over shoot that.
                #TODO: Split into multiple messages?
                if len(message) >= 4100:
                        print "Too long! Trimming..."
                        message = message[:4090]+"..."

                peer=group.rstrip()
                if(('\n' in message)or('\r' in message) or ('\r\n' in message)):
                        try:
                                tempfile='temp'
                                temp=open(tempfile,'w')
                                #Handle potential unicode situations
                                temp.write(message)
                                temp.close()
				
				if temp is not None:
					cliInput.write(tgin, 'send_text', ' '.join([peer.replace(' ', '_'), tempfile])+'\n')
                        except Exception as e:
				print "Error occurred..."
                                print traceback.print_exc()
                else:
			cliInput.write(tgin, 'msg', ' '.join([peer.replace(' ', '_'), message])+'\n')
                return message

