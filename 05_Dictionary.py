# Dictionary in python
myDict = {
    "fast": "In a quick manner",
    "sourabh": "A coder",
    "marks": [43, 34, 45, 32],
    "anotherdict": {'sourabh': 'player'},
    1 : 2,
}
print(myDict['fast'])
print(myDict['sourabh'])
print(myDict['marks'])
print(myDict['anotherdict'])
print(myDict[1])

# Dictionary methods :-
myDict = {
    "fast": "In a quick manner",
    "sourabh": "A coder",
    "marks": [43, 34, 45, 32],
    "anotherdict": {'sourabh': 'player'},
    1 : 2,
}

print(myDict.keys())
        # OR
print(list(myDict.keys())) # Prints the keys of the dictionary.


print(myDict.values())
        # OR
print(list(myDict.values())) # Prints the values of the dictionary.


print(myDict.items()) # Prints the (key, value) for all contents of the dictionary.
