### We will discuss three problem existing 
## then we will solve them using setter ,setter deocorder


class Phone:

    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
       
        # if price>0 :
        #     self._price = price
        # else:
        #     self._price = 0  
        self._price = max(price, 0) ## it is the good method than previous one

      # self.complete_specification = f"{self.brand} {self.model_name} and {self._price}
      #  " 
    @property  ## instead of getter() method we use in python @property
    def complete_specification(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"

    @property
    def price(self):
        return self._price ## Now we need not write phone1._price to print
        ## we can write prin(phone1.price) 

    @price.setter
    def price(self,new_price):  ## to avoid negative value set by anyone ,first 
        ## we have to write @property method what we above set .after that
        ## we have to set @price.setter 
        self._price = max(new_price, 0) 

    def make_a_phone(self,phone_number):
        return f"calling {phone_number}..."  

    def full_name(self):
        return f"{self.brand} {self.model_name}"


phone1 = Phone('Apple', 'iphone14 pro', 123000)
phone2 = Phone('Oppo', 's21', 30000)

print(phone1.brand)
print(phone1.model_name)
# phone1._price = -5000 ### Price never will be negative . if we want no user put
## negative ever , we need to setter() method 
# print(phone1._price)
phone1._price = 10000 ## here price will be changed 
## Now here if given negative value it will set 0
# print(phone1._price)

print(phone1.price)
print(phone1.full_name())
# print(phone1.complete_specification) ## But here price will be not changed it will
## remain previous price . That's a problem . if solve this in the function of max set
## But has also exist another problem to update price . If solve this proble 
## we have to define a function about complete specification

# print(phone1.complete_specification())
##### by using property decorder we need not express function as function 
## we need not write () parenthesis to express .
## we can easily express it as attribute
print(phone1.complete_specification) ## like as
