1
def triangleTest(a, b, c):
    sides = [a, b, c]
    if sides[0] + sides[1] > sides[2]:
        return True
    else:
        return False

side1 = int(input("enter the first side length: "))
side2 = int(input("enter the second side length: "))
side3 = int(input("enter the third side length: "))

if triangleTest(side1, side2, side3):
    print("It's a triangle!")
else:
    print("It's not a triangle.")

2
def greet(name, time):
    if 0 <= time <= 12:
        print("Good morning,", name)
    elif 13 <= time <= 17:
        print("Good afternoon,", name)
    elif 18 <= time <= 23:
        print("Good evening,", name)

name = input("What's your name: ")
time = int(input("What time is it: "))
greet(name, time)

3
def getEven(numbers):
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
    return even
integers = []
for i in range(0,5):
    ans = int(input("Enter number: "))
    integers.append(ans)
print("Even numbers in the list:", getEven(integers))
