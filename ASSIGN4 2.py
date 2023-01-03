a = int(input("Please enter a year and in return I will tell you whether it is a leap year or not: \n"))
if a%4==0 and (a%100!=0 or a%400==0):
    print("Yes, it is a leap year.")
else :
    print("It's not a leap year.") 