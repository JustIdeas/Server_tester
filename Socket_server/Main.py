import socket
import Server_TCP as srvTcp
import Server_UDP as srvUdp


def main():
    UDP_IP = '127.0.0.1'
    PORT = 5000

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind((UDP_IP, PORT))
    while True:
        try:

            data, addr = sock.recvfrom(1024)
            info = data
            print ("Message Received:", info)
            if info != None:
                array = info.decode()
                array = array.split(",")
                print (array[1].translate(str.maketrans({"'":None})))

                Port = array[0].translate(str.maketrans({"'":None}))
                Port = array[0].translate(str.maketrans({"(": None}))
                Port = Port.strip()

                Prot = array[1].translate(str.maketrans({"'":None}))
                Prot = Prot.strip()

                IP = array[2]
                #IP   = array[2].translate(str.maketrans({"'":None}))
                IP   = array[2].translate(str.maketrans({")": None}))
                IP   = IP.strip()
                IP   = IP.translate(str.maketrans({"'":None}))


                if Prot == "UDP" :
                    print ("UDP")
                    print (int(Port))
                    print (str(IP))
                    srvUdp.run(Port, IP).main()
                elif Prot.strip == "TCP":
                    print("TCP")
                    srvTcp.run(Port, IP).main()
                else:
                    print("Não Foi")
        except ValueError:
            print("Something went wrong with:", Exception.args)

main()