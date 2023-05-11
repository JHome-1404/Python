# CONDICIONAL IF
# CONDICIONAL IF

x = 30
if x < 30:
    print("x is less than 30")
else:
    print("x isn't less than 30")

color = "red"
if color == "red":
    print("the color is red")
elif color == "blue":
    print("the color is blue")
else:
    print("any color")

# EXAMPLE
# Form
name = "John"
las_name = "Carter"

if name == "John":
    if las_name == "Carter":
        print("Hello John Carter")
    else:
        print("You're not John Carter")
else:
    print("You're not John Carter")

x = 30
y = 10
if x > 2 and x <= 10:
    print("X is greater than two and less than or equal to ten")
if x > 2 or x <= 20:
    print("X is geater than two or less or eequal to twenty")
if not (x == y):
    print("X is not equal y")
