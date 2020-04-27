"""
Given a phrase, count the occurrences of each word in that phrase.

Reasonable Test: 
good - ("Hi my my name name name is Lauren) 
unusual- ("I am 22 years old")
edge - ("22's and 23's")

Psuedocode: First a dictionary to hold the words and their occurences 
then seperate the phrase by the words


"""
def word_count(phrase):
    count = 1
    for i in range(len(phrase)):
        if (phrase[i] == ' '):
            count +=1
    return count

def count_words(phrase):
    word_counts = {}
    words = phrase.split()
    for word in words:
        if word in word_counts.keys():
            word_counts[word] = word_counts[word] + 1
        else:
            word_counts[word] = 1
    return word_counts



#normal tests
print(count_words("Hi my my name name name is Lauren"))
print(count_words("red fish blue fish two fish something"))
#unusal tests
print(count_words("22's and 23's"))
print(count_words("22's and 23's"))
#edge cases
print(count_words("000 111 222"))
print(count_words("!!!! ???? ***"))

