
for i in range(50):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif (i % 2 == 0) :
        print("Fizz")
    elif (i % 4 == 0):
        print("Buzz")
    else :
        print(i)
    