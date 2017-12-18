# import socket
# import sys
import Voucher
import CPF
import Cad_ind
import Simp_pass
class Controller:

    def __init__(self, function=None):
        self.function = function

    def check(self):
        try:
            print(self.function["code"])

            if self.function["code"] == 1:
                print("Voucher", self.function)
                result = Voucher.Voucher(self.function["voucher"], self.function["time"], self.function["ssid"]).test()
                return result

            elif self.function["code"] == 2:
                print("CPF", self.function)
                result = CPF.CPF(self.function["cpf"], self.function["time"], self.function["ssid"]).test()
                return result

            elif self.function["code"] == 3:
                print("Cadastro Individual", self.function)
                result = Cad_ind.Cad_ind(self.function["cpf"], self.function["time"], self.function["ssid"], self.function["telefone"], self.function["email"], self.function["nome"]).test()
                return result

            elif self.function["code"] == 4:
                print("Senha Simples    ", self.function)
                result = Simp_pass.Simp_pass(self.function["password"], self.function["time"], self.function["ssid"]).test()
                return result

            else:
               print("Não foi", self.function)

        except:
            print("erro occurred in:", BaseException.args())