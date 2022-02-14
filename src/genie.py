#===========================================================================================================================
"""
Name                : Srivenkat A
File Name           : genie.py
"""
#===========================================================================================================================
import numpy as np 

def get_corpus():
    #Extract corpus from dictionary
    dict_name = 'words_beta.txt'
    dict_file = open('./dictionaries/'+dict_name,'r')
    corpus = [word.replace('\n','') for word in dict_file.readlines()]
    dict_file.close()
    return corpus

def prediction(word, overlap, absent):
    crct_pos = np.where(np.array(overlap) == 2)[0]
    misplaced_pos = np.where(np.array(overlap) == 1)[0]
    absent_pos = np.where(np.array(overlap) == 0)[0]

    pred_word = ['_','_','_','_','_']
    if (len(crct_pos) > 0):
        for pos in crct_pos:
            pred_word[pos] = word[pos]
    pred_word = "".join(pred_word)

    pred_letters = list(set([word[i] for i in list(crct_pos)+list(misplaced_pos)]))

    absent_letters = [word[i] for i in absent_pos]
    absent = list(set(absent+absent_letters))

    return pred_word, pred_letters, absent

def prob_words(progress, pred_letters, absent, word_list):
    prob_words = []
    for word in word_list:
        flag=1
        for letter in pred_letters:
            if letter not in word:
                flag = 0
        for letter in word:
            if letter in absent:
                flag = 0
        for i in range(5):
            if (progress[i] != '_') and (word[i] != progress[i]):
                flag = 0
        if (flag == 1):
            prob_words.append(word)
    return prob_words