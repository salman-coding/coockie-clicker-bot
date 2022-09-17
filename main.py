from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s = Service("D:/development/chrome driver/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
def check_money():
    check_money = driver.find_element(By.ID, "money")
    money_value = check_money.text.split(",")
    formatted_money = ""
    for i in money_value:
        formatted_money += i
    money = int(formatted_money)
    if money >= 123456789:
        time_machine = driver.find_element(By.ID, "buyTime machine")
        time_machine.click()
    elif money >= 1000000:
        portal = driver.find_element(By.ID, "buyPortal")
        portal.click()
    elif money >= 50000:
        alchemy_lab = driver.find_element(By.ID, "buyAlchelabmy ")
        alchemy_lab.click()
    elif money >= 7000:
        shipment = driver.find_element(By.ID, "buyShipment")
        shipment.click()
    elif money >= 2000:
        mine = driver.find_element(By.ID, "buyMine")
        mine.click()
    elif money >= 500:
        factory = driver.find_element(By.ID, "buyFactory")
        factory.click()
    elif money >= 100:
        grandma = driver.find_element(By.ID, "buyGrandma")
        grandma.click()
    else:
        cursor = driver.find_element(By.ID, "buyCursor")
        cursor.click()


time_out = time.time() + 60 * 5
checking_time = time.time() + 5 * 1
while True:
    cookie = driver.find_element(By.ID, "cookie")
    cookie.click()
    if time.time() > checking_time:
        check_money()
    elif time.time() >= time_out:
        break
score_cards = driver.find_element(By.ID, "cps")
print(f"Cookies/Second = {score_cards.text}")

driver.close()
