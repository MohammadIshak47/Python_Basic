### We will discuss three problem existing 
## then we will solve them using setter ,setter deocorder


class Phone:

    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = price
        self.complete_specification = f"{self.brand} {self.model_name} and {self._price} "

    def make_a_phone(self,phone_number):
        return f"calling {phone_number}..."  

    def full_name(self):
        return f"{self.brand} {self.model_name}"


phone1 = Phone('Apple', 'iphone14 pro', 123000)
phone2 = Phone('Oppo', 's21', 30000)

print(phone1.brand)
print(phone1.model_name)
print(phone1._price)
print(phone1.full_name())
print(phone1.complete_specification)