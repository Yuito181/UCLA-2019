#BEGINNING OF CALCULATOR


# 1) use if-statements to complete this calculator program with 4 operations
# Example run (what it should look like):
#       0 - add
#       1 - subract
#       2 - multiply
#       3 - divide
#   Enter a number to choose an operation:
#   1
#   Enter your first input: 7
#   Enter your second input: 4
#   7 - 4 = 3

# 2) add a fifth operation, power, that does a to the power of b
# 3) add a sixth operation, square root, that only asks for 1 input number and outputs its sqrt
# 4) seventh operation, factorial(a), one input
# 5) eighth operation, fibonacci(a), one input
# 6) talk to instructors when finished


print("  0 - add")
print("  1 - subract")
print("  2 - multiply")
print("  3 - divide")
print("Enter a number to choose an operation: \n")
op = input()

a = int(input("Enter your first input: "))
b = int(input("Enter your second input: "))

print("a + b =",a+b)


#END OF CALCULATOR