# import socket
import sys
from Socket_tester import sock


class Voucher:
    
    def __init__(self, vnumber, ip):
        self.vnumber = vnumber
        self.ip = ip
    
    def test(self):
        try:

            print("The test has began with voucher number:", self.vnumber, "IP:", self.ip)
            result = sock('8.8.8.8', 15).run()

            if result:
                print("Success Socket!")
            else:
                print("Error Socket!")

            return True
        except:
            print("Something went wrong with:", sys.exc_info()[0], sys.exc_info()[1])
