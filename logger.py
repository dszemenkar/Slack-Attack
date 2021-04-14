import os
import datetime

def WriteLog(log):
    txt = open('logs.txt', "a")
    n = txt.write(str(datetime.datetime.now()) + ': ' + log + '\n')
    txt.close()
