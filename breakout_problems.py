#Given a string of text and a number k, 
# find the k words in the given text that appear most frequently. 
# Return the words in a new array sorted in decreasing order. ”


def findHighFrequencyWords (l_words, k):
	#spit
	l_words 

	#create a dictionary storing the frequency of words
	dict = {}
    for word in l_words:
		if word is not dict:
			dict[word] = 1
		ele:
			dict[word] +=1
	#store a list of the high freq elements as a tuple checking k length of list
    l_sorted = [ (‘a’,0) ]
        for key,value in zip(dict.keys(),dict.values()):
            if value > l_sorted[0][1]:
                if len(l_sorted) = k:
                    l_sorted.pop(0)
                l_sorted.append( (key,value) )
                l_sorted.sort()
    #sort them in decreasing order, then output only the words
    l_sorted[::-1]
    l_outputText = “”
    for word in l_sorted:
        l_outputText += word[0]
    return l_outputText

print(findHighFrequencyWords("Red fish blue fish one fish two fish",3))



#Given a list of n numbers, determine if it contains any duplicate numbers

def find_duplicate(arr):
    arr.sort()
    last = 0
    for i in arr:
        if last == arr[i]:
            return arr[i]
        last = arr[i]

if __name__ == '__main__':
    arr = [6,1,3,4,6,7,9]
    #1346679
    print(find_duplicate(arr))

		