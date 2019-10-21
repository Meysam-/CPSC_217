# This program will compute the factorial of any number given by user
# until user enter some negative values.

n = int(input("please input a number: "))

# the loop for getting user inputs 
while n >= 0:
	# initializing 
    fact = 1
    # calculating the factorial 
    for i in range(1, n+1):
        fact *= i
        # fact = fact * i

    print("%d ! = %d"%(n,fact))

    n = int(input("please input a number: "))
