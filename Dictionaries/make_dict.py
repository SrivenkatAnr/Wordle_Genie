import fileinput
alpha5 = open('words_alpha5.txt','w+')

for word in fileinput.FileInput('words_alpha.txt'):
    if len(word)==6:
        alpha5.write(word)
