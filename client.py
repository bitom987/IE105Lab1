import socket, ssl, sys, pprint
from ssl import SSLContext, PROTOCOL_TLS_CLIENT
from socket import create_connection

hostname='exampleIE105.com'
ip = '192.168.1.187'
port = 3000

context = SSLContext(PROTOCOL_TLS_CLIENT)
context.load_verify_locations('cert.pem')

sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip, port))
input("After making TCP connection. Press any key to go on...")

ssock = context.wrap_socket(sock, server_hostname=hostname, do_handshake_on_connect=False)
ssock.do_handshake()
pprint.pprint(ssock.getpeercert())
input("After handshake. Press any key to continue...")
while True:
    msg = input('Client: ')
    ssock.sendall(bytes(msg, "utf8"))
    if msg == "quit":
       break
    
    data = ssock.recv(1024)
    str_data = data.decode("utf8")
   
    if str_data == "quit":
       print('Server: ', str_data)      
       break
    print('Server: ', str_data)
sock.close()
