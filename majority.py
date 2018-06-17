def majority_strategy(m_questions, answer_list):
    #number of answers equal to 1
    pos_answer = 0
    # number of answers equal to 0
    neg_answer = 0
    #for each element in the answers given by human assistant...
    try:
        for element in answer_list:
            #if the answer is positive, let's add 1
            if element == 1:
                pos_answer += 1
            elif element == 0:
                neg_answer += 1
            else:
                raise Exception('Error occured')
    except:
        print("Something went wrong during elaborating strategy")
    '''
    use majority strategy: item is declared to be a 1 item if it receives 
    (M+1)/2 YES responses, 0 item otherwise
    '''
    if (m_questions+1)/2 == pos_answer:
        return True
    elif (m_questions+1)/2 == neg_answer:
        return False
