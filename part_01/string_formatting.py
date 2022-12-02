'''
name = 'Mohammad Ishak'
age = 26
a = ("Hello, "+name+" . You are now " +str( age) +" old." )

print(a)

# alternative way :
name = "Mohammad Ishak"
age = 26

print("Hello , {} . You are now {} years old".format(name,age))
# Another extreme way
print(f"Hello, {name} .You are now {age} years old") # You must first put on f string.

#Exercise_01: Ask user to input 3 numbers ,you have to prin avegers of the giving 3 numbers
#using string formating . Note : try to all separeted inputs in one line using comma

#solution :

number_one,number_two,number_three = input("Enter your desired three numbers : ").split(",")


print(f"The average of three numbers is : {(int(number_one)+int(number_two)+int(number_three))/3}")




'''
#problem with solution

name,char = input("Enter separated comma name and char : ").split(",")
print(f"Length of my given name are {len(name)}")

print(f"character count :  {name.lower().count(char.lower())}")


