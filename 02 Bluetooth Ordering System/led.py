#Filename : led.py
# - Exists on the same RPi as the RabbitMQ server.
# - Handles client orders via Bluetooth.
# - Subscribes to the ”led” queue.
# - Does not declare exchanges or queues
# - Listens for color commands to change the LED via GPIO.