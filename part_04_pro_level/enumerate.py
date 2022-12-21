
'''
### We use enumerate function with for loop to track position of our item  in iterable

## How can we do this without enumerate function

names = ['bangla','english','mathematics','science']

# position = 0

# for name in names:
#     print(f'{position} ...> {name}')
#     position+=1

### Using enumerate function

for pos,name in enumerate(names):
    print(f'{pos}...> {name}')    


'''

## Define a function that takes two argument
# 1. list containing string
# 2. string that want to find your list
# this function will return the index of string in your list and if 
# string is not present then return -1

def find_index_position(list1,target):
    for pos, name in enumerate(list1):
        if name == target:
            return pos
    return -1
names = ['abdullah','anas','ayisha','irfan']    
# print(find_index_position(names, 'kamal'))   


