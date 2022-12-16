'''
## make flexible fuctions
# *operator
# *args

## Summation two numbers
def sum_all(*args):
    total = 0
    for num in args:
        total+=num
    return total

print(sum_all(20,12,14))

## *args with normal parameter

# def multiply_all(*args):
def multiply_all(num,*args): ## here if we enter normal parameter (num),then *args will
    total = 1                 # take all value except first value
    for i in args:
        total*=i
    return total

print(multiply_all(2,3,4,3))


#### args as argument

def multiply_all(*args):
    total = 1
    for i in args:
        total*=i
    return total

list1 = [2,3,4] 
# print(multiply_all(list1)) ## it will multiply the list but not with the elements of list
print(multiply_all(*list1)) # now it will unpack & multiply the elements of list


## problem : define a function . Input num,iterable(tuple,list) containing numbers as args
## Example :  nums = [1,2,3]
## to_power(3,*nums)
## output : list --[1**3,8,27]
## if user didn't pass any args then give a user message 'hey you didn't pass args
### else return list

### Solution

def to_power(num,*args):
    if args:
        return [i**num for i in args]
    else:
        return 'You didn\'t pass any args'    
        
nums = [1,2,3]
# print(to_power(4,*nums))
print(to_power(3,*[1,2,4]))



##### kwargs arguments
## **kwargs(double star argument)
## kwargs as a parameter

def func(**kwargs): ## it contains value as a dictionary
    # print(kwargs)
    for k,v in kwargs.items():
        print(f"{k} : {v}")

print(func(first_name = 'Mohammad',last_name = 'Ishak'))

'''

## kwargs as a normal parameter

def func(name,**kwargs):
    for k,v in kwargs.items():
        print(f"{k} : {v}")

# print(func('Ishak',sur_name ='Ishak',full_name='Mohammad Ishak'))

## Dictionary unpacking 
d = {'name':'Muhammad Ishak','age':26}
func(**d)