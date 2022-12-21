
### Map function 

# list1 =  [2,3,4,5,6]

# def square(list1):
#     return list1**2

# print(list(map(square, list1)))

### another way(using lambda)
num =  [2,3,4,5,6]
print(list(map(lambda a : a**2, num)))

## using list comprehension
print([i**2 for i in range(2,7)])

### without list comprehension
def square(num):
    return num**2
new_list = []
for number in num:
    new_list.append(square(number))

print(new_list)


###  findout list items length 

list1 = ['bangladesh','pakistan','nepal','bhutan']
print(list(map(len, list1)))


