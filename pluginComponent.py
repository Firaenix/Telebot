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
                                cmdStr = module.getCmd()

                                #Runs the command and returns desired input
                                pluginCmds.append(cmdStr)

                                #On start up, adds the help text to the string
                                s = module.help()
					
                               
                                helpString += "\n"+ s
                        except Exception as e:
                                print traceback.print_exc()

        pluginCmds.append("!help")
	pluginCmds.append("!reloadmodules")
	pluginCmds.append("!reloadplugins")
        print pluginCmds
        print plugins


def importPlugins(name):
    mod = __import__(name, fromlist=[''])
    return mod
	


def callmodule(message):
        try:
                message=message#.decode(encoding="UTF-8",errors="ignore")
                print message
        except Exception as e:
                print "Error occurred: "
		err = traceback.print_exc()
          	print err

                message = "error"
        count = 0
        for pluginCmd in pluginCmds:
                if (message.find(pluginCmd)==0):
                        message=message[len(pluginCmd)+1:]

                        try:
                                #Only cmd that should not be in plugins is !help
                                if pluginCmd == "!help":
					print "this"
                                        return help()
				if pluginCmd == "!reloadmodules":
					print "hit"
					return str(plugins)+reloadModules()
				if pluginCmd == "!reloadplugins":
					return str(plugins)+reloadModules()
                                else:
                                        #If commands match
                                        if pluginCmd == plugins[count].getCmd():
                                               
                                                #Check how many arguments the method takes
                                                if plugins[count].getArgs() > 0:
							#If plugin uses any encoding other than ASCII
							if plugins[count].hasEncodings():
                                                        	reply = plugins[count].do(message)
                                                        	return ("%s" % reply).encode('UTF-8')
							else:
								reply = plugins[count].do(message)
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
