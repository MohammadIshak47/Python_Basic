'''


for i in range(10):
    print(f"Hello world : {i}")



# 1+2+3+4....+10

sum = 0
for i in range(1,11):
    sum+=i
print(sum) 

#another way :

num = int(input("Enter any number : "))

sum = 0

for i in range(1,n+1): #Here we have written n+1 because when we take input 9 ,it will print 8 .that's why we write n+1
    sum+=i
print(sum)

## problem ask a user like 1234

calculate sum of digits 1+2+3+4

solution :
sum = 0
num = input("Enter any number : ")

for i in range(0,len(num)):
    sum+=int(num[i])
print(sum) 

###another simple way:
# ## problem ask a user like 1234

#calculate sum of digits 1+2+3+4

#solution :

num = input("Enter your number : ")
sum = 0

for i in num:
    sum+=int(i)

print(sum)   


#  problem: ask a user for name . Example : Mohammad Ishak
# print count of each words and spaces . output will be :


M : 1
m : 2
h : 2
a : 3
d : 1
I : 1
s : 1
k : k
  : 1 #space or indentation 

solution: 
# mohammd 
m
o
h
a
m
m
d
#Another way 
name = input("Enter your name : ")

# for i in name:
 or # for i in "Mohammad":
    print(i)

'''

# name = input("Enter any number : ")

# tem_vari = ""

# for i in range(0,len(name)):
#     if name[i] not in tem_vari:
#         name+= tem_vari
#         print(f"{name[i]}: {name.count(name[i])}")


  
    
    

  
   

