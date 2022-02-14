#===========================================================================================================================
"""
Name                : Srivenkat A
File Name           : wordle_local.py
"""
#===========================================================================================================================
import numpy as np 

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
            # check for repeat letters, but only 1 present in correct word
            flag = 0
            for j in range(5):
                if word[j] == target[j] && word[j] == target[j]:
                    flag = 1
                    overlap.append(0)
                    break
            if flag == 0:
                overlap.append(1)
        else:
            overlap.append(0)
    return overlap

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


#Extract corpus from dictionary
dict_name = 'words_beta.txt'
dict_file = open('./dictionaries/'+dict_name,'r')
corpus = [word.replace('\n','') for word in dict_file.readlines()]
dict_file.close()

#Get target word as user input
target = input('Enter Wordle target word: \n')
if (target not in corpus):
    print('Target word not in dictionary \n')
    exit()

word_list = corpus
pred_words = ['crane']
absent = []

while (word_list != []):
    word = pred_words[-1]
    print(word + '\n')
    if (word == target):
        print ("Target Achieved \n")
        exit()

    overlap = check_overlap(word, target)
    progress, pred_letters, absent = prediction(word, overlap, absent)
    word_list = prob_words(progress, pred_letters, absent, word_list)
    if (word in word_list):
        word_list.remove(word)

    pred_words.append(word_list[0])

