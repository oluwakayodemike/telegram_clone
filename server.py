import socket
import threading


PORT = 9090
SERVER = '127.0.0.1'

# Address is stored as a tuple
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"

# Lists tcontaining all the clients connected to the server and their usernames.
clients, names = [], []

# Create a new socket for the server
server = socket.socket(socket.AF_INET,
					socket.SOCK_STREAM)

# bind the address of the server to the socket
server.bind(ADDRESS)

# function to start the connection
def startChat():

	print("server is working on " + SERVER)
	
	print(SERVER)


	# listening for connections
	server.listen()

	while True:

		# accept connections and returns a new connection to the client and the address bound to it
		conn, addr = server.accept()
		conn.send("NAME".encode(FORMAT))

		# max amount of data that can be received (bytes) ia 1024
		name = conn.recv(1024).decode(FORMAT)

		# append the name and client to the respective list
		names.append(name)
		clients.append(conn)

		print(f"Userame is : {name}")

		# broadcast message
		broadcastMessage(f"{name} has joined the chat!".encode(FORMAT))

		conn.send('Connection successful!'.encode(FORMAT))

		# Start the handling thread
		thread = threading.Thread(target=handle, args=(conn, addr))
		thread.start()

		# no. of clients connected to the server
		print(f"active connections {threading.active_count()-1}")

# method to handle the incoming messages
def handle(conn, addr):

	print(f"new connection {addr}")
	connected = True
	# receive and broadcast message
	while connected:
		message = conn.recv(1024)
		broadcastMessage(message)

	# close the connection
	conn.close()

# method for broadcasting messages to the each clients
def broadcastMessage(message):
	for client in clients:
		client.send(message)


# call the method to begin the communication
startChat()
