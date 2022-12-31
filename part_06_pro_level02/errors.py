
"""
### build-in errors
### exception , how to handle them
## raise your own errors , debugging etc


### Syntax error
def func: ## Here is syntax error
    print('bangla')

name = 'MohammadIshak'* ## Here is also syntax error

### Indentation error

def Car():
    print('hello car')
  print('bangla) ## Spaces related error is indentation error


#### Name error 

print(bangla) ### when name or anything is not defined then it is called name error

### Type error 

print(124+'bangla') here integer value cannot addition with string value. it is called
type error . When we type wrong operation in wrong function.


### Index error

a = [2,3,4,5]
print(a[5]) ## here index is not exist in the list a 


### Value error

s = 'bangladesh'
print(int(s)) ### Value is string it would be value error 

### attribute error 

when any method or anything has not exist then it is called attribute error

l = [1,2,3]
print(l.push('322')) ## python has no push methods .

### Key error (in dictionary)

phone = {'color':'red','brand':'samsung','price':90000 }

print(phone('model')) ## here phone has no model key . so it is key error


### Raise error
def add(a,b):
    if type(a) is int and type(b) is int:
        return a+b
    
    raise TypeError('OOPs you are passing wrong data type to the function')  

print(add(2, 'bangla')) 



#Raise errors example_01
### NotImplementedError
# Abstract method

class Animal:

    def __init__(self,name):
        self.name = name

    def sound(self):
        raise NotImplementedError('You have to define this method in subclasses')

class Dog(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.name = name
    def sound(self):
        return "ghew ghew"    

class Cat(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed = breed 
    def sound(self):
        return "Meou Meou"  


dogg = Dog('pet', 'giant')
catt  = Cat('cats', 'nel')

"""
