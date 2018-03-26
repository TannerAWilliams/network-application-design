# The same copy of this file should be used by 
# server.py, led.py, processor.py and client.py.
# Each use this to establish a connection with the RabbitMQ Server.
# DO NOT change the key names in this dictionary.
# Feel free to change the values.
#
# Example:
# rmq_params = {"vhost": "vcoolhost", 
# "username": "bryan", 
# "password": "imahokie123", 
# "exchange": "sysexchange", 
# "order_queue": "orders",
# "led_queue": "ledstatus"}


# A python file containing a dictionary with key value pairs
#related to connecting to the RabbitMQ Server.
# Located on client, server, and processor.

rmq_params = {"vhost": "", 
"username": "", 
"password": "", 
"exchange": "", 
"order_queue": "",
"led_queue": ""}


