###########################################################
# change group options Wrapper SDK for the telegram cli   #
#                                                 	  #
# Author: Firaenix                                	  #
###########################################################

import subprocess
import cliInput
import sys


#Explicitly Group Functions
def rename(group, topic, tgin):
        if (group is not None):
                cliInput.write(tgin, 'rename_chat', ' '.join([group.replace(' ', '_'), topic])+'\n')

def set_pic(group, picDir, tgin):
        if (group is not None):
                cliInput.write(tgin, 'chat_set_photo', ' '.join([group.replace(' ', '_'), picDir])+'\n')

def chat_info(group, tgin):
	cliInput.write(tgin, 'chat_info', ' '.join([group.replace(' ', '_')])+'\n')

def add_user(group, user, tgin):
        if (group is not None and tgin is not None):
                cliInput.write(tgin, 'chat_add_user', ' '.join([group.replace(' ', '_'), user])+'\n')

def delete_user(group, user, tgin):
        if (group is not None and tgin is not None):
                cliInput.write(tgin, 'chat_del_user', ' '.join([group.replace(' ', '_'), user])+'\n')

def create_group(group, users, tgin):
	#Users is an array, must give within square brackets eg. [user1, user2, user3, ..., usern]
        if (group is not None and tgin is not None):
                cliInput.write(tgin, 'chat_del_user', ' '.join([group.replace(' ', '_'), " ".join(user)])+'\n')

#Sending Data to Group functions

def send_image(group, photo_dir, tgin):
        if (group is not None and tgin is not None):
                cliInput.write(tgin, 'send_photo', ' '.join([group.replace(' ', '_'), photo_dir])+'\n')

def send_video(group, video_dir, tgin):
        if (group is not None and tgin is not None):
                cliInput.write(tgin, 'send_video', ' '.join([group.replace(' ', '_'), video_dir])+'\n')

def send_doc(group, doc_dir, tgin):
        if (group is not None and tgin is not None):
                cliInput.write(tgin, 'send_document', ' '.join([group.replace(' ', '_'), doc_dir])+'\n')

def send_text(group, text_dir, tgin):
        if (group is not None and tgin is not None):
                cliInput.write(tgin, 'send_text', ' '.join([group.replace(' ', '_'), text_dir])+'\n')

