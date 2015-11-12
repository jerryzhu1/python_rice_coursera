#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# by jerry_zhu

# template for "Stopwatch: The Game"
import simplegui


# define global variables
time = 0
run = False
x = 0
y = 0
message = '0:00:0'
score = '0/0'


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global message
    a = t // 600
    b = (t // 100) % 6
    c = (t // 10) % 10
    d = t % 10
    message = str(a) + ':' + str(b) + str(c) + '.' + str(d)
    return message


# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    global run
    run = True
    timer.start()


def Stop():
    global run, x, y, score
    if run == True:
        if time % 10 == 0:
            x += 1
        y += 1
    run = False
    score = str(x) + '/' + str(y)
    timer.stop()


def Reset():
    global time, run, x, y, score
    time = 0
    format(time)
    x = 0
    y = 0
    run = False
    score = str(x) + '/' + str(y)
    timer.stop()


# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1



# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), [100, 100], 25, 'White')
    canvas.draw_text(score, [250, 100], 25, 'White')


# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 400, 200)


# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", Start, 150)
frame.add_button("Stop", Stop, 150)
frame.add_button("Reset", Reset, 150)
timer = simplegui.create_timer(100, tick)


# start frame
frame.start()

# Please remember to review the grading rubric
