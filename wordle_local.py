#===========================================================================================================================
"""
Name                : Srivenkat A
File Name           : wordle_local.py
"""
#===========================================================================================================================
import numpy as np 
from src.genie import *

"""
val=0: not present 
val=1: present but in wrog position
val=2: correctly positioned
"""
def check_overlap(word, target):
    target = list(target)
    word = list(word)
    overlap = []
    for i in range(5):
        if (word[i] == target[i]):
            overlap.append(2)
        elif (word[i] in target):
            overlap.append(1)
        else:
            overlap.append(0)
    return overlap

#Get word list
corpus = get_corpus()

#Get target word as user input
target = input('Enter Wordle target word: ')
if (target not in corpus):
    print('Target word not in dictionary \n')
    exit()

word_list = corpus
pred_words = ['crane']
absent = []

while (word_list != []):
    word = pred_words[-1]
    print('\n' + str(len(pred_words)) + '. ' + word)
    if (word == target):
        print ("\nTarget Achieved \n")
        exit()

    overlap = check_overlap(word, target)
    progress, pred_letters, absent = prediction(word, overlap, absent)
    word_list = prob_words(progress, pred_letters, absent, word_list)
    if (word in word_list):
        word_list.remove(word)

    pred_words.append(word_list[0])

