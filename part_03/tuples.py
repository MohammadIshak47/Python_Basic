## Tuples are immutable that meanse it not changeable or updateable
## we cannot change it values once it created
## but can add ,delete data from tuple list which is present inside tuple
## tuple is faster than list
## after element without comma it not would be tuple
## tuples are ordered collection of items
## No append ,no pop , no insert, no remove
## only count and index
'''
# tuples = (2)
tuples = (2,) # it would be tuples
print(type(tuples))
a = ("bangla",)  # it would be tuples
print(type(a))

## tuple without parenthesis
tuple1 = 'bangla','english','science','religious study'
print(type(tuple1))

## tuple unpacking

name = ('rasel','faisal','mursalin')
name1,name2,name3 = name
print(name1)
print(name2)
print(name3)

### List inside tuples

color = ('red',['green','purple','orange'])
color[1].pop()
color[1].append('color choice')
print(color)


## Function return two values 

def func(num1,num2):
    addition = num1+num2
    multiplication = num1*num2
    return addition,multiplication

# print(func(10, 20))
addition,multiplication = (30,40)
print(addition)
print(multiplication)

'''

# nums = tuple(range(1,10))
# print(nums)










