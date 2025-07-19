#Lists and Dictionaries with For Loops, List Comprehension, and Dictionary Comprehension
#1. Sum of all numbers in a list
numbers = [10,20,30,40,50,60]
total = 0
for num in numbers:
    previous_total = total
    total += num
    print(f"{num}+{previous_total} : {total}")
    
    
