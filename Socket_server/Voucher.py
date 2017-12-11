# import socket
import sys
from selenium import webdriver

from Socket_tester import sock
from Connect_SSID import connect


class Voucher:
    
    def __init__(self, vnumber, time=90, ssid='__keep_out__'):
        self.vnumber = vnumber
        self.time = time
        self.ssid = ssid
    
    def test(self):
        try:

            print("The test has began with voucher number:", self.vnumber, "time:", self.time, "ssid:", self.ssid)
            result = connect(self.ssid).run()
            if result:
                print("in test, result is:", result)
                options = webdriver.ChromeOptions()
                options.add_argument('--no-sandbox')
                browser = webdriver.Chrome('/home/lu050023/ChromeDriver/chromedriver', chrome_options=options)
                browser.set_page_load_timeout(10)
                browser.get('http://www.ufsc.br')
                browser.find_element_by_id("voucher").send_keys(self.vnumber)
                browser.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[2]/button").click()
                try:
                    urlAlert = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[@class=\'alert alert-danger\']")
                    print("Atingiu o tempo limite")
                    return False

                except:
                    print("exception urlAlert")



                try:
                    urlSucc = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[@class=\'alert alert-success\']")
                    print("check in success")
                    result = sock('8.8.8.8', self.time).run()

                except:
                    print("exception urlSucc")
                    return False

                if result:
                    print("Success Socket!")
                    return True

                else:
                    print("Error Socket!")
                    return False
            else:
                print("in Voucher, was not able to connect on SSID: ", self.ssid["ssid"], result)
                return False

        except:
            print("Something went wrong on Voucher module with:", sys.exc_info()[0], sys.exc_info()[1])

