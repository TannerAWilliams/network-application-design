# Only server.py uses this menu
# Any number of items can exist in this menu
# Keys names on the items in the menu dictionary can be changed to any item name.
# All values set to the keys in the dictioanry should be a sub dictionary formatted like this:
# {'price':<PRICE>, 'time':<TIME>}
# 
# Example 1:
# 	menu = {'item1':{'price':1.50, 'time':4},
# 	'item2':{'price':2.25, 'time':6},
# 	'item3':{'price':3.00, 'time':10},
# 	'item4':{'price':4.50, 'time':2}}
#
# Example 2:
# 	menu = {'tomatos':{'price':5.25, 'time':1},
# 	'cheese':{'price':2.25, 'time':4},
# 	'bread':{'price':1.75, 'time':3},
# 	'milk':{'price':4.50, 'time':3},
#	'avocado':{'price':1000000, 'time':100}}
#
# Example 3:
# 	menu = {'A Wrinkle In Time':{'price':10.75, 'time':1}}


# A python file containing a menu of items with key value pairs
#related to that item including label, price, and time.
# Located only on server.
# Used to display menu to client and for simulating processing
#time.

menu = {}


