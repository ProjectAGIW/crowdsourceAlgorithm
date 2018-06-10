#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

# items = dataset di input, output_condition = condizione di output, properties = proprieta' da soddisfare,
# questions = numero di domande, n_answers = numero delle risposte corrette

from model import Element

questions = []
items = []

def algorithm_outline(items, output_condition):

    items_evaluated = []
    latency = 0
	cost = 0
    answers = []
    while output_condition == False :
        #selection of items
        for item in items:
            #take only items that are not evaluated yet
            if not item.has_evaluation:
                items_evaluated.append(i)

        #ask to human about the item        
        for element,question in items_evaluated, questions:
            current_answer = input(question,element)
            latency += 1
            cost += 1
            #set evaluated to item
            element.has_evaluation = True
            #convert human's answer to 1/0 domain
            element.properties = answer_to_property(current_answer)
        
        print("Latency is: " + str(latency))
        print("Cost is : " + str(cost))
            
        for item,answers[i] in items_evaluated:
            if item.properties == 1:
                answers = answers + 1
                
        output_condition(answers)

def output_condition(answers):
    #omitted

def answer_to_property(answer):
    #omitted


