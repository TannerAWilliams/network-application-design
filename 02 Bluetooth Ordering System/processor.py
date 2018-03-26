#Processor – Mobile Phone
# Filename: processor.py
# - Processor indefinitely processes orders coming in through the RMQ order
#queue.
# - Before it beings processing an order, it uses the order id to send the device
#that placed the order a notification that processing has begun.
# - After processing the order, it uses the order id to send the device that placed
#the order a notification that processing has ended.
# - Mobile device terminates after receiving this final third status update.

# Exists on its own RPi
# Subscribes to the ”order” queue.
# Does not declare exchanges or queues
# Sends led status commands to the “led” queue.
# Sends order status notifications to the client queues