from order_write import *

# order_dictionary= {'Item': 'Apples',
#                     'Price': '£1'}
#
# write_my_order_dictionary_formatting('order.txt', order_dictionary)

order_list_of_dictionaries = [{'item': 'Pie', 'price': 14},
                               {'item': 'Chocolate', 'price': 10},
                               {'item': 'Tofu', 'price': 13}]

write_order_from_list_dictionaries('order.txt', order_list_of_dictionaries)