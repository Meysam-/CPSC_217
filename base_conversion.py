

# This function gives a number which is in base 10 and returns the converted number in base x
# If you do not provide x into the function, it will convert the number to base 2
# x should be somewhere in this range [2,10]
def base10toX(number, x=2):
    bx_number = ""
    while number != 0:
        rem = number % x
        bx_number = str(rem) + bx_number
        number = number // x

    return bx_number


# This function gives a number which is in base x and returns equivalent number in base 10
# x should be somewhere in this range [2,10]
def baseXto10(number, x):
    powers = 1
    sum = 0
    while number != 0:
        rem = number % 10  # getting the right most digit
        sum = sum + rem * powers
        powers = powers * x
        number = number // 10  # shifts the number right and forgets about right most digit

    return sum

# This function gives a number and two bases. it will assume the given number is in base a 
# and will convert number to base b using 2 other functions
# This function will return 2 values:
# first the given number in middle base 10, and second the given number in destination base b
# 2 <= a <= 10 and 2 <= b <= 10
def baseA2B(number, a, b):
    b10_number = baseXto10(number, a)
    base_B_number = base10toX(b10_number, b)

    return b10_number, base_B_number

# how we call our function
b10, bx = baseA2B(521,6, 4)
print("521 in base 10 is:", b10, "and in base 4 is:" , bx)
