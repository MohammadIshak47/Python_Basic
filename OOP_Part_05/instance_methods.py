'''
## Instance methods 
### we know that instance is known as object
## what is exist inside class we called method
## method is what define inside class


class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self):
        return self.age>18    

p1 = Person('Faisal', 'Imtiaz', 14)
p2 = Person('Rasel', 'Ahmed', 19)

# print(p1.full_name())

# print(Person.full_name(p2)) ## if not write self , 
# then it written beside the rules . In background it will run above rules
### That's why we have write self to decrease complexity
# print(p2.full_name())

# print(p1.is_above_18()) ## return False age is below 18
print(p2.is_above_18()) ## return True


'''

## Findout discount of any products

class Laptop:

    # discount = 0

    def __init__(self,brand_name,model_name,price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price

    def full_name(self):
        return f"{self.brand_name} {self.model_name}"
    def is_above_18(self):
        return self.age>18

    def apply_discount(self,num):
        offer_price = (num/100)*self.price
        return self.price - offer_price





l1 = Laptop('Apple','Macbook Pro', 120000)
l2 = Laptop('Lenovo', 'ProVersion', 80000)

print(l1.apply_discount(20)) ## discount percent 20
print(l2.apply_discount(10)) ### discount percent 10