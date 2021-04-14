import os
import datetime
import backend 

def WriteLog(log):
	backend.insert("logs", log)
    #txt = open('logs.txt', "a")
    #n = txt.write(str(datetime.datetime.now()) + ': ' + log + '\n')
    #txt.close()
