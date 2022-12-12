'''
# a = ['Dhaka','Barisal','Rajshahi','Sylhet','Chittagong']
# a = [1,2,3,"ISHAK",'Dhaka',3.44,'num1']
# print(a)
# print(a[3])
# print(a[:3])
# print(a[3:])
# print(a[2:4])
# print(a[:-1])
# print(a[-1:0])

# a[2] = "red"
# a[2:]  = ['yellow','black','white','green'] # to change value
# print(a)

## Add Data into the list

# a = ['apple','mango','banana'] # it append in last of the list
# a.append('orange')
# a = []
# a.append('apple')
# a.append('banana')
# print(a)

## insert method

a = ['dhaka','bhola','pabna']
# # a.insert(1,'cumilla')
# b = ['banana','orange']
# # print(a+b)
# # a.extend(b)
# a.append(b) # it will insert one list into another list that's why we use extend method
# print(a)

## pop method 

# a.pop() # it will remove last element from the list
# print(a)
# del a[0]
# a.remove('bhola')
# print(a)
# print(a)

### To add data append, insert, extend
### To delete del, remove, pop


# in method 

a = ['green','orange','blue']

if "green" in a:
    print("Green is present of list a ")
else:
    print("Green is not present in list a") 


## count method
a = ['apple','banana','orange','mango','banana','pineapple','mango']

# print(a.count('banana'))

## sort method
a.sort() # to sort alphabetic order like a b c
numbers = [5,7,2,3,4]
print(sorted(numbers)) # number sort kora
print(a)


a = ['apple','banana','orange','mango','banana','pineapple','mango']
# a.clear() # element clear korte
# print(a)

a_copy = a.copy()
print(a_copy)

## list_comparison

## Split method 
# Convert string to list

name, age = input("Enter any name & age : ").split() # To take two variable or input into one line

print(name)
print(age)

## strings are immutable means not chanageable in python
# list are mutable means changeable in python
## Join Method
# convert list to string
user_info = ['Muhammad','33']
print(','.join(user_info)) # join two input in one line

## List in for loop

fruit = ['apple','mango','banana','orange','water melon']

for fruits in fruit:
    print(fruits)

## List inside list

matrix = [[1,2,3],[5,6,7],[7,8,9]]

# for sublist in matrix: ## When list inside list then it is called 2d list
#     # print(matrix)
#     for i in sublist:
#         print(i)

print(matrix[1][1])  


# numbsers = list(range(1,12))
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,15,14,1,13]

# numbsers.pop()
# print(numbsers.pop()) # return pop value

# print(numbsers.index(2))
# print(numbers.index[1,12])
# print(numbers.index(1,12))
# print(numbers.index(1,12,14))
def negative_value(numbers):
    negative_list=[]
    for i in numbers:
        negative_list.append(-i)
    return negative_list

print(negative_value(numbers))       



# print(numbsers)

###problem_01: return a list and squre every item
#solution :
numbers = [1,2,3,4,5]

def square_list(numbers):
    square_value_list = []
    for i in numbers:
        square_value_list.append(i**2)
    return square_value_list

print(square_list(numbers))

## problem_02 : Define a function which will take list as an argument & this function
# will return reversed list

#Solution :

numbers = [1,2,3,4,5,6,7,8]

def reverse_list(numbers):
    numbers.reverse()
    return numbers
print(reverse_list(numbers))   

alternative way :
numbers = [1,2,3,4,5,6,7,8]
def reverse_list(numbers):
    return numbers[::-1]

print(reverse_list(numbers))


## another way: user pop & append method
#    

def reverse_list(numbers):
    reverse_item= []
    for i in range(1,len(numbers)+1):
        popped_list = numbers.pop()
        reverse_item.append(popped_list)
    return reverse_item
numbers = [1,2,3,4,5,6,7]
print(reverse_list(numbers))


## problem_03 : define a function that takes a words of agrument and return list
# with reverse of every element in that list.

def reverse_every_element(l):
    reverse_list = []
    for i in l:
        reverse_list.append(i[::-1])
    return reverse_list

list_numbers = ["Dhaka","Khulna","Barisal","Cumilla"]
print(reverse_every_element(list_numbers))



## problem_04 : filter odd_even
# define a function
# list input : [1,2,3,4,5,6,7]
# list ouput : [[1,3,5,7],[2,4,6]]

# Solution :

def filter_odd_even(list_number):
    odd_num = []
    even_num = []
    for i in list_number:
        if i%2 == 0:
            even_num.append(i)
        else:
            odd_num.append(i)
    output = [odd_num,even_num] 
    return output     


list_number = [1,2,3,4,5,6,7]
print(filter_odd_even(list_number)) 


'''

## problem_05: Common elements finder function
# define a function which take 2 lists as input and return a list
#which contains common elements of both list

# Example:
# input [1,2,5,7],[1,2,3,6,9]
# output [1,2]
# Solution : 

def common_item(list1,list2):
    output = []
    for i in list1:
        if i in list2:
            output.append(i)
    return output        



print(common_item([1,2,5,6],[1,2,3,9]))



         














