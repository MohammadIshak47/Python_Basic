'''
### lambda function(anonymous function)
## it is used in built in ,map,reduce,filter

# def add(a,b):
#     return a+b

# print(add(2, 3)) 
## In lambda
# print( (lambda a,b:a+b)(2,3)) 
# print((lambda a,b : a*b) (2,3))

### lambda  Expression practice
print((lambda a: a%2==0) (5)) ## Odd or even findout
print((lambda a: a[-1])("Mohammad")) ## to findout last character of the word

'''

###   if word length > 5 return True else false

# print((lambda a : True if len(a)>5 else False) ('bangla')) 
## without if else
print((lambda a : len(a)>5) ('bangladeshi'))