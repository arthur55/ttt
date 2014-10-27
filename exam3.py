import random
numbers=[]
for j in range(6):
    numbers.append(random.randint(1,49))
    for k in range(len(numbers)):
        if numbers[j]==numbers[k]:
            numbers[j]=random.randint(1,49)
print(numbers)
