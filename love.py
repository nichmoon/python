operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+" :
    results = num1 + num2
    print(results)
elif operator == "-":
    results = num1 - num2
    print(results)
elif operator == "*":
    results = num1 * num2
    print(results)
elif operator == "/":
    results = num1 / num2
    print(results)
else:
    print(f"{operator} is not found") 
   
