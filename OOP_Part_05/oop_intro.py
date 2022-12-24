'''
### class
## object
## init method is also know as constructor
## What are attributes , what are instance variables
## How to create object

class Person: ## We create class because we want to create our own object by using class
    ### here __init_ is a construtor
    def __init__(self,first_name,last_name,age): ## here first_name,last_name,age
        ## are attributes. We can write person_instance or anything instead of self
        ## but according to convention we have to write here self
        self.first_name = first_name ## self.first_name is an instance variable
        self.last_name = last_name ## we can write person_last_name  = last_name 
        ## we can change instance variable. We don't need to left and right are equal
        # variable . but according to convention should write same. 
        self.age = age


p1 = Person('Muhammad', 'Ishak', 26) ## here self is replaced by p1  & p1 is an object
p2 = Person('Irfan', 'Ahmed', 4) ## when we create object then init method is called

print(p1.first_name,p1.last_name)


'''

## problem_01 : create a laptop class with attributes like brand, model, price
## create two object/instance of your laptop class (instance are known as object)

## Solution

class Laptop:
    def  __init__(self,brand_name,model_name, price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand_name + '' + model_name + '' + str(price)


lap1 = Laptop('Macbook ', '32v ', 114000)
lap2 = Laptop('Asus', 'a432', 85000)

# print(lap1.brand_name,lap1.model_name,lap1.price)
# print(lap2.brand_name,lap2.model_name,lap2.price)

print(lap1.laptop_name)

