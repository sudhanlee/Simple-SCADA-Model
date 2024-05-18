#!/usr/bin/env python3

import socket
import threading
import time

def receive_message():
	while True:
		data = sensor_client.recv(1024)
		data = data.decode()
		print(data, type(data))
		if data == "":
			print('Sensor client connection closed...')
			send_message('Sensor client disconnected')
			sensor_client.close()
			break
		else:
			send_message(data)


def send_message(data):
	try:
		# print(data)
		action_client.send(data.encode())

		# if (int(data) >= 40):
		# 	action_client.send('0'.encode())
		# else:
		# 	action_client.send('1'.encode())
	except:
		print("Client error")
		action_client.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('localhost',1337))
server.listen(5)

print("Server listening on port 9999...")

try:

	
	sensor_client, sensor_addr = server.accept()
	print("Conneted to the sensor client...")
	sensor_thread = threading.Thread(target=receive_message, args=())
	sensor_thread.start()

	action_client, action_address = server.accept()

	print("Connected to the actuator client")

	while True:
		pass

except KeyboardInterrupt:
	print("Problem")
	exit(1)