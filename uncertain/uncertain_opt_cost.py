#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

def uncertain_opt_cost(items,K1,strategy):

    n_plus, n_min = 0
    items_copy = items
    answers = []
    current_questions = []
    while len(answers) < K1:
        current_element= calculate(items_copy[0:K1-len(answers)])

        #sbagliato da rivedere

        for i in current_element:
            if calculate(items) == 0:
                n_plus = n_plus + 1
            else:
                n_min = n_min + 1
            # y(r(i) = y(0,0)
            current_questions.append(min(n_min,n_plus))

        answers = input()
        for i in current_questions:
            if strategy(answers) == 1:
                del (items_copy[i])
                set.append(i)

            if strategy(answers) == 0:
                del (items_copy[i])


def calculate(items):
    cost = []
    for item in items:
        temp = probability.item * n_questions
        cost.append(temp)
    return min(cost)
