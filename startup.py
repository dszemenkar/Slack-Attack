#! python3
# -*- coding: cp1252 -*-
import time
import pyautogui as ag
import pyperclip as pc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logger

chromedriver = '/Users/davidszemenkar/Documents/robo-jon/chromedriver'
b = webdriver.Chrome(chromedriver)
b.get("https://app.slack.com/client/TDF6VC50W/CDD3LQBNU")

username = "myusername"
email = "myemail"
password = "password"


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
    time.sleep(25)
    Tab()
    Enter()
    Tab()
    logger.WriteLog('Try to login')
    for letter in "capvxjtechteam":
        ag.press(letter)
    Enter()
    time.sleep(15)
    for letter in username:
        ag.press(letter)
    pc.copy('@')
    ag.hotkey('ctrl', 'v')
    for letter in email:
        ag.press(letter)
    Tab()
    for letter in password:
        ag.press(letter)
    Enter()
    time.sleep(20)

def SendMessage(message):
    i = 0
    #while i < 10:
    #    Tab()
     #   i = i + 1
    for letter in message:
        if letter == 'å':
            pc.copy('å')
            ag.hotkey('ctrl', 'v')
        if letter == 'ä':
            pc.copy('ä')
            ag.hotkey('ctrl', 'v')
        if letter == 'ö':
            pc.copy('ö')
            ag.hotkey('ctrl', 'v')
        ag.press(letter)
    Enter()

def EndSession():
    logger.WriteLog('Job done. Ending session')
    b.quit()
