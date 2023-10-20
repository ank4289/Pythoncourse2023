#Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:

Grade= int(input("Enter the Point earned by candidate \n"))
if Grade >= 90 and Grade <=100:
    print("Grade is A")
elif Grade >= 80 and Grade <=89:
    print("Grade is b")
elif Grade >=70 and Grade <=79:
    print("Grade is c")
elif Grade >=60 and Grade <=69:
    print("Greade is d")
elif Grade >=0 and Grade <=59:
    print("Grade is F")
else:
    print("invalid input")

#Write a program that classifies a triangle based on its side lengths.


Side1= float(input("Enter the Side1 \n"))
Side2= float(input("Enter the Side2 \n"))
Side3= float(input("Enter the Side3 \n"))

if Side1 == Side2 and Side2 == Side3 and Side1 == Side3:
    print("its a equilateral triangle")
elif Side1 == Side2 or Side2==Side3 or Side1 == Side3:
    print("its a isoceles trainagle")
else:
    print("Its a scalene triangle")

#✅ Leap Year Checker:
Year= int(input("Enter the Year \n"))
if (Year%4==0 and Year%100!=0) or (Year%400==0):
    print(f"This year is Leap year {Year}" )
else:
    print("This is year is not Leap Year ")


