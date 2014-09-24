###########################################################################
# Metacritic plugin for HexBot                                             #
#                                                                         #
# Author: Firaenix                                                        #
###########################################################################

import plugin.libraries.pycritic as pycritic

def help():
        return "!critic [console],[term]: Searches Metacritic for the given term \nConsoles:(xb1, 360, xbone, ps, ps2, ps3, ps4, gc, wii, wiiu, pc)"


def do(term):
	console = term.split(",")[0]	
	game = term.split(",")[1]
	game = game.replace(" ", "-")

	if console == "xb1":
		console = "xbox"
	if console == "360":
		console = "xbox-360"
	if console == "xbone":
		console = "xbox-one"
	if console == "ps":
		console = "playstation"
	if console == "ps2":
		console = "playstation-2"
	if console == "ps3":
		console = "playstation-3"
	if console == "ps4":
		console = "playstation-4"
	if console == "gc":
		console = "gamecube"
	if console == "wii":
		console = "wii"
	if console == "wiiu":
		console = "wii-u"
	
	scraper = pycritic.Scraper()
	resource = scraper.get("http://www.metacritic.com/game/"+console+"/"+game)	

        response = resource.name + "\n" 
	response = response+resource.date + "\n" 
	response = response+ "Metascore: "+resource.metascore + "User Score: "+resource.userscore+"\n"
	response = response+resource.description 

        return response

def getCmd():
        return "!critic"

def getArgs():
        return 1

def hasEncodings():
        return True


