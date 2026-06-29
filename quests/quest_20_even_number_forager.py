# The concept here is using the if insde a for loop to filter numbers 
#here we loop through numbers 1 to 20
for i in range(1, 21): 
# if i % 2 equals to 0, the number has no remainder so it is even
    if i % 2 == 0:
        print(i) # print only even numbers
