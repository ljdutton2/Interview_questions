"""Write a function to find the longest common prefix string
 amongst an array of strings.If there is no common prefix, 
 return an empty string ""."""

 #the time complexity of this is O(1) because no matter how large
 #the data set, as long as the array is sorted we only need to
 #compare the largest and the smallest string



def common_prefix(array):
    if not array:
            return ""
    min_ = min(array)
    max_ = max(array)
    array = array.sort()
    if not min_:
        return ""
    for i in range(len(min_)):
        if max_[i] != min_[i]:
            return max_[:i]
    return min_[:]

array = ["flower", "florist","floral", "fleet", "find"]
print(common_prefix(array))
    