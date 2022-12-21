## Advance min max function uses

# a = [2,3,88,44,22]
# print(max(a))

### Findout maximum  and minimum item of string

# def max_finder(Item):
#     return len(Item)
# names = ['Mohammad','Ishak','toy','nest']
# print(max(names, key=max_finder))
# print(min(names, key=max_finder))

### Findout maximum  and minimum item of string using lambda
# names = ['Mohammad Irfan','Ishak','toy','nest']
# # print(max(names, key=lambda  names:  len(names)))
# print(min(names, key=lambda Item: len(Item)))

### in dictionary findout max value or item or list using lambda

student1= [
    {'name':'Mohammad Ishak' , 'score':93,'age':25},
    {'name':'Irfan','score':91,'age':22},
    {'name':'Rasel','score':88,'age':27}

    
]

# print(max(student1, key = lambda item: item.get('score')))
print(max(student1, key=lambda item:item.get('age')))