from selenium import webdriver

import time
import logininfo
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
browser=webdriver.Chrome(options=options)
browser.get("https://www.instagram.com/")

time.sleep(2)
"""
girisyap=browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[2]/span/p/a/span")
girisyap.click()

time.sleep(2)"""

username=browser.find_element(By.NAME,"username")
password=browser.find_element(By.NAME,"password")

username.send_keys(logininfo.username)
password.send_keys(logininfo.password)

loginbutton=browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button")
loginbutton.click()
browser.maximize_window()

time.sleep(10)

sayfa=browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/span/div/a/div/div[1]/div/div")
sayfa.click()
time.sleep(8)

takip=browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[2]/div/a")
takip.click()
time.sleep(5)

jscommand="""
followers=document.querySelector(".xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6");
followers.scrollTo(0,followers.scrollHeight);
var lenOfPage=followers.scrollHeight;
return lenOfPage;
"""

lenOfPage = browser.execute_script(jscommand)
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script(jscommand)
    if lastCount == lenOfPage:
        match=True
time.sleep(20)
followersList=[]

followers=browser.find_elements(By.CSS_SELECTOR,"._ap3a._aaco._aacw._aacx._aad7._aade")

for follower in followers:

    followersList.append(follower.text)

with open("../followers.txt", "w", encoding="UTF-8") as file:
    for followerr in followersList:
        file.write(followerr + "\n")
kapatma=browser.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button")
kapatma.click()

time.sleep(3)
takipci=browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[3]/div/a")
takipci.click()
time.sleep(3)
jscommandtakipci="""
following=document.querySelector(".xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6");
following.scrollTo(0,following.scrollHeight);
var lenOfPage2=following.scrollHeight;
return lenOfPage2;
"""
lenOfPage2 = browser.execute_script(jscommandtakipci)
match=False
while(match==False):
    lastCount2 = lenOfPage2
    time.sleep(3)
    lenOfPage2 = browser.execute_script(jscommandtakipci)
    if lastCount2 == lenOfPage2:
        match=True
time.sleep(20)
followingList=[]

following=browser.find_elements(By.CSS_SELECTOR,"._ap3a._aaco._aacw._aacx._aad7._aade")
for follower2 in following:

    followingList.append(follower2.text)

with open("../following.txt", "w", encoding="UTF-8") as file:
    for follower2 in followingList:
        file.write(follower2 + "\n")

browser.close()
