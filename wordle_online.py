#===========================================================================================================================
"""
Name                : Srivenkat A
File Name           : wordle_online.py
"""
#===========================================================================================================================
import numpy as np 
from src.genie import *
from src.webdriver import *

def check_overlap(word):
    #should interface with website else get input from user
    overlap = input("\nEnter the overlap as a string: ")
    overlap = [int(i) for i in overlap]
    return overlap

#Get word list
word_list = get_corpus()

pred_words = ['crane']
absent = []

while (word_list != []):
    word = pred_words[-1]
    print('\n' + str(len(pred_words)) + '. ' + word)

    overlap = check_overlap(word)
    if (overlap == (2*np.ones(5)).tolist()):
        print ("\nTarget Achieved \n")
        exit()

    progress, pred_letters, absent = prediction(word, overlap, absent)
    word_list = prob_words(progress, pred_letters, absent, word_list)
    if (word in word_list):
        word_list.remove(word)

    pred_word = word_list[0]
    pred_words.append(pred_word)

