num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number "))
num3 = int(input("Enter the third number "))
num4 = int(input("Enter the fourth number "))

if (num1>num4):
    f1 = num1
else:
    f1 = num4

if(num2>num3):
    f2 = num2
else:
    f2 = num3

if(f1>f2):
    print(f1, "is greatest")
else:
    print(f2, "is greatest")