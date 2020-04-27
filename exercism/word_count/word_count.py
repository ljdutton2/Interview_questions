"""
Given a phrase, count the occurrences of each word in that phrase.

Reasonable Test: 
good - ("Hi my name is Lauren) 
unusual- ("I am 22 years old")
edge - ("22's and 23's")

Psuedocode: We can either use pythons built in .split() to seperate the words,
or we can count by the spaces. Assuming we aren't allowed to use built in in
this case I will split by spaces. 
"""
def count_words(phrase):
    count = 1
    for i in range(len(phrase)):
        if (phrase[i] == ' '):
            count +=1
    return count


print(count_words("Hi my name is Lauren"))
print(count_words("I am 22 years old"))
print(count_words("22's and 23's"))
