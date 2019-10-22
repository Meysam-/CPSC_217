"""
This program will prompt the user to enter a number
Then based on the user input will print some rectangle 
for example:
	n = 1
	*

	n = 2
	**
	**

	n = 3
	***
	* *
	***

	n = 5
	*****
	*   *
	*   *
	*   *
	*****
"""

n = int(input("input number:"))

# first for will generate the rows
for i in range(n):
	# second for in for columns
    for j in range(n):
    	# if it is first row or last row
        if i == 0 or i == n-1:
            print("*", end='')
        # middle rows
        else:
        	# first column or last column in the middle rows
            if j == 0 or j == n-1:
                print("*", end='')
            # middle columns in the middle rows
            else:
                print(' ', end='')
    print() # this empty print is for going to the next line

