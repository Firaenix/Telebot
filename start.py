#!/usr/bin/python

import subprocess
import sys

proc = subprocess.Popen(['python','-u','bot.py'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)

while True:
	try:

  		line = proc.stdout.read()
  		print line.rstrip()
  		if "Telegram-cli" in line:
    			print "line captured:  ", line.rstrip()
    			line.stdout.flush()
  		else:
    			break

	except:
		print "Crashed. Do something...", sys.exc_info()
