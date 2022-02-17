from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import selenium
import shutil
import os
from datetime import date, datetime
import time
import creds
import random

##Variables defined.
login_page = "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&"
amd5900x = "https://www.amazon.com/dp/B08164VTWH?ie=UTF8&tag=hotstock0e7-20"
test_link = "https://www.amazon.com/AMD-Ryzen-3950X-32-Thread-Processor/dp/B07ZTYKLZW/ref=sr_1_1?dchild=1&keywords=ryzen+5900&qid=1606523573&sr=8-1"
amd5800x = "https://www.amazon.com/AMD-Ryzen-5800X-16-Thread-Processor/dp/B0815XFSGK"


#function to log into amazon using the creds from creds.py file.
def login_to_amazon(Driver):
    Driver.get(login_page)
    time.sleep(2)
    # Driver.find_element_by_id("submit.buy-now").click()
    email_input = Driver.find_element_by_id("ap_email")
    email_input.send_keys(creds.username)
    Driver.find_element_by_id("continue").click()
    time.sleep(1)
    pass_input = Driver.find_element_by_id("ap_password")
    pass_input.send_keys(creds.password)
    time.sleep(1)
    Driver.find_element_by_name("rememberMe").click()
    email_input = Driver.find_element_by_id("signInSubmit").click()
    print("Check Phone if need to verify")
    time.sleep(10)




## can turn on headless if dont want to see window.
options = Options()
# options.add_argument("--no-sandbox")
# options.add_argument("--remote-debugging-port=9222") 
options.add_argument(r"--user-data-dir=C:\Users\NS\AppData\Local\Google\Chrome\User Data\Profile 1")
# options.add_argument("--headless")
# options.add_argument("--window-size=1920,1080")
options.add_experimental_option("excludeSwitches", ["enable-automation","disable-popup-blocking"])
options.add_experimental_option('useAutomationExtension', False)
# options.add_argument("--disable-dev-shm-usage")
AmazonDriver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
print ("Headless Chrome Initialized")
# params = {'behavior': 'allow', 'downloadPath': DownloadLocation}
# MintDriver.execute_cdp_cmd('Page.setDownloadBehavior', params)
try:
    login_to_amazon(AmazonDriver)
except:
    print("Cant Login")


# while True:
#     print("Navigate to link")
#     AmazonDriver.get(test_link)
#     element = WebDriverWait(AmazonDriver, 5).until(EC.presence_of_element_located((By.ID, "buy-now-button")))
#     # print(element)
#     if element:
#         print("CLickedBuy Now Button Found")
#         AmazonDriver.find_element_by_id("buy-now-button").click()
#         # time.sleep(1200)
#         try:
#             element1 = WebDriverWait(AmazonDriver, 5).until(EC.presence_of_element_located((By.NAME, "placeYourOrder1")))
#             print(element1)
#             print("First Element")
#             if element1:
#                 try:
#                     AmazonDriver.find_element_by_name("placeYourOrder1").click()
#                     print("PlacedYourOrder Button Found")
#                     time.sleep(5)
#                     print("Bought Items!")
#                     break
#                 except:
#                     pass
#         except:
#             print("No STANDARD check out Place your order button found")
#             try:
#                 AmazonDriver.find_element_by_id("buy-now-button").send_keys(Keys.SPACE)
#                 print("Second Element")

#                 no_thanks = WebDriverWait(AmazonDriver, 10).until(EC.presence_of_element_located((By.ID, 'turbo-checkout-iframe')))
#                 if no_thanks:
#                     AmazonDriver.switch_to.frame("turbo-checkout-iframe")
                    
#                 element2 = WebDriverWait(AmazonDriver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="turbo-checkout-pyo-button"]')))
#                 print(element2)
#                 if element2:
#                     try:
#                         AmazonDriver.find_element_by_xpath('//*[@id="turbo-checkout-pyo-button"]').click()
#                         print("Turbo PlacedYourOrder Button Found")
#                         time.sleep(5)
#                         print("Bought Items!")
#                         break
#                     except:
#                         pass
#             except:
#                 print("No TURBO Check out Place your order Found")
#                 AmazonDriver.switch_to.default_content()
#     sleeptime = random.randrange(0,5)
#     print(f"Sleeping for {sleeptime} seconds")
#     time.sleep(sleeptime)

#While loop that is used to scan and purchase.
while True:
    print("Navigate to link")
    AmazonDriver.get(amd5800x)
    try:
        element = WebDriverWait(AmazonDriver, 5).until(EC.presence_of_element_located((By.ID, "buy-now-button")))
        # print(element)
        if element:
            print("CLickedBuy Now Button Found")
            AmazonDriver.find_element_by_id("buy-now-button").click()
            # time.sleep(1200)
            try:
                AmazonDriver.find_element_by_id("buy-now-button").send_keys(Keys.SPACE)
                print("Second Element")
                no_thanks = WebDriverWait(AmazonDriver, 2).until(EC.presence_of_element_located((By.ID, 'turbo-checkout-iframe')))
                if no_thanks:
                    AmazonDriver.switch_to.frame("turbo-checkout-iframe")
                element2 = WebDriverWait(AmazonDriver, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="turbo-checkout-pyo-button"]')))
                print(element2)
                if element2:
                    try:
                        AmazonDriver.find_element_by_xpath('//*[@id="turbo-checkout-pyo-button"]').click()
                        print("Turbo PlacedYourOrder Button Found")
                        time.sleep(5)
                        print("Bought Items!")
                        break
                    except:
                        pass
            except:
                print("No TURBO Check out Place your order Found")
                AmazonDriver.switch_to.default_content()
                try:
                    element1 = WebDriverWait(AmazonDriver, 2).until(EC.presence_of_element_located((By.NAME, "placeYourOrder1")))
                    print(element1)
                    print("First Element")
                    if element1:
                        try:
                            AmazonDriver.find_element_by_name("placeYourOrder1").click()
                            print("PlacedYourOrder Button Found")
                            time.sleep(5)
                            print("Bought Items!")
                            break
                        except:
                            pass
                except:
                    print("No Standard PlaceYourOrder Button Found")
    except:
        print("No Buy Now Button Found")

    # sleeptime = random.randrange(0,5)
    # print(f"Sleeping for {sleeptime} seconds")
    # time.sleep(sleeptime)
