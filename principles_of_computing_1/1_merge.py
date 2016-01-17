#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# by jerry_zhu

"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # calculate the length of inpute line
    length = len(line)

    # create a new line and set some variables
    new_line = list(line)
    final_line = [0]*length
    count = 0
    paired = True
    key = 0

    # find and merge  elements in line
    for dummy_i in range(len(line)):
        if paired and line[dummy_i] != 0:
            key = line[dummy_i]
            index = dummy_i
            paired = False
        elif not paired and line[dummy_i] != 0:
            if line[dummy_i] == key:
                new_line[index] = line[index]*2
                new_line[dummy_i] = 0
                paired = True
            else:
                key = line[dummy_i]
                index = dummy_i

    # resort new_line and remove all zeros to the left
    for dummy_i in range(len(new_line)):
        if new_line[dummy_i] != 0:
            final_line[count] = new_line[dummy_i]
            count += 1
    return final_line
