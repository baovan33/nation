from selenium import webdriver
import time
import os

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get("https://www.instagram.com/")
time.sleep(2)

# Đăng nhập
driver.find_element_by_name("username").send_keys("crawl.selenium")
time.sleep(0.5)
driver.find_element_by_name("password").send_keys("1231123112322132")
# Enter
button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
button.click()
time.sleep(2)

#truy cap trang 2hand
driver.get('https://www.instagram.com/us2hand_sneaker/')
time.sleep(2)

#click vào nut fl
# //*[@id="react-root"]/section/main/div/ul/li[2]/a/span
follow = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
follow.click()
time.sleep(5)

#crawl
for i in range(1,1000):
   scr1 = driver.find_element_by_xpath(f'/html/body/div[6]/div/div/div[2]/ul/div/li[{i}]')
   driver.execute_script("arguments[0].scrollIntoView();", scr1)
   time.sleep(1)
   text = scr1.text
   list = text.encode('utf-8').split()
   dirname = os.path.dirname(os.path.abspath(__file__))
   csvfilename = os.path.join(dirname, "hi.txt")
   file_exists = os.path.isfile(csvfilename)
   f = open(csvfilename,'a')
   f.write(str(list[0]) + "\r\n")
   f.close()
   print('{};{}'.format(i, list[0]))
   #print(i + ";" + list[0])

time.sleep(5)