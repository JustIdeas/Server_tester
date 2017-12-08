# import socket
import sys
from selenium import webdriver

from Socket_tester import sock
from Connect_SSID import connect


class Voucher:
    
    def __init__(self, vnumber, ip):
        self.vnumber = vnumber
        self.ip = ip
    
    def test(self):
        try:

            print("The test has began with voucher number:", self.vnumber, "IP:", self.ip)
            connect("__keep_out__").run()

            browser = webdriver.Chrome('/home/lu050023/ChromeDriver/chromedriver')
            browser.get('www.ufsc.br')
            result = sock('8.8.8.8', 15).run()

            if result:
                print("Success Socket!")
                return True

            else:
                print("Error Socket!")
                return False


        except:
            print("Something went wrong with:", sys.exc_info()[0], sys.exc_info()[1])
