import socket
import Server

class Voucher:
    
    def __init__(self, vnumber, ip):
        self.vnumber = vnumber
        self.ip = ip
    
    def Test(self):
        try:
            print("The test has began with voucher number:", self.vnumber, "IP:", self.ip)
            Server.boleanResult = True
        except:
            print("Something went wrong with:", Exception, BaseException.args())
