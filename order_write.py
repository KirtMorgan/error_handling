
# # Writing the order with a list
# def write_my_order_list(file_name, order):
#     try:
#         with open(file_name, 'a') as file:
#             for item in order:
#                 file.write(item + '\n')
#     except FileNotFoundError as errmsg:
#         print('No file to write on, check your file name')
# write_my_order_list('order.txt', ['Chocolate'])
#
# # Writing the order with a dictionary
# def write_my_order_dictionary(file_name, order_dictionary):
#     try:
#         with open(file_name, 'a') as file:
#                 for value in order_dictionary.keys():
#                     file.write(str(value) + '\n')
#
#     except FileNotFoundError as errmsg:
#         print('No file to write on, check your file name')
#         raise
#
#
# order_dictionary2 = {'item': 'Mushroom',
#                   'price': '10'}
#
# write_my_order_dictionary('order.txt', order_dictionary2)


# def write_my_order_dictionary_formatting(file_name, order_dictionary):
#     try:
#         with open(file_name, 'a') as file:
#                 for key in order_dictionary.keys():
#                     # print(order_dictionary[key])
#                     string_to_save = str(key) + ':' + str(order_dictionary[key])
#                     file.write(string_to_save + '\n')
#     except FileNotFoundError as errmsg:
#         print('No file to write on, check your file name')
#         raise

# Creating a list of dictionaries and calling the functions to write
def write_order_from_list_dictionaries(file_name, order_list_dict):
    try:
        with open('order.txt', 'a') as file:
            for dictionary in order_list_dict:
                print(dictionary)
                for key in dictionary.keys():
                    print(key)
                    print(dictionary[key])
                    string_to_save = str(key) + ':' + str(dictionary[key])
                    file.write(string_to_save + '\n')

    except FileNotFoundError as errmsg:
        print('No file to write on, check your file name')
        raise