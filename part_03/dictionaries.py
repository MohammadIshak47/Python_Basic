
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
'''

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

for key,value in user_info.items():
    print(f"the key is {key} and value is {value}")