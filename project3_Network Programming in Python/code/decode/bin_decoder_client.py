import socket

host = 'local host'
port = 1234

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', port))
message = input('Enter message: ')
client_socket.send(message.encode())
message = client_socket.recv(1024)

print('Received message: ' + message.decode())

client_socket.close()