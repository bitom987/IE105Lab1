#!/usr/bin/python3
  
import socket, ssl, pprint

SERVER_CERT    = './cert.pem'
SERVER_PRIVATE = './key.pem'


context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER) # For Ubuntu 20.04 VM
# context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)      # For Ubuntu 16.04 VM
context.load_cert_chain(SERVER_CERT, SERVER_PRIVATE)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.bind(('192.168.1.188', 3000))
sock.listen(5)

while True:
  client, addr = sock.accept()
  
  print('Connected by', addr)
  while True:
    ssock = context.wrap_socket(newsock, server_side=True)
    print("TLS connection established")
    data = ssock.recv(1024)              # Read data over TLS
    str_data = data.decode("utf8")
    if str_data == "quit":
    	break
    print("Hello " + str_data)
    
    msg = input("Server: ")
    client.sendall(bytes(msg,"utf8"))
    if msg == "quit":
    	break
    	
sock.close()



