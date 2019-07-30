
# 1) generate random numbers 
# 2) append that random number to a list
# 3) calculate the sum of each item in that lists

import random

# this will generate a random number between 0 and 20
# and store it a variable called randoms
# random = random.randint(0,20)
# print(random)
# range(10) will create a new list between 0 and 10

numList = []

for x in range(35, 40):
    randomNumber = random.randint(0,20)
    # print(randomNumber)
    numList.append(randomNumber)
    print("current numList in loop", numList)

print("final numList: ", numList)

# initialize a variable called sum as 0; start with 0 the add eachItem
sum = 0

for eachItem in numList:
    sum = sum + eachItem 
    print(sum)

    
print("final sum is = " + str(sum))
