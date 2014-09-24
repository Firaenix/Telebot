Telebot
===================

Telegram bot written in Python which is loosely basted off of the work from asdofindia. Heavily modified by @Firaenix & @Hexane_ with lots of improvements!


## Setup Guide ##

Prior to installing this, [vysheng's tg cli](http://github.com/vysheng/tg) needs to be installed so the bot can communicate on Telegram. This can be done with
    
    git clone https://github.com/vysheng/tg.git && cd tg
    ./configure
    make

Run that and configure an account
    
    ./telegram -k tg-server.pub

You will need a valid phone number to authenticate the client with Telegrams servers. You can use your own or use any online verification service, provided it hasnt be previously used by another Telegram user.

Note: Current system time is critical when connecting to Telegram. If your system time is off by even a minute or two, the client will start throw errors.    

### Instalation and configuration of the bot###

Telebot uses a slew of Python libraries which can be obtained with pip or python easy install. Check the leading lines in bot.py and plugin.

The repo can be downloaded and put to use with the following command
    
    git clone https://github.com/Hexane/telebot.git && cd telebot

A couple of things need to be edited prior to starting the bot.    

Within bot.py the path to the telegram client needs to be changed within the pathtotg variable. By default it is '../tg/'
/plugin/wolf.py needs a valid app id to work. This can be obtained on the developer section of the Wolfram website.

### Disabling modules ###
If you don't want some of these modules, just remove them from the modules array in callmodule function
If you want to disable twitter, just comment out all lines with 'twitbot' in it in the main function.


## Features, Fixes and Fun ##
  
* The bot can be communicate to in a group chat or single chat. 
* Text encoding has been fixed.
* Name addressing has been fixed.
* Plugins are now fully modular.
* Neat plugin framework.
* Slew of new plugins.
* Lots of engine improvements!
* + Everything else I've forgotten to mention.

## Commands ##

!wolf [query]: Will search Wolfram|Alpha for a solution to a query
!pat : Send the bot some love
!slap [user] : Slaps the user with a large trout
!reboot : Restarts the bot
!time : Returns the current Server System Date/Time
!flip: flip some fuckin' tables
!penis : The textual fallace
!finger: spread hatred across the chat
!google [search_term]: Searches google for given search term 
!uptime : Returns how long the bot has been running.
!interject string: returns interjection
!wiki [term]: Searches wikipedia for the given term
!credits: Displays the credits for HexBot


## Credits ##

asdofindia - Base/Original code.
Firaenix - Massive overhauls, majority of work. 
Hexane_ - Improvements, Plugins.
