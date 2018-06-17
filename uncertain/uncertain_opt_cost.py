#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

probability_threshold = 0.6
cats_items = {}
junk_items = {}
doubt_items = {}

def uncOptCost(items, K1, strategy):
    while len(cats_items) < K1:
        for item in items:
            #missing answers
            evaluate_item(item, answers, strategy)
            if len(cats_items) == K1:
                break

def evaluate_item(item, answers, strategy):
    #for each assistant, evaluate the item and store the answer in a list
    #the answers contained an error rate yet
    result = threshold(answers)
    #there's a cat
    if result == 1:
        cats_items.append(item)
    elif result == -1:
        junk_items.append(item)
    elif result == 0:
        doubt_items.append(item)


#calculating y probability
def expected_cost(pos_questions, neg_questions, tot_questions):
    pos_probability = pos_questions / tot_questions
    neg_probability = neg_questions / tot_questions
    estimated_cost = pos_probability * pos_questions + neg_probability * neg_questions
    if estimated_cost > probability_threshold:
        return False
    else:
        return True

