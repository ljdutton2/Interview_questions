"""
The Collatz Conjecture or 3x+1 problem can be summarized as follows:
Take any positive integer n. If n is even, divide n by 2 to get n / 2. 
If n is odd, multiply n by 3 and add 1 to get 3n + 1. Repeat the process indefinitely.
 The conjecture states that no matter which number you start with, you will always reach 1 eventually.
Given a number n, return the number of steps required to reach 1.

check if even or odd to begin with
set counter to count iterations
if even divide by 2 until 1 is reached
if odd multiply 3 and add 1 until 1 is reached


"""
from prettytable import PrettyTable

def collatz_conjecture(num):
    counter = 0
    while num > 1:
        if (num % 2):
            num = 3*num+1
        else:
           num=num//2
        counter += 1
    return counter

variable_table = PrettyTable()
variable_table.field_names = ["Variable",  "Value"]
variable_table.add_row(["counter", 0])
variable_table.add_row(["num", 12])
variable_table.add_row(["counter", 9])

print(variable_table)



