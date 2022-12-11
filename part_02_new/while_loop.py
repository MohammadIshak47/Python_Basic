'''
i = 1
while i<=10:
    # print("Hello Python")
    print(f"Hello world {i}")
    i = i+1

#sum of any number from 1 to 10 
sum = 0
i = 1

while i<=10:
    sum = sum+i  # or sum+=i means sum = sum+i   # sum = 0+1+2+3+4+5+6+7+8+9+10
    i = i+1
print(sum) 

#print natural number from 1 to n

n = int(input("Enter any number : "))

sum = 0
i = 1

while i<=n:
    sum+=i #sum = sum+i
    i+=1
print(sum)

#problem: Ask user to input  containing more than one digit .
# Example 1256 . calculate 1+2+5+6 and print

#solution : 

n = input("Enter any number : ")

sum = 0
i = 0

while i<len(n):
    sum+= int(n[i])
    i+=1
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


name = input("Enter your name : ")

temp_vari = ""

i = 0
while i<len(name):
    if name[i] not in temp_vari:
        temp_vari+= name[i]
        print(f"{name[i]}:  {name.count(name[i])}")
    i+=1  

'''

# Infinite Loop

i = 0
while i<=10:
    print("You are well behavior")




  



 
   
  
    
