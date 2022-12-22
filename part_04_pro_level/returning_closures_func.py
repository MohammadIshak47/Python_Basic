'''

##### Function inside function ,returning function
## Inside function , function return or it is also called closures or first class function

def outer_func():
    def inner_func():
        print("Inside inner func")
    # return inner_func()
    return inner_func

def outer_func2(msg):
    def inner_func2():
        print(f"Message is {msg}")
    return inner_func2

var = outer_func2('Hi, there!')
var() ## to execute here you need to give parenthesis ()        
# var = outer_func()
# var()

'''

### returning function practice

def to_power(x):
    def calc_power(n):
        return n**x
    return calc_power


square = to_power(2)
# print(square(2))   
# print(square(4)) 
cube = to_power(3)
print(cube(5))


