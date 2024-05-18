#!/usr/bin/env python3

# import RPi.GPIO as gpio
import socket
import time

# gpio.setmode(gpio.BOARD)
# gpio.setup(3,gpio.OUT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client.connect(('localhost',1337))

try:
	while True:
		data = client.recv(1024)
		if (data.decode() == ""):
			client.close()
			break
		else:
			# print(data.decode())
			try:
				if (int(data.decode()) == 1):
					# gpio.output(3, gpio.HIGH)
					print("High shit")
				elif (int(data.decode()) == 0):
					# gpio.output(3, gpio.LOW)
					print("Low shit")
			except:
				print(data.decode())

except KeyboardInterrupt:
	print("Closing connection with server")
	client.close()