# coding=utf-8
import csv
import os
import threading

# from common.globalPath import LOG_PATH, LOG_DIR


LOG_DIR = '../LOG/'
LOG_PATH = LOG_DIR + 'refilename.log'

class saveCsvFile():
    _instance = 0

    def __init__(self):
        self.myMutex = threading.Lock()

        if not os.path.exists(LOG_DIR):
            os.makedirs(LOG_DIR)

    @classmethod
    def instance(cls):
        if (cls._instance == 0):
            cls._instance = saveCsvFile()
        return cls._instance

    def RECORD_LOG(self, fileName, li):
        # 记录一条日志
        self.myMutex.acquire()
        self.info(fileName, li)
        self.myMutex.release()

    def info(self, fileName, li):
        if fileName != '':
            LOG_PATH = LOG_DIR + fileName

        self.f = open(LOG_PATH, 'a+', encoding='utf-8', newline='')
        self.writer = csv.writer(self.f)
        self.writer.writerow(li)
        self.f.close()


def SAVE_CSV_FILE(fileName, li, ifprint=True):
    try:
        if ifprint == True:
            print(fileName, li)
        if fileName == '':
            fileName ='not_name.csv'
        saveCsvFile.instance().RECORD_LOG(fileName, li)
    except:
        print("PRINTERROR:MY_RECORD_LOG,except")


