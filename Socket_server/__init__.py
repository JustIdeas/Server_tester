import socket


def UDPServer(Rec_Port):

    UDP_IP = "127.0.0.1"
    PORT = int(Rec_Port)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind((UDP_IP, PORT))
    while True:
        data, addr = sock.recvfrom(1024)
        info = data
        print ("Message Received:", info)
        if info.decode() == "Ok":
            print ("foi")
        else:
            print("Não Foi")

def TCPServer(Port):
    print(Port)
    TCP_IP = "127.0.0.1"
    TCP_Port = int(Port)
    BUFFER_SIZE = 20

    tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpSock.bind((TCP_IP, TCP_Port))
    tcpSock.listen(1)

    conn, addr = tcpSock.accept()
    print ("connection address:", addr)

    while True:
        data = conn.recv(BUFFER_SIZE)
        array = data.decode()
        if not data: break
        print ("Message Received:", array)
        conn.send(data)
    conn.close()

def main():
    UDP_IP = "127.0.0.1"
    PORT = 5000

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind((UDP_IP, PORT))
    while True:
        data, addr = sock.recvfrom(1024)
        info = data
        print ("Message Received:", info)
        array = info.decode()
        array = array.split(",")
        print (array[1])

        Port = array[0]
        Prot = array[1]
        if array[1] == 'UDP' :
            print ("UDP")
            UDPServer(Port)
        elif array[1] == 'TCP':
            print("TCP")
            TCPServer(Port)
        else:
            print("Não Foi")


main()