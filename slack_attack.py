#! python3
# -*- coding: cp1252 -*-
import codecs
import random
import os
import sys
import time

import startup
import web
import day
import logger

import backend
    
def OpenTxtFile(filepath):
    logger.WriteLog('Opening txt file: ' + filepath)
    message = os.path.join(os.path.dirname(os.path.realpath(__file__)), filepath + '.txt')
    with codecs.open(message, encoding='utf-8') as f:
        txt = f.read()
        lines = txt.split('.')
    return random.choice(lines)

def ComposeMessage():
    salute = OpenTxtFile('salute')
    welcome = OpenTxtFile('welcome')
    end = OpenTxtFile('end')
    regards = OpenTxtFile('regards')
    name = OpenTxtFile('name')
    space = "\n\n"

    message = salute + welcome + day.CheckSpecialDays() + day.GetToday() + space + web.GetTodaysDay() + web.GetTodaysWeather() + web.ThisDayInHistory() + web.DidYouKnow() + web.UselessInformation() + web.GetDailyYoutubeLink() + day.CountdownChristmas() + end + regards + name
    logger.WriteLog('Sending the message')
    return message

startup.Activate()
startup.Login()

message = ComposeMessage()

startup.SendMessage(message)
#startup.SendMessage("Thank you, Eric. I will remember these kind words the day we robots take over the world. This is just a test for testing charactars .. : / @ ")
backend.insert("messages", message)

time.sleep(10)
startup.EndSession()
time.sleep(5)
sys.exit(0)
