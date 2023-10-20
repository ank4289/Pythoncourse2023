# fabonaci series

for fab in range(10):
    fab = fab + 1
    print(fab)

#Factorial

fact= int(input("Enter the number for factorial\n"))
factorial=1
if fact >= 1:
    for i in range(1,fact+1):
        factorial= factorial *i
        print("Factorial is ",factorial)