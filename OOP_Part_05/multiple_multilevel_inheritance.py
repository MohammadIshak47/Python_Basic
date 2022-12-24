'''
### inheritance
### multiple inheritance
#### multilevel inheritance


class Phone: ## base class/parent class

    def __init__(self,brand,model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = price

    def full_name(self): ## here full_name , make_a_call is method
        return f"{self.brand} {self.model_name}"

    def make_a_call(self,phone_number):
        return f"calling {phone_number}..." 

class SmartPhone(Phone): ## here SmartPhone class is derived class/child class
    ## it is derived Phone class all propertis

    def __init__(self,brand,model_name,price,memory,internal_camera): ## every phone
        ## has brand,model_name,price and extra we add above specification
        # self.brand = brand
        # self.model_name = model_name 
        # self.price = price
        # ## our coding principal is dry = don't repeat 
        # yourself , we are not following this above  ... according to dry

        #### we can inherit base/parent class all properties by two ways.

        #### one way --->
        # Phone.__init__(self, brand, model_name, price) ## it is uncommon way . Few people use it

        #### Another way
        super().__init__(brand, model_name, price) ## common way . when we write super()
        ## method we don't need to write self 

        
        self.memory = memory
        self.internal_camera = internal_camera




phone1 = Phone('Nokia', '1100', 3000)
smartphone1 = SmartPhone('Apple', 'iphone 14 pro', 150000, '256GB', '5MP') 

# print(phone1.make_a_call(0))

print(smartphone1.full_name() + f" and price is {smartphone1._price} ") ## Now we can
## call Phone class all properties in SmartPhone class



'''

