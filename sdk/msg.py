###################################################
# send message Wrapper SDK for the telegram cli   #
#                                    		  #
# Author: Firaenix                   		  #
##################################################

import traceback
import subprocess
pathtotg='../tg/bin/' 
spacer = "_____________________"

def send_msg(group,peer,message, tgin):

	#process = 
#subprocess.Popen([pathtotg+'telegram-cli','-k',pathtotg+'../tg-server.pub'],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
        if (group is not None):
                message=peer + ": \n" + spacer +"\n" + message

                #4100 is the Telegram limit, make sure that we dont over shoot that.
                #TODO: Split into multiple messages?
                print len(message)
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

                                #tgin.write(' '.join(['send_text', peer.replace(' ','_'), tempfile])+'\n')
				tgin.flush()
                        except Exception as e:
				print "Errored"
				print "Error occurred..."
                                print traceback.print_exc()
                else:
                        tgin.write(' '.join(['msg', peer.replace(' ', '_'), message])+'\n')
			tgin.flush()
                return message

