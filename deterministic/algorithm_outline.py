# items = dataset di input, output_condtion = condizione di output, properties = proprieta' da soddisfare,
# questions = numero di domande, n_answers = numero delle risposte corrette
n_answers = 0
questions = []
items = [1, 2, 3, 4]
properties = ['cat is on the table']


def algorithm_outline(items, output_condition, properties):

    global n_answers
    items_evaluated = []
    latency = 0
    n_questions = 0
    epsilon = []
    result = 0
    answers = []
    while n_answers == 0 :
        for i in questions:
            if i not in items_evaluated:
                items_evaluated.append(i)

        '''for i in items_evaluated:
            current_answer = input(properties,i)
            latency = latency +1
            n_questions = n_questions + questions
            answers = []
            '''
        for i,answers[i] in items_evaluated:
            if answers[i] == 1:
                n_answers = n_answers + 1
        if output_condition == n_answers:
            result = 1



