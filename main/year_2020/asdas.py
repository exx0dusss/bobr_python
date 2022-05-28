import operator
while True:
    try:
        digit_one = int(input('Enter digit one '))
        digit_two = int(input('Enter digit two '))
    except TypeError:
        print("You can enter only digits ")
    else:
        break
    
sign = input("Enter operator ")
if sign not in ['+','-','/','*']:
    print("I dont know this operator")
    
if sign == "+":
    result = operator.add(digit_one, digit_two)
    print(f"Result {result}")
elif sign == "-":
    result = operator.sub(digit_one, digit_two)
    print(f"Result {result}")
elif sign == "/":
    result = operator.truediv(digit_one, digit_two)
    print(f"Result {result}")
elif sign == "*":
    result = operator.mul(digit_one, digit_two)
    print(f"Result {result}")