
'''
### Why we use dictionaries?
## ans : Because of limitations of lists, lists are not enough to represent real data. 
# Unordered collections of data in key:value pair
# There is no indexing in dictionaries because of unordered list

# Method_01 to create dictionary

# person_info = {'name':'Mohammad Ishak','gender':'Male','profession':'student'}
# print(person_info)

## method_02 to create dictionary

person_info = dict(name ='Mohammad',gender = 'Male',address='Dhaka')
print(person_info)
print(person_info['address']) # to access indiviual data
print(person_info['gender'])

## Which kinds of data dictionary can store?
## anything like strings, list,dictionary,numbers

info_of_person = {
    'name':'Ishak',
    'desire':'To be a great person',
    'favorite_movies' : ['thriller','Vikram'],
    'favs_tunes' : ['jazz','ami dekini']
}

print(info_of_person['favorite_movies'])

## How to add data into empty dictionaries

# user_info = {}
# user_info['name'] = 'Mohammad Ishak'
# # user_info['gender','id'] = 'male','ab1'
# user_info['qualification'] = 'Hons'
# print(user_info)

user_info ={
    'name':'Ishak',
    'working place': 'Dhaka',
    'gender': 'Male'
}


# if 'name' in user_info: # to see key 
#     print("present")
# else:
#     print("Not present")  
# 

# for i in user_info: ## to see all keys
#     print(i)

# for i in user_info.values(): ## to see all values
#     print(i)

##loop in dictionaries

# for i in user_info:
#     print(user_info[i])

##items methods
# user_items = user_info.items()
# print(user_items)
# print(type(user_items))

# for key,value in user_info.items():
#     print(f"the key is {key} and value is {value}")

## pop method

# popped_items = user_info.pop('gender')
# print(f"pop item is {popped_items}")
# print(popped_items)


## popitem

pop_item = user_info.popitem()
print(user_info)
print(pop_item)

user_info = {
    'Name':'Mohammad Ishak',
    'Gender':'Male',
    'favs_time':'winter',
    'favs_books': ('Bela furabar age ','by arif azad'),
    'favs_tunes': ('isq','pyaar thora')
}

more_info = {'Name':'Foisal Imtiaz','city':'Dhaka','Hobbies':['reading books','videos']}

user_info.update(more_info)
print(user_info)

## fromkeys

user_info = {'name':'Ishak','age':'26','gender':'male','gender':'female'} ## in 
#dictionaries there not will be same key .it will be print only one key and overrite with end key
# user_info = dict.fromkeys(('name','age','gender'),'unknown') # unknown value will enter the name ,age and gender keys
# user_info = dict.fromkeys(range(1,10),'unknown')
## Get Method
# print(user_info.get('name'))# we can access keys &  get keys value using get method
# print(user_info)

print(user_info.get('names')) ## if not key found then it return None
print(user_info.get('names','not found')) # Now it will return not found

print(user_info)

# if user_info.get('name'):
#     print("This method is present here")
# else:
#     print("This method is not present here")
## None means no value is exist here
# # if None ...False else True

# # user_info.clear()
# user_info1 = user_info.copy()
# user_info1.popitem()
# print(user_info1)        


##problem_02: Define a function that takes a number(n).return a dictionary containing
# cube of numebers from 1 to n. (cube menas 1**3)

## Solution:
##cube finder

def cube_finder(n):
    cubes = {}
    for i in range(1,n+1):
        cubes[i] = i**3
    return cubes
print(cube_finder(5)) 

'''
       

