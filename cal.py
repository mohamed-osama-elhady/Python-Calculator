num1 = input("Enter your first number: : ")
operator =  input("Enter the operator you wish to perform: (+,-,*,/) ")
num2 = input("Enter the second number: ")

num1 = float(num1)
num2 = float(num2)


if operator == '+':
    result =num1+num2
elif operator == '-':
    result = num1-num2
elif operator == '*':
    result = num1*num2
elif operator == '/':
    if num2 != 0 :
        result = num1/num2
    else :
        print("Cannot divide by zero")
        exit()

else : 
    print("invalid operator entered")
    exit()
print (num1, operator, num2, '=', result)