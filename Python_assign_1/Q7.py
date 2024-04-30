#Q.7) Using for loop, write and run a Python program to find factorial from 0 to 10
print("The factorial from 1 to 10 is ")

a = 1
b = a
li = [1,2,3,4,5,6,7,8,9,10]
for value in li:
    while a <= value:
        b = b * a
        a = a + 1 
    else:
        print(f"Factorial of {value} is {b}")