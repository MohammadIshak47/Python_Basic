
'''


# def square(*a):
#     return a**2

# print(square(4))

####  pass function as a argument 

# def square(a):
#     return a**2


# l = [1,2,3,4,5]
# print(list(map(square, l)))

## custom function
l = [1,2,3,4]
def square_define(func,l):
    new_list = []
    for item in l:
        new_list.append(func(item))
    return new_list

print(square_define(lambda a : a**2,l))

print( [i for i in range(1,6) if i**2])

### Decorators intro :
### Decorators __ Enhance the functionality of other functions

def decorators_function(any_function):
    def wrapper_function():
        print("This is awesome function")
        return any_function()
    return wrapper_function

@decorators_function ## This is shortcut ## here first called
# decoratores functin ar this is awesome function
## @ use for decorators . this is also called sugar function
def func1():
    print("This is function 1")

@decorators_function
def func2():
    print("This is function 2")

# func1 = decorators_function(func1)
func1() ## when I called func1 then first it will print my decoratores_function
## along with func1
func2()


## Drawback findout and solution


def decoratores_func(any_function):
    def wrapper_function(*args,**kwargs):
        print("This is fantastic function")
        return any_function(*args,**kwargs) ## we have to must return this function
    return wrapper_function

@decoratores_func
def func(a):
    print(f"This is  func with argument {a}")
    
@decoratores_func
def add(a,b):
    return a+b 

print(add(2,3))       


from functools import wraps # To solve this problem we have to import and write
## below function 
def decoratores_func(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        ''This is wrapper function''
        print("This is awesome function")
        any_function(*args,**kwargs)
    return wrapper_function


@decoratores_func
def add(a,b):
    ''This is add function''
    return a+b

print(add(2, 3))

print(add.__doc__) ## it shows some errors . To solve this problem
print(add.__name__)

#### problem: 
## @ print function data
## this function takes two numbers as argument and return their sum
## output  you are calling add function 
## output this function takes two numbers as parameters and return their sum 
## output 9

## solution 
from functools import wraps
def decoratores_fun(function):
    @wraps(function)
    def wrapper_function(*args,**kwargs):
        print(f"You are calling {function.__name__}")
        print(f"{function.__doc__}")
        return function(*args,**kwargs)
    return wrapper_function

@decoratores_fun
def add_function(a,b):
    'this function takes two numbers as parameters and return their sum '
    return a+b

print(add_function(4, 5))    


## problem_02: coding run time count problem

# import time

# t1 = time.time()

# x = input("Enter any value  : ")
# if  x==5 :
#     print("X is equal to 5")
# else:
#     print("x is not equal to 5 ")   
# t2 = time.time()
# print(t2-t1)     

### Execution run time count

from functools import wraps
import time

def calculate_time(function):
    @wraps(function)
    def wrapper_function(*args,**kwargs):
        print(f"Execution  func name is {function.__name__}")
        t1 = time.time()
        returned_value = function(*args,**kwargs) ## I do not return here because
        # if I return this then it will jump out of run time & we can't calculate
        #  run time .That's why I have taken this into returned_value .
        t2 = time.time()
        total_time = t2 - t1
        print(f"This function took  {total_time} seconds")
        return returned_value
    return wrapper_function

@calculate_time
def square_finder(n):
    return ([i**2 for i in range(1,n+1)])

square_finder(1000)
'''








