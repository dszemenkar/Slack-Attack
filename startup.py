#! python3
# -*- coding: cp1252 -*-
import time
import pyautogui as ag
import pyperclip as pc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logger
import creds

b = webdriver.Chrome(executable_path=creds.driver)
b.get("https://app.slack.com/client/TDF6VC50W/CDD3LQBNU")

username = creds.username
email = creds.email
password = creds.password

def Tab():
    ag.press('tab')

def Enter():
    ag.press('enter')

def Activate():
    print("Kopplar upp")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("Aktiverar Robot-Jonathan...")
    logger.WriteLog('Start job. Activating robot.')
    time.sleep(1)

def Login():
    time.sleep(10)
    Tab()
    Enter()
    Tab()
    logger.WriteLog('Try to login')
    ag.typewrite(creds.teamname, interval=0.3)
    Enter()
    time.sleep(10)
    ag.typewrite(username, interval=0.3)
    pc.copy('@')
    ag.hotkey('ctrl', 'v')
    ag.typewrite(email, interval=0.3)
    Tab()
    pc.copy(password)
    ag.hotkey('ctrl', 'v')
    Enter()
    time.sleep(30)

def SendMessage(message):
    ag.typewrite(message, interval=0.3)
    Enter()

def EndSession():
    logger.WriteLog('Job done. Ending session')
    b.quit()
