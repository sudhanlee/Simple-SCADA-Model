#!/usr/bin/env python3

# import RPi.GPIO as gpio
import socket
import time


# gpio.setmode(gpio.BOARD)
# gpio.setup(3, gpio.IN)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client.connect(('localhost',1337))

time.sleep(5)

try:
	while True:
		try:
			# data = str(gpio.input(3))
			data = input("Enter data: ")
			# data = "0"
			if data == "":
				client.close()
				break
			client.send(data.encode())
			time.sleep(1)
		except:
			print("Error detected. Trying again...")
			client.close()
			break



except KeyboardInterrupt:
	print("Close connection with server")
	client.close()

