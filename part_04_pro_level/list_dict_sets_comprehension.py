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


#### List comprehension with if else statement

numbers = list(range(1,11))
# list1 = []
# for i in numbers:
#     if i%2 == 0:
#         list1.append(numbers)
#print(list1)  

#### List comprehension with if else statement
#Even numbers
print([i for i in numbers if i%2==0])
print([i for i in range(1,11) if i%2==0])
## odd numbers
print([i for i in numbers if i%2!=0])
print([i for i in range(1,11) if i%2!=0])


## problem_01 : Define a function 
# num to string 
# Example : input [True,False,[21,32],30,23.2,1]
### output : [30,23.2,1]

## Solution

def num_to_string(list1):
    return [str(i) for i in list1 if type(i)==int or type(i)==float]

print(num_to_string([True,False,[21,32],30,23.2,1]))

### List comprehension with if else

# nums = [1,2,3,4,5,6,7,8,9,10]

# new_list = []

# if i in nums:
#     if i%2==0:
#         new_list.append(i*2)
#     else:
#         new_list.append(-i)

# print(new_list)

### in List comprehension with if else

print([ i*2 if (i%2 == 0) else -i for i in range(1,11)])

### Nested list comprehension 
## Example : [[1,2,3],[1,2,3],[1,2,3]]

print([[i for i in range(1,4) ] for j in range(3)])



### Dictionary Comprehension
# square : {1:1,2:4,3:9}
# print({num:num**2 for num in range(1,10)})
# print({f"square of {num} is":num**2 for num in range(1,10)})

square ={f"square of {num} is ":num**2 for num in range(1,10)}

for k,v in square.items(): ## To present items

    print(f"{k} : {v}")

### To count string in Dictionaries
string = "MohammadIshak"
print({char:string.count(char) for char in string})

## Dictionary comprehension with if else
## d = {1:'odd',2:'even'}

print({ i:('even' if i%2==0 else 'odd') for i in range(1,10) })

'''

### Sets comprehension

# print({i**2 for i in range(1,11)})
names = ['Ishak','Tamim','Irfan','Anas']
print({ name[0] for name in names})

