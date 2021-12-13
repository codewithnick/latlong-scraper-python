import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import csv
import traceback
class Semaphore:
    fileinuse=False
f=open("address.txt")
txt=f.read().split("\n")
f.close()
print(txt)
def find(i):
    try:
        # selenium-wire proxy settings
        wire_options = {
            'proxy': {
                "http": "http://rwqlrvti-rotate:kv9fmbc8ffka@p.webshare.io:80/",
                "https": "http://rwqlrvti-rotate:kv9fmbc8ffka@p.webshare.io:80/"
            }  
        }

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--ignore-certificate-errors-spki-list')
        chrome_options.add_argument('--ignore-ssl-errors')
        chrome_options.add_argument('--disable-gpu')

        driver=webdriver.Chrome(executable_path=r"chromedriver.exe", options=chrome_options )
        driver.get("https://www.doogal.co.uk/LatLong.php")
        time.sleep(1)
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/button[1]').click()
        except:
            pass
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3);")
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[1]/h4').click()
        time.sleep(1)
        driver.find_element_by_id("postcode").send_keys(i)
        time.sleep(1)
        driver.execute_script("latLng.geocode()")
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[1]/h4').click()
        time.sleep(1)
        a=''#driver.find_element_by_id("latlngspan").text
        b=driver.find_element_by_id("lat").get_attribute('value')
        time.sleep(1)
        c=driver.find_element_by_id("long").get_attribute('value')
        driver.close()
        print(a,b,c)
        while(Semaphore.fileinuse):
            time.sleep(1)
        Semaphore.fileinuse=True
        with open('csv_file.csv', 'a') as f:
            # create the csv writer
            writer = csv.writer(f)

            # write a row to the csv file
            writer.writerow([i,b,c])
        if len(b)>1 and len(c) >1:
            f=open("completed.txt","a")
            f.write(i+'\n')
            f.close()
        Semaphore.fileinuse=False
    except:
        traceback.print_exc()
#adding incomplete statement
f=open("completed.txt")
completed=f.read().split('\n')
f.close()
f=open("address.txt")
total=f.read().split('\n')
f.close()
f=open("address.txt","w")
incomplete=list(set(total)-set(completed))
print(incomplete)
for i in incomplete:
    f.write(i+"\n")
f.close()
# importing the threading module

import threading
for i in txt:
    t1 = threading.Thread(target=find, args=(i,))
    t1.start()
    seconds_between_each_thread=0.3
    time.sleep(seconds_between_each_thread)

