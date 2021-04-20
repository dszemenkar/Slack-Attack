#! python3
# -*- coding: cp1252 -*-
import bs4
import requests
import datetime
import logger
import random

def ThisDayInHistory():
    child = random.randint(1, 4)
    res = requests.get('https://en.wikipedia.org/wiki/Main_Page')
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    day = soup.select("#mp-otd > ul > li:nth-child(" + str(child) + ")")
    try:
        dayStr =' This day in history: ' + day[0].text + ' '
    except:
        logger.WriteLog('Did not fetch history')
        dayStr = ""
    return dayStr

def UselessInformation():
    dateTimeInstance = datetime.datetime.now()
    #if 0 or 2 or 4 == dateTimeInstance.weekday():
    child = random.randint(1, 30)
    res = requests.get('https://www.kickassfacts.com/fact-of-the-day/')
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    day = soup.select("#post-39039 > div.share-container > div > div > ol > li:nth-child(" + str(child) + ")")
    try:
        size = len(day[0].text)
        mod_string = day[0].text[:size - 9]
        dayStr = 'Some random facts of the day: ' + mod_string + '. '
    except:
        logger.WriteLog('Did not fetch useless information')
        dayStr = ""
    return dayStr

def DidYouKnow():
    dateTimeInstance = datetime.datetime.now()
    if 5 or 3 or 1 == dateTimeInstance.weekday():
        child = random.randint(1, 7)
        res = requests.get('https://en.wikipedia.org/wiki/Main_Page')
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        try:
            day = soup.select("#mp-dyk > ul > li:nth-child(" + str(child) + ")")
            dayStr = 'Did you know' + day[0].text + ' '
        except:
            logger.WriteLog('Did not fetch did-you-know')
            dayStr = ""
    return dayStr

def GetTodaysDay():
    res = requests.get('https://nationaldaycalendar.com/what-day-is-it/')
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    day = soup.select('#et-boc > div > div > div > div.et_pb_row.et_pb_row_0 > div > div.et_pb_module.et_pb_text.et_pb_text_0.et_pb_text_align_left.et_pb_bg_layout_light > div > ul:nth-child(3) > li:nth-child(1) > h3 > a')
    try:
        dayStr = 'Todays day is ' + day[0].text + '!'
    except:
        logger.WriteLog('Did not fetch theme')
        dayStr = ""
    return dayStr

def GetTodaysWeather():
    res = requests.get('https://www.timeanddate.com/weather/sweden/vaxjo')
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    wstr = ""
    try: 
        temp = soup.select('#qlook > div.h2')
        wstr = " The temperature is right now: " + str(temp[0].text + ", ")

        weather = soup.select('#qlook > p:nth-child(6)')
        split_string = weather[0].text.split("c")

        feels = split_string[0].lower()
        size = len(feels)
        mod_string = feels[:size - 4]
        wstr = wstr + "but it " + mod_string + "."
    except:
        wstr = " I haven't found out about the weather today. Unable to look out the window. Who placed me here? "
    return wstr

def GetDailyYoutubeLink():
    res = requests.get('http://www.randomvideogenerator.com/')
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    tag = soup.select('#video > iframe')[0]['src']
    intro = "\n\nFeel free to check out this random youtube video to kickstart your day!: "
    try:
        ytLink = intro + tag + "\n\n"
    except:
        ytLink = "Youtube did not have any cool videos today, check back again tomorrow."
    return ytLink
