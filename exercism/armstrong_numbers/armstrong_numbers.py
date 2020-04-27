"""
Exercism.io coding problems

An Armstrong number is a number that is the sum 
of its own digits each raised to the power of the number of digits
Write some code to determine whether a number is an Armstrong number.

reasonable test input: 9(since we know it is an armstrong number), 100,5,8

Psuedocode: The number we are testing will be passed as an argument
We need to first check the number of digits the num has, and loop through 
each digit putting it to the power of the num digits, 
getting the sum of these numbers
finally, checking to see if the original number equals the calculated number
 """

def is_armstrong_number(num):
    num = str(num)
    length = len(num)
    sum = 0 
    for digit in num:
        sum += int(digit) ** length
    if str(sum) == num:
        return True
    else:
        return False
        
   
        
    
    
        
if __name__ == "__main__":
    #good test input
    print(is_armstrong_number(9))
    #good test input
    print(is_armstrong_number(150))
    print(is_armstrong_number(150))
    #edge case tried number too big
    #edge case tried decimal 
 
   