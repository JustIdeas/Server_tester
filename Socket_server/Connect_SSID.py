import subprocess
import sys

class connect:

    def __init__(self, ssid='intelbras'):
        self.ssid = ssid

    def run(self):
        try:
            print ("SSID: ", self.ssid)
            command = ('iw dev wlp2s0 connect '+str(self.ssid))
            print(command)

            execute = subprocess.getoutput(command)
        except:
            print("Something went wrong module SSID in:", sys.exc_info()[0], sys.exc_info()[1]  )
