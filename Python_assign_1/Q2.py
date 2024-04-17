#Write a program to accept a 4 digit number and
"""
a. Display face value of each decimal digit
b. Display place value of each decimal digit
c. Display no in reverse order by changing decimal place values If user enters a 4 digit number 9361 outp
ut should be
a. 9 3 6 1
b. 9361 = 9 000 + 300 + 60 + 9
c. 1639
"""

num =int(input("Enter a four digit number:"))

i = 1
while i <=4:
    rem = int(num % 10)
    num=num/10
    i=i+1
    rev = num*10 +rem

    print(f"{rem}")