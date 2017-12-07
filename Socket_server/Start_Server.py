import socket
import sys

PORT = 5004
class run:

    def __init__(self, port, ip, prot):
        self.port = port
        self.ip   = ip
        self.prot = prot

    def CL_UDP(self):

        UDP_PORT = 5000
        Message = self.port, self.prot, self.ip
        print("UDP IP: ", self.ip)
        print("UDP Port: ", self.port)
        print("message", Message)

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(4000)
        sock.connect((self.ip, UDP_PORT))
        sock.send(str(Message).encode('utf-8'))
        data, server = sock.recvfrom(1024)
        received = data.decode()
        print (received)

    def CL_TCP(self):

        TCP_PORT = 5000
        BUFFER_SIZE = 1024
        Message = int(self.port) + ",TCP" + "," + str(self.ip)

        tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpsock.connect((self.ip
                         , TCP_PORT))
        tcpsock.sendfile(Message)
        data = tcpsock.recv(BUFFER_SIZE)
        tcpsock.close()

        print("Message Received:", data)


run(5005,"127.0.0.1","UDP").CL_UDP()