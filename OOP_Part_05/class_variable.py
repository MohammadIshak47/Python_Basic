'''

### What is class variable 
## What is instance variable
## Instance variable always unique

class Circle:
    pi = 3.1416 ## Here pi is class variable because variable is inside class
    ## then it is called class variable

    # def __init__(self,pi,radius):
    def __init__(self,r):
        self.r = r

    def circle_circumference(self):
        return 2*Circle.pi*self.r


# c1 = Circle(3.1416, 3) ## Here We can see that two problems . one is we have 
## to declare pi value repeatly . Two , as a result memory storage need fill up 
## and memory waste and need more space to execution pi value repeatly . 
# To solve this we can
## use Class variable
# c2 = Circle(3.1416, 4)
c1 = Circle(2)
c2 = Circle(3)
print(c1.circle_circumference())

### Discount findout 
class Laptop:

    discount_percent = 10 ## We can use it when every product discount is same

    def __init__(self,brand_name,model_name,price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price

    def apply_discount(self):

        offer_price = (Laptop.discount_percent/100)*self.price
        return self.price - offer_price


l1 = Laptop('Apple', 'Macbook Pro', 120000)
l2 = Laptop('Dell', 'A200', 90000)

# print(l1.apply_discount())
print(l2.apply_discount())

### if every product has different discount offer .How we solve it?
## solution
class Laptop:

    discount_percent = 10 ## We can use it when every product discount is same.
    ## When different product has different discount . How can we solve it?

    def __init__(self,brand_name,model_name,price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price

    def apply_discount(self):

        offer_price = (self.discount_percent/100)*self.price
        ### Here first it will looking for class variable a . If not then it will
        ## looking for object variable . it found it then it will take it . Here 
        ## self discount_percent is object variable . so it will took it and class
        ## variable Laptop.discount_percent replaced by object variable self.discount_pecent
        return self.price - offer_price


l1 = Laptop('Apple', 'Macbook Pro', 120000)
l2 = Laptop('Dell', 'A200', 90000)

# print(l1.apply_discount())
# print(l2.apply_discount())
print(l1.__dict__) ## by using dict method we can show laptop full specificatin
## dictionary order to dict
l1.discount_percent == 50 ## here it will print object variable not class varibale discount

print(l1.apply_discount())


'''

### problem : object/ instance count in a class

class Person:
    count_instance = 0

    def __init__(self,first_name,last_name,gender,age):
        Person.count_instance+=1
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age


p1 = Person('Muhammad', 'Ishak', 'Male', 26) ##1
p2 = Person('Muhammad', 'Faisal', 'Male', 14) ##2 
p3 = Person('Muhammad', 'Rasel', 'Male', 16) ## 3

print(Person.count_instance) ## Here it will show 3 instance





