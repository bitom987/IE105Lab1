import socket, ssl, sys, pprint

hostname='example.org'
ip = '192.168.1.188'
port = 3000
context = SSLContext(PROTOCOL_TLS_CLIENT)
context.load_verify_locations('cert.pem')

sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
sock.connect((hostname, port))
input("After making TCP connection. Press any key to go on...")

ssock = context.wrap_socket(sock, server_hostname=hostname, do_handshake_on_connect=False)

ssock.do_handshake()
pprint.pprint(ssock.getpeercert())
input("After handshake. Press any key to continue...")
while True:
    msg = input('Client: ')
    sock.sendall(bytes(msg, "utf8"))

    if msg == "quit":
        break
    
    data = sock.recv(1024)

    print('Server: ' + data.decode("utf8"))
sock.close()
sock.close()
