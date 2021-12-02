#!/usr/bin/python3
import socket,ssl,pprint
from socket import AF_INET, SOCK_STREAM
from ssl import SSLContext, PROTOCOL_TLS_SERVER

SERVER_CERT    = './cert.pem'
SERVER_PRIVATE = './key.pem'
coHello = 0

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER) # For Ubuntu 20.04 VM
# context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)      # For Ubuntu 16.04 VM
context.load_cert_chain(SERVER_CERT, SERVER_PRIVATE)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
  sock.bind(('192.168.1.188', 3000))
  sock.listen(5)
  tls = context.wrap_socket(sock, server_side=True)
  print ('Connected by ', addr)
  while True:
    data = client.recv(1024)
    str_data = data.decode("utf8")
    recentdata = str_data
    print("Client: ",str_data)
    if str_data == "quit":
      break
    if coHello == 0:
      msg = "Hello " +str_data
      coHello = 99
      client.sendall(bytes(msg,"utf8"))
      while recentdata == str_data:
        data = client.recv(1024)
        str_data = data.decode("utf8")
      print("Client: ",str_data)
    msg = input("Server: ")
    client.sendall(bytes(msg,"utf8"))
    if msg == "quit":
    	break
    	
sock.close()



