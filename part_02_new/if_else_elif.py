'''
winnig_number = int(input("Enter your winnig number : "))

if 0<winnig_number<50:
    print(winnig_number," is the too low number ")
elif winnig_number>100:
    print(winnig_number,' is too high')
else:
    print(winnig_number,"Congrats you are winner") 



winnig_number = int(input("Enter any number : "))
guess_number = int(input("Enter any guessing number : "))

# if guess_number<winnig_number:
#     print("The number is too low")
# elif guess_number>winnig_number:
#     print("The number is too high")
# else:
#     print("Congrats, You win!")

if guess_number == winnig_number:
    print("Contrats, You win!")
else:
    if guess_number<winnig_number:
        print("Too low")
    else:
        print("Too high")  

   
user_name = input("Enter your name : ")
age = int(input("Enter your age :  "))


if (user_name[0] == 'a' or user_name[0] == 'A')  and age>=10 :
    print("You are allow to watch coco movie ")
else:
    print("Sorry, you cannot watch coco movie")

'''
age = int(input("Enter your age : "))

if 1<=age<=3:
    print("You have need no ticket. You are free to enter the zoo")
elif 4<=age<=10:
    print("Your entry ticket price is 150tk only ")
elif 11<=age<=60:
    print("Your entry ticket price is 250tk only") 
else:
    print("Your entry ticket price is 200tk only")       

