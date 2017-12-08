# import socket
# import sys
import Voucher


class Controller:

    def __init__(self, function=None, value=None):
        self.function = function
        self.value = value

    def check(self):
        try:
            print("First",self.function[0])
            self.function[0] = self.function[0].translate(str.maketrans({"(": None}))
            print("Second",self.function[0])
            self.function[0] = self.function[0].translate(str.maketrans({"'": None}))
            print("Inside Voucher def, info:", self.function[0])
            if self.function[0] == "voucher":
                print("Voucher", self.function)

                self.function[1] = self.function[1].translate(str.maketrans({"'": None}))
                self.function[2] = self.function[2].translate(str.maketrans({"'": None}))
                self.function[2] = self.function[2].translate(str.maketrans({")": None}))
                # print ("before", boleanResult)
                result = Voucher.Voucher(self.function[1], self.function[2]).test()
                # print ("after", boleanResult)

                return result
            else:
               print("Não foi", self.function)
        except:
            print("erro occurred in:", BaseException.args())

#def main():
#    try:
#
#        if len(self.function) == 1:
#            print("You need to pass an argument(function)")
#        else:
#            print ("Argument list:", sys.argv)
#
#
#            print("Arguments list array", arguments[1])
#
#            if arguments[1] == "voucher":
#                print("Entrou Arguments Voucher")
#                Controller(arguments[1]).voucher()
#            else:
#                print("Has no function with this name")
#    except:
#        print("An error has occurred in:", BaseException.args())




#main()

