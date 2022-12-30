'''
### Special magic methods/dunder methods (__init__) before and after double underscore
## is called dunder/magic methods
### operator overloading
## Polymorphism means many form .method overloading is also polymorphism
## suppose add method we can add two string or two integer to use one add method
### __str__,__repr__,__len__ these are dunder/special magic methods

class Phone:

    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = price

    def phone_name(self):
        return f"{self.brand} {self.model_name}"

    def __str__(self): ## it is nicely formated string.
        ## it is use normal user
        return f"{self.brand} {self.model_name}"    

    def __repr__(self): ## repr represent complete code  . I mean has created in repr .
        ## it is use developer so that developer can debugging ,bugging
        # return f"{self.brand} {self.model_name} and price is {self._price}"
        return f'Phone(\'{self.brand}\',\'{self.model_name}\',\'{self._price}\')'
        ## it will return object

    def __len__(self): ## it is use to return len
        return len(self.phone_name())  

    def __add__(self,other):
         return self._price + other._price  

    def __mul__(self,other):
        return self._price * other._price
    def __divison__(self,other):
        return self._price / other._price   

class SmartPhone(Phone):
    def __init__(self, brand, model_name, price,memory,ram):
        super().__init__(brand, model_name, price)
        self.memory = memory
        self.ram = ram

    def __len__(self):
        return self._price    



phone1 = Phone('Nokia', '1100', 2000)
phone2 = Phone('Symphony', '21s', 3000)

print(phone1 + phone2) ## here we can use operator overloading(like add dunder)
## to avoid error.
print(phone1*phone2)
print(phone1/phone2)


# print(str(phone1))
# print(repr(phone1))

# print(phone1)
# print(phone1.__repr__()) ## it will print like object 


print(len(phone1)) ## here by using len method we can get phone1 object len
print(len(phone2)) ### & aslo get phone2 object len .This is Polymorphism 

'''

class Phone:

    def assign_color(self,color):
        self.color = color
    def assign_cost(self,cost):
        self.cost = cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost

p1 = Phone()
p1.assign_color('red')
print(p1.show_color())
