#Encapsulation
## all data keep inside class is called encapsulate. it binding all data together
## after Encapsulation then work abstraction 
## Abstraction
## suppose l = [6,3,2,5,7]
## l.sort() #tim sort
## here we know  if we use sort method list will be sorted
## But we don't know how to sort method work and how it will be sort inside
## This is called abstraction . it hides compexity from the user  
### Some special Naming Convention
## _name (here underscore is a convention ) . By using naming convention
#  we say developer don't erase or edit this name or object . Because it is private
## property from instance variable .Convention of private name.
## __name__ # it called double underscroe or dunder/magic methods

## Naming Mangling
### __name ( it is not a convention) 



class Phone:

    def __init__(self,brand_name,model_name,price):
        self.brand_name = brand_name
        self.model_name = model_name
        # self.price = price
        # self._price = price  ## _private is naming convention
        # self._name  = name ## _name is naming convention
        self.__price = price ## __name , it is naming mangling

    def make_a_phone_call(self,phone_number):
        return (f"calling {phone_number}...")

    def full_name(self):
        return f"{self.brand_name} {self.model_name}"


phone1 = Phone('Nokia', '1100', 2000)
# print(phone1._price) ## we can also change private name like _price

# phone1._price = -2000
# print(phone1._price) ## it will change

# print(phone1.__price) # Now it will not working because it shows
## _Phone__price cause it is public naming & python
# change it names. we can see it by using __dict__
print(phone1.__dict__)

## Now this error will be solved to use _Phone__price  this
print(phone1._Phone__price) ## Now it will work

phone1._Phone__price = -2000 ## it will changeable cause it is public 
print(phone1._Phone__price) ## Now it will showing -200 .


