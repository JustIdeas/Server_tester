import socket
import sys
import json

from Controller import Controller

BUFFER_SIZE = 512


class Run:
    def __init__(self, port, ip):
        self.port = port
        self.ip = ip

    def main(self):

        print("Address port received:", self.port
              , "Address IP received:", self.ip)

        tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_sock.bind((self.ip, int(self.port)))
        tcp_sock.listen(1)
        try:

            while True:
                conn, addr = tcp_sock.accept()
                print("connection address:", addr)

                while True:
                    data = conn.recv(BUFFER_SIZE)
                    array = json.loads(data.decode())
                    print("info from array:", array)
                    result = Controller(array).check()

                    if not data: break
                    if result:
                        conn.send('Teste OK'.encode('utf-8'))
                    else:
                        print("Message Received:", array)
                        conn.send('Not working'.encode('utf-8'))

        except:
            print("something went wrong on module Server TCP with:", sys.exc_info()[0], sys.exc_info()[1])
            conn.close()
            tcp_sock.close()
            Run(5001, '127.0.0.1').main()

if __name__ == '__main__':
    Run(5001, '127.0.0.1').main()
