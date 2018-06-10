items = []

def opt_sequential(items,K1):
    answers = []
    set = []
    items_copy = items
    while len(answers) < K1:
       min_element = calculate(items)
        #ask questions
        current_answer = input(min_element)
        answers.append(current_answer)
        if strategy(answers) == 1:
            del(items_copy[min_element])
            set.append(min_element)

        if strategy(answers) == 0:
            del (items_copy[min_element])
        
def calculate(items):
    cost = []
    for item in items:
       temp =  probability.item * n_questions
       cost.append(temp)
    return min(cost)
