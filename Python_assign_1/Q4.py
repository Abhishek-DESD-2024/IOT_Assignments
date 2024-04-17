#Write a Python function to find the maximum of three numbers.

num1=int(input("Enter Num1:"))
num2=int(input("Enter Num2:"))
num3=int(input("Enter Num3:"))


def fun(num1,num2,num3):
    if (num1>num2):
        print("num1 is greater")
    elif(num2>num3):
        print("num2 is greater")
    else:
        print("num3 is greater")

fun(num1,num2,num3)