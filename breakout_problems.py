#Given a string of text and a number k, 
# find the k words in the given text that appear most frequently. 
# Return the words in a new array sorted in decreasing order. ”


def findHighFrequencyWords (ls_words, k):
	#spit
	ls_words 

	#create a dictionary storing the frequency of words
	dict = {}
    for word in ls_words:
		if word is not dict:
			dict[word] = 1
		else:
			dict[word] +=1
	
	#store a list of the high freq elements as a tuple checking k length of list
    ls_sorted = [ (‘a’,0) ]
        for key,value in zip(dict.keys(),dict.values()):
            if value > ls_sorted[0][1]:
                if len(ls_sorted) = k:
                    ls_sorted.pop(0)
                ls_sorted.append( (key,value) )
                ls_sorted.sort() #sort by index [1], don’t know the syntax

    #sort them in decreasing order, then output only the words
    ls_sorted[::-1]
    ls_outputText = “”
    for word in ls_sorted:
        ls_outputText += word[0]
    return ls_outputText

print(findHighFrequencyWords("Red fish blue fish one fish two fish",3))

		