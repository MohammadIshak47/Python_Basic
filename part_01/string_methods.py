'''
a = "There are many people here with some hasitation & you are given some fruits"
# print(a.replace("are", "were"))
# print(a.replace(' ', '_')) spaces replaces with underscroe
# print(a.replace('are', 'were',1)) # only one are replaces with were

# print(a.find('are'))
are_posi1 = a.find('are')
are_posi2 = a.find('are',are_posi1+1) # we want to find out second are position

print(are_posi2)

'''

## Center method

# a = "Mohammad" # here a string length is 8 . If we want to add * left and right 
# #between string,then we have to given 10 

# print(a.center(10,'*'))
# print(a.center(12,"*"))

name = input("Enter your name : ") # Whatever user input name , then it's left and right side will print 4 *
print(name.center(len(name)+8,"*")) 





