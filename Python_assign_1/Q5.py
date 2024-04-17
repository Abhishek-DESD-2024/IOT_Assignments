'''5)The marks obtained by a student in 3 different subjects are input by the user. Your program should calc
ulate the average of subjects and display the grade. The student gets a grade as per the following rules:
Average Grade
90-100 A
80-89 B
70-79 C
60-69 D
0-59 F'''

sub1=int(input("Enter the marks of subject1:"))
sub2=int(input("Enter the marks of subject2:"))
sub3=int(input("Enter the marks of subject3:"))

avg=float((sub1+sub2+sub3)/3)
#print(avg)


if (avg>=90 & avg<=100):
    print("Grade A")
elif (avg>=80 & avg<=89):
    print("Grade B")
elif (avg >=70 & avg <=79):
    print("Grade C")
elif(avg>=60 & avg <=69):
    print("Grade D")
else:
    print("Fail")


