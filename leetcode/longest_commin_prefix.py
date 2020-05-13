"""Write a function to find the longest common prefix string
 amongst an array of strings.If there is no common prefix, 
 return an empty string ""."""

 
 
def common_prefix(array):
    if not array:
            return ""
    min_ = min(array)
    max_ = max(array)
    if not min_:
        return ""
    for i in range(len(min_)):
        if max_[i] != min_[i]:
            return max_[:i]
    return min_[:]

array = ["flower", "florist","floral", "fleet"]
print(common_prefix(array))
    