###########################################################################
# Minecraft Bukkit/Spigot Integration Plugin				  #
# Author: Hexane		                                          #
###########################################################################
import subprocess
import os
import pluginComponent

craftDir = "/home/craft/"
jar = "spigot.jar"

def help():
        return "!mc [start/stop/reload] controls minecraft server"

def do(args, optionsList):

	# To write to a command line
	# writes the initial command to the spigot cli, 
	# adding the extra commands from the array onto the end of the initial, separated by spaces
	#write(mcin, "First command eg. /start", ' '.join(["Extra", "commands"]))
	
	if args == "start":
        	_proc = subprocess.Popen(["java", "-Xms128M", "-Xmx512M", "-XX:MaxPermSize=128M", "-jar", craftDir+jar],stdin=subprocess.PIPE,stdout=subprocess.PIPE, cwd=craftDir)
	        mcin = _proc.stdin
		
		for line in iter(optionsList[3].readline, ''):
			if "!mc stop" in line:
				#stop minecraft
				write(mcin, "save-all", "")
				write(mcin, "stop", "")
				_proc.kill()
				mcin = None
				return "Minecraft stopped"
				#break out of the for loop with a return or something
			elif "!mc broadcast" in line:
				print line
                                write(mcin, "say", line)

			
			pluginComponent.callmodule(line, optionsList)

		return "CUUUUUUUUUUUUUUUUUNT"
		#for line in iter(_proc.stdout.readline,''):
		#	print line.rstrip()

		
	elif args == "say":
	        write(mcin, "say", ' '.join(["JOIN", "ISIS"]))
	        #write(mcin, "First command eg. /start", ' '.join(["Extra", "commands"]))

		return "Broadcasted."	
	elif args == "reload":
		return "Reloaded."


def write(mcin, cmd, message):
	 #Grabs the desired command, out puts it to the CLI
	 if (mcin is not None):
		 print cmd
		 print message
		 mcin.write(' '.join([cmd, message])+'\n')
		 mcin.flush()
	 else:
		 raise Exception('mcin is None!')

def getCmd():
        return ["!mc"]

def getArgs():
        return 2

def hasEncodings():
	return True
