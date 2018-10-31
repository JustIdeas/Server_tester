# import socket
# import sys
from Test_Cases import Voucher


class Controller:

    def __init__(self, function=None, value=None):
        self.function = function
        self.value = value

    def check(self):
        try:
            print(self.function["code"])

            if self.function["code"] == 1:
                print("Voucher", self.function)
                result = Voucher.Voucher(self.function["voucher"], self.function["time"], self.function["ssid"]).test()
                return result

            else:
               print("Não foi", self.function)

        except:
            print("erro occurred in:", BaseException.args())