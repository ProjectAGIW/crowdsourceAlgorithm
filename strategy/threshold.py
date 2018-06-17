#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

def threshold(rated_answers):

    sum_answers = sum(rated_answers)
    if sum_answers > 0:
        #it's a cat
        return 1
    elif sum_answers == 0:
        # difficult question
        return 0
    else:
        # it's not a cat
        return -1