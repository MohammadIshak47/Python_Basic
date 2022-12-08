
'''

###
def add(a,b):
    return a+b

print(add(33,44)) 

def sum_num(a,b,c):
    return a+b+c


a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

print("The result of sum is : ",sum_num(a, b, c))

def last_char(name):
    return name[-1]

print(last_char('Mohammad'))    # it will return last character of the name  

## Without passing parameter or argument

def performance():
    return "Your laptop performance is so much poor"

print(performance())


def odd_even(num): # odd even check
    if num%2==0:
        return "even"
    else:
        return "odd"
num = int(input("Enter any number : "))
print(odd_even(num))

## we can write above code also below format: _
def odd_even(num):
    if num%2 == 0:
        return "even"
    return "odd"
num = int(input("Enter any number : "))
print(odd_even(num)) 

## we can write above code also below format: _

def is_even(num):
    if num%2 == 0:
        return True
    return False

num = int(input("Enter any number : "))
print(is_even(num))

## we can write above code also below format: _
def is_even(num):
    return num%2 == 0

num = int(input("Enter any number : "))
print(is_even(num))


# problem_01_ define two numbers and findout the largest numbers between two numbers

#Solution :
def  number(a,b):
    if a>b:
        return a," is grater than",b
    return b, "is grater than ",a
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
print(number(num1, num2))  

# Another way : 
def is_grater(num1,num2):
    if num1>num2:
        return num1
    return num2

num1 = int(input("Enter number1 : "))
num2 = int(input("Enter number2 : "))
print("The grater is ",is_grater(num1, num2))


# problem : define three numbers. Findout gratest one.

solution : 
def grater_num(num1,num2,num3):
    if num2<num1>num3:
        return num1
    elif num1<num2>num3:
        return num2
    return num3 # this return works like else

num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))
num3 = int(input("Enter your third number : "))
print("The gratest is ",grater_num(num1, num2, num3))


# Funciton inside Function
def new_greatest(a,b,c):
    # bigger = greater(a,b)
    # return greater(bigger,c)
      return greater(greater(a,b),c)

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

print("The gratest number is ",new_greatest(num1, num2, num3))

## kiss _--- keep it simple stupid

### Palindrome problem: 

def is_palindrome(word):
    if word == word[::-1]:
        return True
    return False

palindrome_numw = input("Enter any word or num : ")

print(is_palindrome(palindrome_numw))

## Another way :

def is_palindrome(word):
    return word == word[::-1]

word = input("Enter any number or word : ")
print(is_palindrome(word))


'''

## Fibonacci number : 

# 0 1 1 2 3 5 8 13 ..... 

def Fibonacci_num(number):
    a = 0 # first number
    b = 1 # second number 

    if number == 1:
        print(a)
    elif number == 2:
        print(a, b)  # first and second number will print 0 1
    else:
        print(a, b , end = ' ') # here end = '' means it will print all numbers accordingly list or in one line
        for i in range(number-2): # w have written n-2 because first two numbers is fixed, if we print many number then it will print total number -2
            c = a+b
            a = b
            b = c 
            print(b, end = ' ')
            

number = int(input("Enter any number :  "))
print(Fibonacci_num(number))






       

            