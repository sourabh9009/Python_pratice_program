letter = '''Dear name,

I'm very glad to inform you about your selection in our coding house.
you are selected.
Have a great day ahead.
Greetings and regards.

Tom.
Date: date
'''
Name = input("Enter your name\n")
Date = input("Enter Date\n")
letter = letter.replace("name", Name)
letter = letter.replace("date", Date)
print(letter)