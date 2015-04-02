import sys 
import io 
import traceback 
import glob 
import compileall
import os
import subprocess

import bot


pluginCmds = []
plugins = []
helpString = ''
spacer = "_____________________"


def getPlugins(firstRun):
        #This method dynamically loads plugins at startup
	global pluginCmds
	global plugins	
	global helpString 
	pluginCmds = []
	plugins = []
	helpString = 'All possible commands:\n'

	if(not firstRun):
		workingDir = os.path.dirname(os.path.realpath("bot.py"))
		print workingDir	
		compileall.compile_dir(workingDir)

        path = "plugin/*.py"
        print "Initializing plugins..."
        for fname in glob.glob(path):
		plugin_path = fname.split(".py")[0]
                package_plugin = plugin_path.replace("/", ".")

                if(package_plugin != "plugin.__init__"):
                        try:
                                print package_plugin

                                #Dynamic imports the plugins in the plugin directory
				try:
                                	plugins.append(importPlugins(package_plugin))
				except ImportError:
					print "Unable to import plugin, is it valid?"
					print traceback.print_exc()

				module = importPlugins(package_plugin)
                                cmds = module.getCmd()

                                #Runs the command and returns desired input
                                pluginCmds.append(cmds)

                                #On start up, adds the help text to the string
                                s = module.help()
					
                               
                                helpString += "\n"+ s
                        except Exception as e:
                                print traceback.print_exc()

        pluginCmds.append(["!help"])
	#pluginCmds.append(["!reloadmodules"])
	#pluginCmds.append(["!reloadplugins"])

def importPlugins(name):
    mod = __import__(name, fromlist=[''])
    return mod
	
def callmodule(message, optionsList):
        command = message.split(' ')[0]
        count = 0
        for pluginCmd in pluginCmds:
		for subCmd in pluginCmd:

	                if (command.lower() == subCmd or (subCmd[0] != "!" and subCmd in command.lower())):
				#turns the message into the arguments to pass to the plugin
				if subCmd[0] == '!':
	        	                message=message[len(subCmd)+1:]
				else:
					message=message[len(subCmd):]

                	        try:
                        	        #Only cmd that should not be in plugins is !help
                                	if subCmd == "!help":
        	                                return help()
                	                else:
                        	                #If commands match
                                        	if subCmd.lower() in plugins[count].getCmd():
							#Tell the plugin which command was used to call it
                                             		if len(pluginCmd) > 1:
								message = [message, subCmd]  
                                                	
							#Check how many arguments the method takes
	                                                if plugins[count].getArgs() == 1:
								#If plugin uses any encoding other than ASCII
								if plugins[count].hasEncodings():
                        	                                	reply = plugins[count].do(message)
                                	                        	return ("%s" % reply).encode('UTF-8')
								else:
									reply = plugins[count].do(message)
                                                       	        	return reply
							if plugins[count].getArgs() > 1:
								#If any plugin needs SDK functions, args must be > 1
								#If plugin uses any encoding other than ASCII
                        	                                if plugins[count].hasEncodings():
                                	                                reply = plugins[count].do(message, optionsList)
                                        	                        return ("%s" % reply).encode('UTF-8')
                                                	        else:
                                                        	        reply = plugins[count].do(message, optionsList)
	                                                                return reply	
	                                                else :
								if plugins[count].hasEncodings():
	        	                                                reply = plugins[count].do()      
        	        	                                        return ("%s" % reply).encode('UTF-8')
								else:
									reply = plugins[count].do()
                                                	                return reply
	                        except Exception as e:
        	                        print "Error occurred..."
					err = traceback.print_exc()
                        	        print err

                                	return "Error Occurred. \n\n"+traceback.format_exc()

		count = count+1


def help():
        return helpString

def reloadModules():
	print "\nReloading modules"
	getPlugins(False)
	return "\nReloading modules... \nPlease wait a moment"
