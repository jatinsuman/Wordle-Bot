from collections import Counter
import numpy
import random

file = open(r"C:\Users\sumia\Downloads\sgb-words.txt", "r")
content = file.readlines()
coun = Counter()

all_words = [x.lower() for x in content]

all_words1 = all_words
all_words2 = all_words
all_words3 = all_words

guess_words = []
all_words_yel = []
all_words_gre = []
all_words_gra = []

letters = []

file.close()

for word in all_words:
    for letter in word:
        letters.append(letter.lower()) 

coun.update(letters)

del coun["\n"]
del coun["-"]
del coun["."]
del coun["'"]
del coun["/"]
del coun["1"]
del coun["3"]
del coun["2"]
del coun["0"]

keys = list(coun.keys())
values = list(coun.values())
sorted_value_index = numpy.argsort(values)
rev_sorted_coun = {keys[i]: values[i] for i in sorted_value_index}
sorted_coun =  list(dict(reversed(list(rev_sorted_coun.items()))).keys())

com_words = [x for x in all_words if sorted_coun[0] in x and sorted_coun[1] in x and\
             sorted_coun[2] in x ]

n = 0
vals = []
correct = []
n_correct = []
wrong = []
j = 0

while True:
    correct_digi = False
    if j == 0:
        print("type 'help' for help")
        guess = random.choice(com_words)
        print(guess)
    j += 1
    wurd = [x for x in guess]
    del wurd[5]
    check = input("    : ")
    if check.lower() == "help":
        print("""RULES OF WORDLE:           
                
Guess the Wordle in 6 tries.
Each guess must be a valid 5-letter word.
The color of the tiles will change to show how close your guess was to the word.
            
Example:
Guess: WEARY
    if the W tile is in green, it means that W is in the word and is in the correctrect spot.
    if it were in yellow, it means that it was correctrect, but was in the wrongng spot.
    if it is gray, it means that the letter is not part of the word.
    
    To denote the colors here: Green = 2, Yellow = 1, Gray = 0
    
    So for example WEARY --> 21001
                
    If the word is not in the word list, type in 'nw' """)
    if check.isdigit():
        if len(check) == 5:
            for char in check:
                if char == "0" or char == "1" or char == "2":
                    vals.append(char)
                else:
                    print("Input must be 0, 1, or 2. Green = 2, Yellow = 1, Gray = 0")
                if len(vals) == 5:
                    correct_digi = True
        else:
            print("Only 5 values are to be entered")
    elif check.lower() != "help" or check.lower() != "nw":
        print("Invalid input")
    if correct_digi:
        for val in vals:
            try:
                if val == "1":
                    n_correct.append((vals.index(val, n, 5), wurd[vals.index(val, n, 5)]))
                if val == "0":
                    wrong.append((vals.index(val, n, 5), wurd[vals.index(val, n, 5)]))
                if val == "2":
                    correct.append((vals.index(val, n, 5), wurd[vals.index(val, n, 5)]))
            except ValueError:
                pass
            n += 1
            if n >= 5:
                n = 0
    
    for element in wrong[:]:
        if element[1] in [x[1] for x in correct]:
            wrong.remove(element)

    for item in wrong:
        all_words_gra = [x for x in all_words1 if item[1] not in x]
        all_words1 = all_words_gra
    if len(wrong) == 0:
        all_words_gra = all_words

    for item in n_correct:
        all_words_yel = [x for x in all_words2 if item[1] not in x[item[0]] and item[1] in x]
        all_words2 = all_words_yel
    if len(n_correct) == 0:
        all_words_yel = all_words

    for item in correct:
        all_words_gre = [x for x in all_words3 if item[1] in x[item[0]]]
        all_words3 = all_words_gre
    if len(correct) == 0:
        all_words_gre = all_words
    
    guess_words = list(set(all_words_gra) & set(all_words_yel) & set(all_words_gre))
    all_words = guess_words
    
    if check.lower() == "nw":
        guess = random.choice(guess_words)
    try:
        guess = random.choice(list(guess_words))
    except:
        pass
    print(guess)

    vals.clear()