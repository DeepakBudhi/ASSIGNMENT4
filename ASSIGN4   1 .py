a = int(input("Enter your marks:\n"))
if a<0 or a>100:
    print("Invalid input")
elif 0<a<25:
    print("Your grade is F")
elif 25<=a<45:
    print("Your grade is E")
elif 45<=a<50:
    print("Your grade is D")
elif 50<=a<60:
    print("Your grade is C")
elif 60<=a<80:
    print("Your grade is B")
elif 80<=a<=100:
    print("Your grade is A")