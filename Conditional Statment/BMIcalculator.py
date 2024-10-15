weight=float(input("Enter Your Weight! "))
height=float(input("Enter Your Height! "))
BMI=weight/height**2
if BMI <= 18.4:
    print(BMI , " You are under weight!")
elif BMI <= 24.9:
    print(BMI , " You are healthy!")
elif BMI <= 29.9:
    print(BMI , " You are over weight!")
elif BMI <= 34.9:
    print(BMI , " You are severly over weight!")
elif BMI <= 39.9:
    print(BMI , " You are obese!")
else:
    print(BMI," You are severly obese!")