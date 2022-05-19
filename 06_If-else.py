# If-else Statement
a = int(input("Enter your age: "))

if a<18:
    print("You are eligible for driving.")
elif a==18:
    print("You are eligible for driving. But drive carefully.")
else:
    print("You are eligible for driving.")


# Another example of if-else
sub1 = int(input("Enter first subject marks: "))
sub2 = int(input("Enter second subject marks: "))
sub3 = int(input("Enter third subject marks: "))

if (sub1<33 or sub2<33 or sub3<33):
    print("you are fail.")
elif (((sub1+sub2+sub3)/3)<40):
    print("You are fail.")
else:
    print("You are passed.")
    