import socket
import Server


resultBolean = False

class run:
    def __init__(self, port, ip):
        self.port = port
        self.ip = ip

    def main(self):
        try:
            print("Address port received:", self.port
                  , "Address IP received:", self.ip)
            BUFFER_SIZE = 1024

            tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcpSock.bind((self.ip, int(self.port)))
            tcpSock.listen(1)

            conn, addr = tcpSock.accept()
            print ("connection address:", addr)

            while True:
                data = conn.recv(BUFFER_SIZE)


                array = data.decode()
                array = array.split(",")

                print ("info from array:",array)
                Server.Controller(array).voucher()

                if not data: break
                print ("Result variable:", resultBolean)
                    #if resultBolean == True:
                conn.send('Teste OK'.encode('utf-8'))
            #    else:
                print ("Message Received:", array)
                #conn.send('Not working'.encode('utf-8'))
            conn.close()
        except:
            print("something went wrong with:", Exception, BaseException.args())


run(5001, '127.0.0.1').main()
