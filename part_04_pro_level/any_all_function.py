
'''
###  all function ## all function define all values in a list or dict is true or false
## any function defines if any numbers in a list is even it will give True
numbers1 = [1,2,3,4,5]
numbers2 = [64,6,78,8,96]

# evens = []

# for num in numbers1:
#     evens.append(num%2==0)

# print(evens) 
# print(all([True,True,True,True,True]))  

### using list comprehension

print(all([i%2==0 for i in numbers1]))
print(all([i%2==0 for i in numbers2])) ## all numbers are even . so it is given True
print(any(numbers1)) ## Here it will given True

'''

##  any all


# def find_total(*args):
#     if all([(type(arg) == int or type(arg) == float) for arg in args]):
#         total = 0
#         for num in args:
#             total+=num
#         return total
#     else:
#         return "Wrong input"    

# print(find_total(2,3,4,5))
# print(find_total(2,2.3,'ishak','Mohammad',['Ishak Ahmed'])) ## Now it can't be sum 
## Now it will return wrong input or given text

    
