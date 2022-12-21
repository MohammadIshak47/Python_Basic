
'''
### Sorted function 

# fruits = ['banana','jackfruit','orange','apple','mango']
# fruit1 = ('banana','jackfruit','orange','apple','mango') ## here tuple are immutable menas
# ## unchangeable
# print(sorted(fruits))
# print(sorted(fruit1)) ## first it will take fruit1 then convert into list and print it as list

# fruit3 = {'banana','jackfruit','orange','apple','mango'}
# print(sorted(fruit3))## first it will take fruit1 then convert into list and print it as list
'''

### Advance level

mobile = [
    {'brand_name':'samsung','model':'s21ultra','price':'100000'},
    {'brand_name':'google','model':'pixel6_plus','price':'50000'},
    {'brand_name':'oppo','model':'a12','price':'40000'},
    {'brand_name':'Vivo','model':'poco31','price':'23000'}

]

# print(sorted(mobile,key = lambda item : item.get('price'))) ## output will be lower price to higher price
# print(sorted(mobile,key = lambda item:item['price']))
# print(sorted(mobile,key= lambda item : item['price'] ,reverse =True)) #It will give
## output higer price to lower price

# print(sorted(mobile,key =  lambda item : item.get('price'),reverse =True))



