# Hangman
Classic game of hangman in console

## Description
This project goal is to recreate the classic game of Hangman that the user can play from the computer console. Built using python, the software starts by choosing a random word from a list of 2466 words (words.py). Once a word has been chosen, the software will display the hangman at its initial state and the empty spaces in order to let the user know the length of the word. The player is only allowed to enter one letter at a time and the software will be able to recognize if input entered is more than one letter or not a letter (number or symbol). The software will also let the user know if the input given was repeated, if the guess was correct or incorrect and print out the hangman display after every guess. After winning or losing the game the player can choose to play another round and the software will also keep track of the amount of points, but this will reset after the game is closed. 

Word list from: https://www.randomlists.com/data/words.json

## How to use
1. Download **hangman.y** & **words.py**
2. Run `hangman.py`
3. Play!

You can play as many rounds as you like and the game keeps track of the round number and the points you earned

## Challenges faced
- Usage of python lists
- Learning pytest
- Creating a test for a function that asks user for input by creating mock inputs

## Learning outcomes
- Python (First time building something with python)
- Pytest
