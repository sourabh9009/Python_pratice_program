# a={"Sanyam",456,456.5676887}
a=("Sourabh", 7566029864,"cooldude@gmail.com","RNT Hostel ")

print(a)
print(type(a))

b= list(a)
print(type(b))
print(b)
#   Appending 
b.append(26)
print(b)

#  Inserting
b.insert(1,"Kumar")
print(b)

#        Printing Details
print("Name : ", a[0] )
print("Contact Number  : ", a[1] )
print("Email  : ", a[2] )
print("Address  : ", a[3] )
