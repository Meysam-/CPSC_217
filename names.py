"""
The purpose of this program is to read a file which contains some names
and then extract the data from the file and build a python dictionary with it.

The file name will be provided as command line argument.
"""

import sys

print(sys.argv)

# faking the command line arguments
sys.argv = ['names.py', 'GirlsNames1.txt']

file_name = sys.argv[1]

try:
    file_handle = open(file_name, 'r')
    print(file_handle)

    # this line will read the whole file and return it as a string
    file_contents = file_handle.read()
    # print(file_contents)

    # we always need to close the files when we are done whit it
    file_handle.close()

except FileNotFoundError:
    print("file not exist!!")
    exit()

# Processing the contents of the file:
# this line will split the lines of the text and return a List of strings
names = file_contents.split("\n")

print(names)

names_dict = {}
# the following code will go though every line of the file (means every element of "names" List)
for name_number in names:

	# this line will split the name and the number in each line
	split_text = name_number.split(" ")
	if len(split_text) >= 2:
		name = split_text[0]
		number = int(split_text[1])
		names_dict[name] = number

print(names_dict)
