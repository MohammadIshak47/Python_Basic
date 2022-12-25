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


### multiple inheirtance 
### multilevel inheritance
## MRO(Method Resoultion Order)
## According to MRO , class called instance/object or methods
### method overriding 
##### isinstance() , issubclass()
### isinstance() , we use it for ,if this object/instance is this class or not.
#  if it then return True  and not , then return False  


class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = price

    def full_name(self):
        return f"{self.brand} {self.model_name}"
    def make_a_call(self,phone_number):
        return f"calling {phone_number} ..."

class SmartPhone(Phone): # derieved/child class ##multiple inheritance
    def __init__(self, brand, model_name, price,memory,ram,internal_camera): ## here
        ## brand, model_name and so on are called instance variable
        super().__init__(brand, model_name, price)
        self.memory = memory
        self.ram = ram
        self.internal_camera = internal_camera
    def full_name(self): ## Here method are overloading because .
        ## full_name() method was Phone class . but it is also used in SmartPhone
        ## class with increase some efficient and performance
        return f"{self.brand} {self.model_name} and price is {self._price}"    

# class SmartPhone2(Phone): # derieved/child class ##multiple inheritance
#     def __init__(self, brand, model_name, price,external_camera,internal_memory,size):
#         super().__init__(brand, model_name, price)
#         self.external_camera = external_camera
#         self.internal_memory = internal_memory
#         self.size = size


class FlagshipPhone(SmartPhone): ## FlagshipPhone derieved from SmartPhone . It is
    ## called multilevel inheritance
    def __init__(self, brand, model_name, price, memory, ram, internal_camera,front_camera,android_version):
        super().__init__(brand, model_name, price, memory, ram, internal_camera)
        self.front_camera = front_camera
        self.android_version = android_version

    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self._price} , {self.ram} {self.front_camera} {self.android_version}"    




## method is known as function

phone1 = Phone('Nokia', '1100', 12000)

smartphone = SmartPhone('Apple', 'iphon pro', 120000, '48MP', '256GB', '6.1inches')
flagshipphone = FlagshipPhone('Realme', 'pro_02', 14000, '64GB', '4GB', '16MP', '48MP', '8.1')

# print(flagshipphone.model_name)
# print(flagshipphone.brand)
# print(smartphone.full_name())
# print(help(smartphone)) ### MRO calling process
## By helping MRO we can see that python first searching SmartPhone class . If the 
## method what it looking for found then take it , if not found then looking for
## another class like Phone . if the method is not exist on 
# and Phone next it will found builtins.object

# print(flagshipphone.android_version)
# print(help(flagshipphone))   ## By using(MRO) help function , first it will looking
##### on FlagshipPhone. If found this method like full_name
## then it take it from our FlagshipPhone class . If not found then it looking upper class
### like SmartPhone . if exist then take ,not exist then looking next upper class
## like Phone . if found then take. and next it will found builtins.object


# print(flagshipphone.full_name()) ## Now it will called first FlashipPhone class.
## so full_name method is not exist FlashipPhone class .Now next it will looking
### SmartPhone class . Now we will find full_name method and python will now called this
## method and stop here searching



print(flagshipphone.full_name())
### Now it will looking this full_name method in FlashipPhone class . If found
## then called it and stop searching


print(isinstance(smartphone, SmartPhone)) ## here smartphone == object and SmartPhone =class
### Return True

print(isinstance(smartphone, FlagshipPhone)) ## return False

### issubclass()

print(issubclass(SmartPhone, Phone)) ## python will check SmartPhone class has inherited
## Phone class or not .If yes then True and if not then False . Here return True

print(issubclass(SmartPhone, FlagshipPhone)) ## return False


'''

### multiple inheritance (no developer use multiple inheritance)## it is too much complicated

class A:
    
    def class_a_method(self):
        return 'I\m just a class A method'
    def hello(self):
        return 'Hello I,m from class A'

class B:
    
    def class_b_method(self):
        return 'I\m just a class B method'
    def hello(self):
        return 'Hello I,m from class B'
            


# class C(A,B):
class c(B,A): ## Here first call class C ,then class B ,then class A
    pass

instance_c = C()

# print(instance_c.class_a_method())
# print(instance_c.class_b_method())

print(instance_c.hello()) ## first it will called class A , method hello

print(help(C)) ## to check MRO we can find out order and solve complxity in multiple inheritance

print(C.mro()) ## to check MRO
print(C.__mro__) ## to check MRO







