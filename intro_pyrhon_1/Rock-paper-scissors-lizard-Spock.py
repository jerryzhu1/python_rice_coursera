#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# by jerry_zhu

#convert name to number
def name_to_number(name):
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        print "The name is invalid"
    return number

#convert number to name
def number_to_name(number):
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        print "The number is invalid"
    return name

#generate computer's guess and print out the winner
def rpsls(player_choice):
    print "Player chooses",str(player_choice)

    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)

    print "Computer chooses",str(comp_choice)

    dif = (player_number - comp_number) % 5
    if dif == 1 or dif == 2:
        print "Player wins!"
    elif dif == 3 or dif == 4:
        print "Computer wins!"
    else:
        print"Player and computer tie!"
    print " "

#import "random"
import random

#test my code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


