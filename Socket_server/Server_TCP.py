import socket
import sys

from Server import Controller

BUFFER_SIZE = 1024


class Run:
    def __init__(self, port, ip):
        self.port = port
        self.ip = ip

    def main(self):
        try:
            print("Address port received:", self.port
                  , "Address IP received:", self.ip)

            tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp_sock.bind((self.ip, int(self.port)))
            tcp_sock.listen(1)

            conn, addr = tcp_sock.accept()
            print("connection address:", addr)

            while True:
                data = conn.recv(BUFFER_SIZE)

                array = data.decode()
                array = array.split(",")

                print("info from array:",array)
                result = Controller(array).check()

                if not data: break
                # print("Result variable:", resultBolean)
                if result:
                    conn.send('Teste OK'.encode('utf-8'))
                else:
                    print("Message Received:", array)
                    conn.send('Not working'.encode('utf-8'))
            conn.close()
        except:
            print("something went wrong with:", sys.exc_info()[0], sys.exc_info()[1])


Run(5001, '127.0.0.1').main()
