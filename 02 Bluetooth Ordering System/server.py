#Filename: server.py
# - When the server receives an order request, it sends the “receipt” to the
#Bluetooth client, but it also sends that same receipt to a processor through
#and RMQ order queue that the processor RPi is listening to.
# - Bluetooth server sends a message to the “led” queue to update the LED
#status.