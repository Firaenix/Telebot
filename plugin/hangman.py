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
	if not isGameExists() or message[0] == "new_game":
		# Start a new game
		return newGame()

	return turn(message[0], peer)

def turn(guess, peer):
	# Get all initial values
	sentence = getSentence()
	unsolved = getUnsolved()
	turns = int(getTurns())
	failed = getFailed()
	guesses = getGuesses()

	if turns > 0:
		# Assume guess is the full word, remove punctuation and check against sentence
		guess = guess.translate(None, string.punctuation).upper()
		tempSentence = sentence.translate(None, string.punctuation).upper()

		# Guessed correctly, won the game
		if guess == tempSentence:
			return gameWin(peer, unsolved)

		# Else if guess is not in the guessesList
		elif guess in tempSentence:
			# Guess is a word in tempSentence but not the whole sentence
			if len(guess) > 1:
				return unsolved + "\n" + guess + " is in the sentence, you're on the right track!"

			if guess not in guesses:
				unsolved = revealCharInUnsolved(sentence, unsolved, guess)
				guesses += guess
				
				message = unsolved + "\n" + "You guessed "+guess+"!"
				
				writeBackToFile(sentence, unsolved, turns, failed, guesses)
				
				if not isSolved(unsolved, sentence, peer):
					return message
				return gameWin(peer, unsolved)
			else:
				writeBackToFile(sentence, unsolved, turns, failed, guesses)
				return unsolved+"\nYou've already guessed " + guess +"!"
		# Guess is not in the sentence
		else:
			
			if guess in guesses:
                                writeBackToFile(sentence, unsolved, turns, failed, guesses)
                                return unsolved+"\nYou've already guessed " + guess +"!"

			turns -= 1
			guesses += guess
			message = unsolved +"\nWrong, you have "+ str(turns) + " more guesses"

			writeBackToFile(sentence, unsolved, turns, failed, guesses)
			return message

		# Turn over, write back
		writeBackToFile(sentence, unsolved, turns, failed, guesses)
	# Turns <= 0
	else:
		endGame()
		return "You Lose\nSentence was: " + sentence


def gameWin(peer, unsolved):
	endGame()
	return unsolved+ "\n"+peer + " Wins!"

def isSolved(unsolved, sentence, peer):
	unsolved = unsolved.replace(" ", "")
	unsolved = unsolved.replace(".", " ")
	
	
	if unsolved.upper() == sentence.upper():
		print "Solved! Won Game!"
		return True

	return False

def revealCharInUnsolved(sentence, unsolved, char):
	tempUnsolved = unsolved

	# Punctuation is already displayed
	if char in string.punctuation:
			return unsolved

	# Need to iterate through unsolved and sentence
	for i, c in enumerate(sentence):
			if c.upper() == char.upper():
				tempUnsolved = replaceCharAtIndex(tempUnsolved, i, char)

	return tempUnsolved

def replaceCharAtIndex(word, index, char):
	# Remove all spaces, for consistency
	wordList = list(word.replace(" ", ""))
	
	wordList[index] = char

	# Re add all spaces
	return ' '.join(wordList)

def getSentence():
	# Reads ;~ separated document, gets the 0th element
	fileDir = hangdir + "hangman"
	
	with open(fileDir, "r") as myfile:
	        data = myfile.read().split(";~")
		return data[0]
	
	return None

def getUnsolved():
	# Reads ;~ separated document, gets 1st element
	fileDir = hangdir + "hangman"

	with open(fileDir, "r") as myfile:
                data = myfile.read().split(";~")
                return data[1]

	return None

def getTurns():
	# Reads ;~ separated document, gets 2nd element	
	fileDir = hangdir + "hangman"
	
	with open(fileDir, "r") as myfile:
                data = myfile.read().split(";~")
                return int(data[2])

	return None

def getFailed():
	# Reads ;~ separated document, gets 3rd element
	fileDir = hangdir + "hangman"
        
	with open(fileDir, "r") as myfile:
                data = myfile.read().split(";~")
                return data[3]

	return None

def getGuesses():
	# Reads ;~ separated document, gets 4th element
        fileDir = hangdir + "hangman"
        
	with open(fileDir, "r") as myfile:
                data = myfile.read().split(";~")
                return data[4]

        return None

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
	if os.path.isfile(hangdir + "hangman"):
		print "Game Exists"
		return True	
	# Else
	print "No Game Exists"
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

	message = "Started new game of Hangman! \n" + unsolved
	return message 

def chooseRandomSentence():
	# Randomly select a sentence from the sentence list
	fileDir = hangdir + "sentences"
	sentences = genfromtxt(fileDir, delimiter=';~', dtype=None)

	# Get random item from sentences
	return random.choice(sentences)[0]

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

