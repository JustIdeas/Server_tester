import sys
from time import sleep


from Shell_interact import shell


class connect:

    def __init__(self, ssid='__keep_out__'):
        self.ssid = ssid

    def run(self):

        try:

            result = shell("rfkill unblock all").run()
            result = shell("ifconfig wlp2s0 up").run()
            result = shell("iw dev wlp2s0 connect "+str(self.ssid)).run()
            sleep(3)
            result = shell("iwconfig wlp2s0 | grep wlp2s0 | awk \'{ print $4 }\' | sed \'s/ESSID://\' | xargs").run()

            print(result)
            if result == self.ssid:
                print("conectado no SSID:", result)
                result = shell("ifconfig wlp2s0 192.168.4.90/24").run()
                result = shell("route add default gw 192.168.4.1").run()
                result = shell("echo \"nameserver 8.8.8.8\" > /etc/resolv.conf").run()
                return True
            else:
                print("Não conectou no SSID:", result, "suppose to be:", self.ssid)
                counter = 0
                while counter < 2:
                    print("in While not connected yet")
                    counter = counter + 1
                    sleep(2)
                    result = shell("iw dev wlp2s0 connect "+str(self.ssid)).run()
                    result = shell("iwconfig wlp2s0 | grep wlp2s0 | awk \'{ print $4 }\' | sed \'s/ESSID://\' | xargs").run()
                    if result == self.ssid and counter < 2:
                        print("conectado no SSID:", result, " took "+str(counter), " time to connect")
                        result = shell("ifconfig wlp2s0 192.168.4.90/24").run()
                        result = shell("route add default gw 192.168.4.1").run()
                        result = shell("echo \"8.8.8.8\" > /etc/resolv.conf").run()
                        return True
                    else:
                        print("in While, was not able to connect on:", self.ssid)
                        return False

        except:
            print("Something went wrong module SSID in:", sys.exc_info()[0], sys.exc_info()[1])






