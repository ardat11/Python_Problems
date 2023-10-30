#The given program declares a list of words.

#Task
#Create a program to take a letter as input and output all the words in the list that have that letter.

#Input Example
#h

#Output Example
#home
#happiness

words = ["cat", "car", "code", "home", "learn", "fun", "job", "love", "friend", "zoo", "enjoy", "happiness", "family", "goal", "desire"]

letter = input()

for word in words:
    if letter in word:
        print(word)
