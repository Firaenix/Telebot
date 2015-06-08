# -*- coding: utf-8 -*-
###########################################################################
# Hangman game, not finished, pretty broken atm                           #
# Author: Firaenix                                                        #
###########################################################################

import os
import sdk.group
import sdk.msg
import random
from numpy import genfromtxt
import string

hangdir = "plugin/etc/hangman/"

def help():
        return "!hang(man): Begins a game of hangman"

def do(message, optionsList):
        return play(message, optionsList);

def play(message, optionsList):
        group = optionsList[1]
	peer = optionsList[2]
	tgin = optionsList[0]
	
	# Check if existing game is running
	if not isGameExists():
		# Start a new game
		newGame()

	turn(message[0])

def turn(guess):
	# Get all initial values
	sentence = getSentence()
	unsolved = getUnsolved()
	turns = getTurns()
	failed = getFailed()
	guesses = getGuesses()

	if turns > 0:
		# Assume guess is the full word, remove punctuation and check against sentence
		guess = guess.translate(None, string.punctuation).upper()
		tempSentence = sentence.translate(None, string.punctuation).upper()

		if guess is tempSentence:
			endGame()
			return "You win!"
		# Else if guess is not in the guessesList
		elif guess in sentence:
			if guess not in guesses:
				revealCharInUnsolved(sentence, unsolved, guess)
				guesses += guess
				
				message = unsolved + "\n" + "You guessed "+guess+"!"
				return message
			else:
				return "You've already guessed " + guess +"!"
		# Guess is not in the sentence
		else:
			turns -= 1
			message = "Wrong, you have "+ turns + " more guesses"
			return message
	# Turns <= 0
	else:
		endGame()
		return "You Lose\nSentence was: " + sentence

def revealCharInUnsolved(sentence, unsolved, char):
	tempUnsolved = unsolved

	# Punctuation is already displayed
	if char in string.punctuation:
			return unsolved

	# Need to iterate through unsolved and sentence
	for i, c in enumerate(sentence):
			if c is char:
				tempUnsolved[i] = char.upper()

	return tempUnsolved

def getSentence():
	# Reads ;~ separated document, gets the 0th element
	fileDir = hangdir + "hangman"
        sentence = genfromtxt(fileDir, delimiter=';~', dtype=None)
	return sentence[0]

def getUnsolved():
	# Reads ;~ separated document, gets 1st element
	fileDir = hangdir + "hangman"
        unsolved = genfromtxt(fileDir, delimiter=';~', dtype=None)
	return unsolved[1]

def getTurns():
	# Reads ;~ separated document, gets 2nd element	
	fileDir = hangdir + "hangman"
        turns = genfromtxt(fileDir, delimiter=';~', dtype=None)
	return turns[2]

def getFailed():
	# Reads ;~ separated document, gets 3rd element
	fileDir = hangdir + "hangman"
        failed = genfromtxt(fileDir, delimiter=';~', dtype=None)

	return failed[3]
def getGuesses():
	# Reads ;~ separated document, gets 4th element
        fileDir = hangdir + "hangman"
        guesses = genfromtxt(fileDir, delimiter=';~', dtype=None)

        return guesses[4]

def writeBackToFile(sentence, unsolved, turns, failed, guesses):
	# Clears current file, writes new file, tab delimited
	# sentence;~unsolved;~turns;~failed;~guesses
	os.remove(hangdir + "hangman")
	filePath = hangdir + "hangman"

        # Create a new file
        file = open(filePath, "w+")

	# Write to file:
        # 0: Sentence, 1: Unsolved, 2: Turns, 3: Failed
        file.write(str(sentence) + ";~")
        file.write(str(unsolved) + ";~")
        file.write(str(turns) + ";~")
        file.write(str(failed) + ";~")
        file.write(str(guesses) + ";~")

	return "Wrote to file."

def isGameExists():
	# Check if file exists and is not empty
	if os.path.isfile(hangdir) and not os.stat(hangdir).st_size == 0:
		return True	
	# Else
	return False

def newGame():
	# Check again that the file is empty
	filePath = hangdir + "hangman"
	
	# Create a new file
	file = open(filePath, "w+")

	# New hgame sentence
	sentence  = chooseRandomSentence()
	unsolved = generateUnsolved(sentence)
	turns = 15
	failed = 0
	guesses = ""

	# Write to file:
	# 0: Sentence, 1: Unsolved, 2: Turns, 3: Failed
	file.write(str(sentence) + ";~")
	file.write(str(unsolved) + ";~")
	file.write(str(turns) + ";~")
	file.write(str(failed) + ";~")
	file.write(str(guesses) + ";~")

	file.close()

	message = "Beginning Hangman \n" + unsolved
	return message 

def chooseRandomSentence():
	# Randomly select a sentence from the sentence list
	fileDir = hangdir + "sentences"
	sentences = genfromtxt(fileDir, delimiter=';~', dtype=None)

	print(sentences)

	# Get random item from sentences
	return random.choice(sentences)	

def generateUnsolved(sentence):
	# Converts sentence into a series of _'s and .'s, punctuation is left in
	unsolved = ""
	
	charList = list(str(sentence))

	# For each letter in sentence
	for letter in charList:
		if letter is " ":
                        unsolved += "."
		elif isPunctuation(letter):
			unsolved += letter
		else:
			unsolved += "_ "
	
	return unsolved

def isPunctuation(letter):
	if letter in string.punctuation:
		return True	

	return False

def endGame():
	# erase hangdir + "hangman"
	os.remove(hangdir + "hangman")

def getCmd():
        return ["!hangman","!hang", "!hman"]

def getArgs():
        return 2

def hasEncodings():
        return True

