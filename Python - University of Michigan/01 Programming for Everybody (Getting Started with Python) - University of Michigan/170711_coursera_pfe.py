#Author : Rohan M. Nanaware
#Date C.: 11th Jul 2017
#Date M.: 11th Jul 2017
#Purpose: Python for everybody code documentation

#Chapeter 2 -1st executable code chunk
efloor = input("Europe floor?")
print("US floor",int(efloor)+1)

#Chapter 2 exercise 3
hrs = input("Enter work hours:")
rate = input("Enter hourly rate:")
print("Pay:",float(hrs)*float(rate))

#Chapter 3 Conditional statements
x = 4
if x > 2:
    print("Greater than two")
else:
    print("Less than or equal to two")
print("Comparison complete")
#Chapter 3 More conditional statements
x = 4
if x <= 2:
    print("\nSmall")
elif x < 10:
    print("\nMedium")
#else:
#    print("\nLarge")
print("\n\nComparison completed!")
#Try and except - always include a minimal part of code in the try and except block
x = 'Hello world'
try:
    print(int(x))
except:
    print('Please enter an integer')
    
#Chapter 4 Functions
def computepay(hrs,r):
    if hrs >= 40:
        pay = (hrs - 40)*r*1.5 + 40*r
    else:
        pay = (hrs - 40)*r*1.5 + 40*r
    return pay

hrs = float(input("Enter Hours:"))
rate = float(input("Enter rate per hour:"))
p = computepay(hrs,rate)
print(p)

#Chapter 5 Loops
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break    
    try:
        num = float(num)
    except:
        print("Invalid input")
        continue
    if largest is None:
        largest = num
    elif num > largest:
        largest = num
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num 
    print(largest, num, smallest)
print("Maximum is ", largest)
print("Minimum is ", smallest)
