'''
### generators 
### generators are iterators
## generators is sequence but it also an iterators
### we can't run loop two times in generator

## iterator
## iterable

l= [1,2,3] ## iterable ## in iterable items print again and again to finish it
## iterable is limited to call & so problems but iterator has not exist it
## iterable need to convert into iterator but iterator not needed to convert

i = iter(l) ## here it will be change in  iterator
# print(i)
# map(lambda a : a**2,l) ## here it will return iterator
for i in map(lambda a : a**2, l): ## we can for loop in iterator
    print(i)

# l = [1,2,9,6,7]
## we access more value in sequence we need to use list
## memory.....[9] ## in generator one time access only one value in sequenc


#### create my first generator in generator function
## generator function

## 1 to 10 print

def nums(n):
    for i in range(1,n+1):
        yield i ## by using yield it becomes generator ## yield is a keyword .
        ## so we don't need to write it like yield i instead of yield(i)

# print(nums(10))

for number in nums(10): ## it will generator 1 to 10 when we demand it otherwise not
    print(number)  ## generator generate one times in one num . then again generate next
    ## number like 2 then previous number 1 will be deleted and new number 2 will 
    # be access in memory then again generate next number like 3 will be access and
    ## previous number 2 will be deleted . That's why it save memory space


## problem_01: 
# define generator function
# take one number as argument
# generate a sequence of even numbers from 1 to that number

### Solution : 
def even_num_finder(n):
    for num in range(2,n+1,2):
        # if num%2== 0 :
            yield num



for num in even_num_finder(10): ## if generator will create one times then 
    ## we can run loop in only one times
    print(num)    


### Generator comprehension

# print([i**2 for i in range(1,10)])

## Using generator we can do this term like
square = (i**2 for i in range(1,10)) ## it has already created generator to use this ()

# print(next(square))
# print(next(square))
# print(next(square))

for num in square:
    print(num)
'''


### List vs generator

### memory usage ,time
## when should use list , when should use generator
## time
import time

# t1 = time.time()
# list1 = [i**2 for i in range(10000000)] ## 10 million enough time to run
# # t2 = time.time()
# # print(t2 - t1)
# print(time.time()-t1)


t1 = time.time()
generator = (i**2 for i in range(10000000)) ## 10 million tiny time to execute
print(time.time()-t1)
        
### when we need to use generator num again and again and run loop multi times
## like todo list then we need to use list

### we don't want to execute or run loop multi times then we need to use generator