#!/bin/bash

while true
do
	if ps ax | grep -v grep | grep python > /dev/null
	then
    		echo "Bot running. Swiggity swooty."
	else
		killall python
    		nohup python bot.py
	fi
	sleep 30
done
