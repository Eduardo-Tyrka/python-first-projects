# calculator

# numbers 
print("choose a number")
first_number = int(input())
print("choose other number")
second_number = int(input())

# operation
print("choose an operation")
operation = input()

# calculate
if operation == "+":
    result = first_number + second_number
    print("result:")
    print(result)
elif operation == "-":
    result = first_number - second_number
    print("result:")
    print(result)
elif operation == "*":
    result = first_number * second_number
    print("result:")
    print(result)
elif operation == "/":
    result = first_number / second_number
    print("result:")
    print(result)
