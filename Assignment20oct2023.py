#Task: Create a function that checks if a given string is a palindrome (reads the same forwards and backward). 121'
def Palindrome():
    if Name == Rev:
        print("This string is Palindrom")
    else:
        print("Not a Palindrome")



Name= input("Please enter a name \n")
Rev= Name[::-1] # Reverse the whole string
print(Rev)

Palindrome() # Function calling

# Sum of digit of positive integer
def Sumofnumber():
    if a <= 0:
        print("This is input not applicable enter any positive number")
    else:
        sum=0
        for i in range(1, a+1):
            sum= sum + i
        print("The sum of number is:",sum)

a= int(input("Please enter a new input number \n"))

Sumofnumber()
