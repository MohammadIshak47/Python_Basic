
### Decorators

# def square(*a):
#     return a**2

# print(square(4))

####  pass function as a argument 

# def square(a):
#     return a**2


# l = [1,2,3,4,5]
# print(list(map(square, l)))

## custom function
l = [1,2,3,4]
def square_define(func,l):
    new_list = []
    for item in l:
        new_list.append(func(item))
    return new_list



