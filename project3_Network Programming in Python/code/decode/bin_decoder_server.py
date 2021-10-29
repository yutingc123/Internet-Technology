import socket

host = 'local host'
port = 1234
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', port))
server_socket.listen()
client, address = server_socket.accept()

print("Connection from: ", str(address))

message = client.recv(1024)
binaryString = message.decode()
binaryValues = binaryString.split()
asciiString = ""
for binaryValue in binaryValues:
    integer = int(binaryValue, 2)
    asciiCharacter = chr(integer)
    asciiString += asciiCharacter

message = asciiString 
client.send(message.encode())

client.close()