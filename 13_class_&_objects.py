class Employee:
    company = "Google"

mark = Employee()
david = Employee()
print(mark.company)
print(david.company)

Employee.company =  "Youtube"

print(mark.company)
print(david.company)

# Another example of class objects :-
class circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def circumference(self):   # circumference = 2*pi*r
        return 2 * 3.14 * self.radius

c1 = circle(5)
a = c1.area()
b = c1.circumference()

print("area", a)
print("circumference", b)