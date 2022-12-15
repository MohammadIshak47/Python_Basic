'''
## with the help of list comprehension ,we can create list in one line

## Create a list of squres from 1 to 10

# squares = []

# for i in range(1,11):
#     squares.append(i**2)
# print(squares) 

###   in List Comprehension
# square2 = ([i**2 for i in range(1,11)])
# print(square2)
# print([i**2 for i in range(1,11)]) 


# a = []
# for i in range(1,11):
#     a.append(-i)
# print(a)    

###   in List Comprehension
# print([-i for i in range(1,11)])


names = ['Ishak','Irfan','Anas']

# list = []

# for name in names:
#     list.append(name[0])
# print(list)    

###  in List Comprehension

print([name[0] for name in names])

## Problem : Define a function that take list of strings
## list containing reverse of every strings
## Note using list comprehension 
# using normal method
#Example : list = ['abc','def','ijk]
## reverse strings will be ['cbc','fed','kji']

## Solution
def reverse_strings(list1):
    new_list = []
    for name in list1:
        new_list.append(name[::-1]) 
    return new_list

print(reverse_strings(['bangla','english','science']))

## In list comprehension   

def reverse_function(list1):
    return [name[::-1] for name in list1]

print(reverse_function(['bangla','english','math','scienc'])) 


'''

#### List comprehension with if else statement




