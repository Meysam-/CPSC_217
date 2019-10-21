# This program will sort three inputted numbers

# getting the inputs 
a = int(input())
b = int(input())
c = int(input())

# Method 1
# initializing
# we imagine that x < y < z
x = 0
y = 0
z = 0

if a < b:
    x = a
    z = b
else:
    x = b
    z = a

if x < c:
    if z < c:
        y = z
        z = c
    else:
        y = c
else:
    y = x
    x = c

print(x,y,z)

# Method 2
if a < b < c:
    print(a, b, c)
elif a < c < b:
    print(a, c, b)
elif b < a < c:
    print(b, a, c)
elif b < c < a:
    print(b, c, a)
elif c < a < b:
    print(c, a, b)
else:
    print(c, b, a)

# Method 3
if a > b:
    a, b = b, a

if b > c:
    b ,c = c, b

if a > b:
    a, b = b, a

print(a, b, c)










