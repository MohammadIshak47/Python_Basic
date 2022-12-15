
'''
## set __ unordered collection of unique items
### To remove value or items from set we use set and use mathmatical like union ,intersection

a = {2,3,4,5,6}
# print(a)
# b = a
# # print(set(b))
# print(list(set(b)))

# To add
a.add(7)
a.add(8)
a.add(7) ## same value will taken two times ,only one element take one time
## remove
a.remove(5)
## Discard method
a.discard(4)
a.discard(10) # if value not in set then it will 
#not showing any error by using discard method
## clear method
# a.clear() # it will delete all items in sets
### copy method
b = a.copy()
print(b)
s = {1,1.2,1.0,'bangla'}
print(s)
s = {'a','bangladesh',2,'b'}

## To check any items in this set use in keyword

# if 'a' in s:
#     print("a is present here")
# else:
#     print("a is not present here")

## For loop

# for i in s:
#     print(i)



'''

## union , intersection

a = {1,2,3,4,5,2}
b = {2,3,4,7,8,9}
# result = a.union(b)
## we can also use, |  to union
print(a|b)
# intersectionOfab = a.intersection(b)
### We can intersetion using ,& operation
print(a & b) 
# print(result)
# print(intersectionOfab)


