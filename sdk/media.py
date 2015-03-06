###########################################################
# media functions Wrapper SDK for the telegram cli        #
#                                                         #
# Author: Firaenix                                        #
###########################################################

import subprocess
import cliInput
import sys

def send_image(group, photo_dir, tgin):
        if (group is not None and tgin is not None):
                cliInput.write(tgin, 'send_photo', ' '.join([group.replace(' ', '_'), photo_dir])+'\n')

def send_doc(group, doc_dir, tgin):
        if (group is not None and tgin is not None):
                cliInput.write(tgin, 'send_document', ' '.join([group.replace(' ', '_'), doc_dir])+'\n')


def set_profile_pic(photo_dir, tgin):
        if (photo_dir is not None and tgin is not None):
                cliInput.write(tgin, 'set_profile_photo', ' '.join([photo_dir])+'\n')

