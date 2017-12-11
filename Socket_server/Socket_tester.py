import socket
import sys
from time import sleep



class sock:

    def __init__(self, ip, time=0):
        self.ip = ip
        self.time = time*60+30

    def run(self):
        i = 0
        control_variable = 0

        try:
            print(self.time)

            while i < 2:
                print('Entrou while')
                init = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                init.settimeout(5)
                init.connect((self.ip, 53))
                # init.timeout(3)
                init.shutdown(2)
                control_variable = control_variable + 1
                sleep(self.time)
                i = i + 1

        except socket.error as e:
            print("Cannot connect to ", self.ip)
            control_variable = control_variable - 1
            print("Something went wrong inside of Socket_teste module:", sys.exc_info()[0], sys.exc_info()[1])

        if control_variable == 0:
            print("OK", control_variable)
            return True
        else:
            print("NOK", control_variable)
            return False


