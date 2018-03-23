

def condProb(type, pos, word_cts, t_data):
    '''
    prob_TandP = word_cts[type][pos] / len(t_data)
    count = 0
    for item in t_data:
        if type in item:
            count += 1
    prob_T = count / len(t_data)
    print("\n", prob_TandP, prob_T, prob_TandP / prob_T, "\n")
    '''
    p_t = word_cts[type][pos]
    p_b = 0
    for key in word_cts.keys():
        p_b += word_cts[key][pos]
    return(p_t / p_b)