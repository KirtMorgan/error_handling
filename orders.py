# Error handling/Opening files
# This is the section on opening files
try:
    # The file gets stored in the variable
    file = open('order.txt', 'r')

    # Read line by line and store in another variable(list_of_lines)
    list_of_lines = file.readlines()
    print(list_of_lines)

    # Iterate over the list_of_lines/Print out each line
    for line in list_of_lines:
        print(line.strip())

    # Clean up by closing the file
    file.close()

# This is the section on error handling
except FileNotFoundError as errmsg:
    print('There has been a error, File not found')
    print(errmsg)
    raise



