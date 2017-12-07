import socket

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
print(received)