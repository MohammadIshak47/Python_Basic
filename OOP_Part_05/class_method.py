'''
## Class method
## difference between class methods and instance methods

class Person:
    count_instance = 0 ## class variable or class attribute 

    def __init__(self,first_name,last_name,gender,age):
        Person.count_instance+=1
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
    @classmethod
    def count_instance_num(cls): # here we write cls because class is already defined
        return f"You have created {cls.count_instance} instances of {cls.__name__} class" ## or 
        ## we can write Person class . Person is our class name   


p1 = Person('Muhammad', 'Ishak', 'Male', 26) ##1
p2 = Person('Muhammad', 'Faisal', 'Male', 14) ##2 
p3 = Person('Muhammad', 'Rasel', 'Male', 16) ## 3

# print(Person.count_instance) ## Here it will show 3 instance
print(Person.count_instance_num())
# print(p1.count_instance_num()) ## Here we can write object name .but it is not good 
## here to write object name



## class method as a constructor
## to define as myself First I have to create construnctor for my own

class Person:
    count_instance = 0 ## class variable or class attribute 

    def __init__(self,first_name,last_name,gender,age):
        Person.count_instance+=1
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
    @classmethod
    def from_string(cls,string):
        first_name,last_name,gender,age = string.split(',') 
        return cls(first_name,last_name,gender,age) ### Here created our own instance

    @classmethod
    def count_instance_num(cls): # here we write cls because class is already defined
        return f"You have created {cls.count_instance} instances of {cls.__name__} class" ## or 
        ## we can write Person class . Person is our class name   


p1 = Person('Muhammad', 'Ishak', 'Male', 26) ##1
p2 = Person('Muhammad', 'Faisal', 'Male', 14) ##2 
p3 = Person('Muhammad', 'Rasel', 'Male', 16) ## 3


# print(Person.count_instance_num())

p4 = Person.from_string('Md','Ishak','Male',23)
print(p4)
print(p4.count_instance_num()) ## here we can any object 




'''

## static method use as a normal function . It is not related class or object
## staic method has logical connection with class

class Person:
    count_instance = 0 ## class variable or class attribute 

    def __init__(self,first_name,last_name,gender,age):
        Person.count_instance+=1
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
    @classmethod
    def from_string(cls,string):
        first_name,last_name,gender,age = string.split(',') 
        return cls(first_name,last_name,gender,age) ### Here created our own instance

    @staticmethod
    def hello():
        print('hello, static method called')



p1 = Person('Muhammad', 'Ishak', 'Male', 26) ##1
p2 = Person('Muhammad', 'Faisal', 'Male', 14) ##2 
p3 = Person('Muhammad', 'Rasel', 'Male', 16) ## 3


# print(Person.count_instance_num())

p4 = Person.from_string('Md','Ishak','Male',23)
print(p4)
print(p4.count_instance_num()) 







