'''
## make flexible fuctions
# *operator
# *args

## Summation two numbers
def sum_all(*args):
    total = 0
    for num in args:
        total+=num
    return total

print(sum_all(20,12,14))

'''

## *args with normal parameter

# def multiply_all(*args):
def multiply_all(num,*args): ## here if we enter normal parameter (num),then *args will
    total = 1                 # take all value except first value
    for i in args:
        total*=i
    return total

print(multiply_all(2,3,4,3))