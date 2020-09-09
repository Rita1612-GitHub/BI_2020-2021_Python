#Enter numbers and operator
number1 = float(input('Enter the first number: '))
operator = input('Enter the operator: ')
number2 = float(input('Enter the second number: '))
#Checking
if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    if number2 != 0: #Check devision by zero
        print(number1 / number2)
    else:
        print("Division by zero!")
elif operator == "**":
    print(number1 ** number2)
elif operator == " % ":
    print(number1 % number2)
elif operator == "//":
    print(number1 // number2)
else:
    print("Wrong operator")

