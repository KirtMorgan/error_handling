# Error handling/Opening files
# This is the section on opening files
def open_function (file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file.readlines():
                print(line.rstrip('\n'))

    # This is the section on error handling
    except FileNotFoundError as errmsg:
        print('There has been a error, File not found')
        print(errmsg)
        raise

    finally:
        print('File open, read and list execution complete')

open_function('order.txt')
