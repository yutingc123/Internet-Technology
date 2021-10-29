import socket
host = 'local host'
port = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', port))
server_socket.listen()
client, address = server_socket.accept()

print("Connection from: ", str(address))

message = client.recv(1024)
message = ' '.join('{0:08b}'.format(ord(x), 'b') for x in message.decode())
client.send(message.encode())

client.close()