### filter function

# def is_even(num):
#     return num%2 == 0

# num = [2,3,4,5,6,7,8]
# print(tuple(filter(is_even, num))) ## it will take only even numbers in tuple

### another way:
# num = [2,3,4,5,6,7,8]
# # print(list(filter(lambda a : a%2==0, num)))
# for numbers in num: ## we can iterate filter or lambda only one times but tuple or list many times
#     print(num)

## shortly
# print(list(filter(lambda a : a%2 == 0,(range(1,12))))) 

## using list comprehension
print(list(i for i in range(1,13) if i%2==0))