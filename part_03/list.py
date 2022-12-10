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

'''

## List inside list

# matrix = [[1,2,3],[5,6,7],[7,8,9]]

# for sublist in matrix:
#     # print(matrix)
#     for i in sublist:
#         print(i)




