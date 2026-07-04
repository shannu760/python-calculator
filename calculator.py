num1 = int(input("give me a number: "))
num2 = int(input("give me a second number: "))
opt = input("choose an operator: ")
if opt=="+":
    c=num1+num2
    print(c)
elif opt=="-":
    print(num1-num2)
elif opt=="*":
    print(num1*num2)
elif opt=="/":
    print(num1/num2)
else:
    print("invalid operator")

