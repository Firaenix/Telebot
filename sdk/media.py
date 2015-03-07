###########################################################
# media functions Wrapper SDK for the telegram cli        #
#                                                         #
# Author: Firaenix                                        #
###########################################################

import subprocess
import cliInput
import sys

#Send Data files
def send_image(user, photo_dir, tgin):
        if (user is not None and tgin is not None):
                cliInput.write(tgin, 'send_photo', ' '.join([user.replace(' ', '_'), photo_dir])+'\n')

def send_doc(user, doc_dir, tgin):
        if (user is not None and tgin is not None):
                cliInput.write(tgin, 'send_document', ' '.join([user.replace(' ', '_'), doc_dir])+'\n')

def send_video(user, video_dir, tgin):
        if (user is not None and tgin is not None):
                cliInput.write(tgin, 'send_video', ' '.join([user.replace(' ', '_'), video_dir])+'\n')

def send_text(user, text_dir, tgin):
        if (user is not None and tgin is not None):
                cliInput.write(tgin, 'send_text', ' '.join([user.replace(' ', '_'), text_dir])+'\n')

#other functions
def set_profile_pic(photo_dir, tgin):
        if (photo_dir is not None and tgin is not None):
                cliInput.write(tgin, 'set_profile_photo', ' '.join([photo_dir])+'\n')

