import random
i = 0
temp = 0
while i <10:
    deepak = random.randrange(0,10)
    aryan = random.randrange(0,10)
    a = int(input(f"Question {i+1} : {deepak}*{aryan}: "))
    i = i+1
    if a == deepak * aryan:
        print("Right!")
        temp = temp +1
    else:
        print("Wrong.The answer is ",deepak*aryan )

if temp <=5:
    print("Sorry, you got just",temp,"correct.")

if temp>5:
    print("Great,You got",temp ,"correct")



