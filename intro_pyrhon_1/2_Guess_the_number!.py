#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# by jerry_zhu

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


import random
import simplegui
import math

numb_range = 100
numb_range_low = 0
numb_range_high = 100


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, numb_remain
    numb_remain = int(math.ceil(math.log(numb_range + 1, 2)))
    secret_number = random.randrange(0,numb_range)

    print "New game. Range is from 0 to",numb_range
    print "Number of remaining guesses is", numb_remain
    print ""

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global secret_number, numb_remain,numb_range
    secret_number = random.randrange(0,100)
    numb_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global secret_number, numb_remain,numb_range
    secret_number = random.randrange(0,1000)
    numb_range = 1000
    new_game()

def input_guess(t):
    # main game logic goes here
    global numb_remain
    guess = int(t)
    numb_remain = numb_remain - 1
    print "Guess was",guess
    print "Number of remaining guesses is",numb_remain

    if guess == secret_number:
        print "Correct!"
        print ""
        new_game()
    elif guess < secret_number and numb_remain <> 0:
        print "Higher!"
    elif guess > secret_number and numb_remain <> 0:
        print "Lower!"
    pass

    if numb_remain == 0:
        print "You ran out of guesses. The number was",secret_number
        print ""
        new_game()
    else:
        print ""

# create frame
f = simplegui.create_frame("Guess the number",200,200)

# register event handlers for control elements and start framefradd
f.add_button('Range is [0,100)', range100, 200)
f.add_button('Range is [0,1000)', range1000, 200)
f.add_button('New game',new_game, 200)
f.add_input('Enter a guess', input_guess, 200)

# call new_game
new_game()


# always remember to check your completed program against the grading rubric
