from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

import time
from gtts import gTTS
from config import CHROME_PROFILE_PATH
import google_search as search
import g_translate as translator
import ChatBot as wiki
import YT_search as youtubeSearch
import YT_Download as videoDownloader

options = webdriver.ChromeOptions()
options.add_argument(CHROME_PROFILE_PATH)
driver = webdriver.Chrome(executable_path="/home/adhil/Downloads/chromedriver_linux64/chromedriver",options=options)
driver.get("https://web.whatsapp.com")

print("Scan QR Code, And then Enter")
input()
print("Logged In")

inp_xpath_search = '//span[@title="BOT"]'
input_box_search = WebDriverWait(driver, 50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
input_box_search.click()
time.sleep(5.4)

mesg_box_xpath = '//div[@class="_1awRl copyable-text selectable-text"][@data-tab="6"][@dir="ltr"]'

temp = ""

msg_xpath = '//div[@class="_1RAno message-in focusable-list-item"]'
message = WebDriverWait(driver, 50).until(lambda driver: driver.find_elements_by_xpath(msg_xpath))
messageBox = driver.find_element_by_xpath(xpath=mesg_box_xpath)

messageBox.send_keys("Started" + Keys.ENTER)
messageBox.send_keys("To convert text into audio use the format\nAUD SAMPLE TEXT" + Keys.ENTER)
messageBox.send_keys("For google search use the format\nGOOGLE SAMPLE TEXT" + Keys.ENTER)
messageBox.send_keys("To translate english to malayalam use the format\nTRANS_ML SAMPLE TEXT" + Keys.ENTER)
messageBox.send_keys("For youtube search\nYT SAMPLE TEXT" + Keys.ENTER)

size = len(message) - 1

print(message)

attach_btn = driver.find_element_by_xpath('//span[@data-testid="clip"]')

while True:
    try:
        message = driver.find_elements_by_xpath(msg_xpath)
        size = len(message) - 1
        if temp == "":
            temp = message[size]
        elif temp != message[size]:
            texts = message[size].text.split('\n')
            print(texts[0])
            if "AUD" in texts[1]:
                try:
                    print("Yes")
                    string = texts[1].replace('AUD', '')
                    audFile = gTTS(text=string, lang="en", slow=False)
                    file_name = string[:4] + ".mp3".replace(' ', '')

                    audFile.save(file_name)
                    attach_btn.click()
                    time.sleep(1)

                    doc_atach_btn = myElem = driver.find_element_by_xpath('//input[@type="file"]')
                    path = '/home/adhil/PycharmProjects/WhatsappBot/' + file_name
                    print(path)
                    doc_atach_btn.send_keys(path)

                    send_button = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//span[@data-testid="send"][@data-icon="send"]')))
                    send_button.click()
                except:
                    messageBox.send_keys("An error occurred. try again" + Keys.ENTER)
            elif "GOOGLE" in texts[1]:
                try:
                    messageBox.send_keys(search.getGoogleResult(texts[1].replace("GOOGLE","")) + Keys.ENTER)
                except:
                    messageBox.send_keys("An error occurred. try again" + Keys.ENTER)
            elif "TRANS_ML" in texts[1]:
                try:
                    malayalamTrans = translator.convertToMalayalam(texts[1].replace("TRANS_ML",""))
                    messageBox.send_keys( malayalamTrans+ Keys.ENTER)
                except:
                    messageBox.send_keys("An error occurred. try again" + Keys.ENTER)
            elif "YT" in texts[1]:
                try:
                    messageBox.send_keys(youtubeSearch.search(texts[1].replace("YT","")) + Keys.ENTER)
                except:
                    messageBox.send_keys("An error occurred. try again" + Keys.ENTER)
            elif "YOU_DOWN" in texts[1]:
                link = texts[1].replace("YOU_DOWN","")
                link = link.replace(" ","")
                path = videoDownloader.downloadVideo(link)

                attach_btn.click()
                time.sleep(1)

                doc_atach_btn = myElem = driver.find_element_by_xpath('//input[@type="file"]')
                print(path)
                doc_atach_btn.send_keys(path)

                send_button = WebDriverWait(driver, 100).until(
                    EC.presence_of_element_located((By.XPATH, '//span[@data-testid="send"][@data-icon="send"]')))
                send_button.click()

            else:
                messageBox.send_keys( wiki.getResult(texts[1])+Keys.ENTER)
    except:
        messageBox.send_keys("An error occurred. try again" + Keys.ENTER)
    temp = message[size]




