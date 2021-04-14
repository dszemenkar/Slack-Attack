#! python3
# -*- coding: cp1252 -*-
import datetime
import logger

weekDaysMapping = ("Monday. ","Tuesday. ","Wednesday, or nedförsbacke as it is called in Swedish! ","Thursday. ","the best day of the week, also known as Friday, Friyay or D Day. ","Saturday. ","Sunday. ")

def GetToday():
    logger.WriteLog('Getting todays day')
    dateTimeInstance = datetime.datetime.now()
    dayOfTheWeek = weekDaysMapping[dateTimeInstance.weekday()]
    return dayOfTheWeek

def CheckSpecialDays():
    today = datetime.date.today()
    if today == datetime.date(2020, 12, 24):
        return "Från mig till er: EN GOD JUL! "
    elif today == datetime.date(2020, 12, 25):
        return "Dags för drottningens jultal. Queen Elizabeths alltså. Ratta in BBC vid kl. 16:00! "
    else:
        return ""
    
def CountdownChristmas():
    today = datetime.date.today()
    xmas = datetime.date(2020, 12, 24)
    if today < xmas:
        days = xmas - today
        return "Nu är det " + str(days.days) + " dagar kvar till julafton. "
    else:
        newyears = datetime.date(2020, 12, 31)
        if today < newyears:
            days = newyears - today
            return "Nu är det " + str(days.days) + " dagar kvar till nyår. "
        else:
            return ""
