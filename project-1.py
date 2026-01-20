# Simple Calculator


val1 = eval(input("Enter the input1 :- "))
val2 = eval(input("Enter the input2 :- "))
operator = input("Enter the operator:- ")
if operator == "+":
    print(val1 + val2)
elif operator == "-":
    print(val1 - val2)
elif operator == "*":
    print(val1 * val2)
elif operator == "/":
    print(val1 / val2)
elif operator == "%":
    print(val1 % val2)
elif operator == "^":
    print(val1 ** val2)
else:
    print("Invalid operator")
