# coding=utf-8

import csv
import datetime
import os
import threading


LOG_DIR = '../LOG/'
ERROR_LOG_PATH = LOG_DIR + 'my_error_log.log'

SAVE_LOG_PATH = LOG_DIR + 'save_csv_log.csv'


class MyLogRecord():
    _instance = 0

    def __init__(self):
        self.thLOCK = threading.Lock()

        if not os.path.exists(LOG_DIR):
            os.makedirs(LOG_DIR)


    @classmethod
    def instance(cls):
        if (cls._instance == 0):
            cls._instance = MyLogRecord()
        return cls._instance

    def ERROR_LOG(self, str):
        self.thLOCK.acquire()
        self.error_log(str)
        self.thLOCK.release()

    def SAVE_FILE_LOG(self, path, li):
        self.thLOCK.acquire()
        self.save_log(path, li)
        self.thLOCK.release()


    def save_log(self, path, li):
        self.f = open(path, 'a+', encoding='utf-8', newline='')
        self.writer = csv.writer(self.f)
        self.writer.writerow(li)
        self.f.close()


    def error_log(self, msg):
        f = open(ERROR_LOG_PATH, 'a+', encoding='utf-8')
        str_time = datetime.datetime.ctime(datetime.datetime.now())
        f.write(str_time)
        f.write(' -- ')
        f.write(msg)
        f.write('\n')
        f.close()



def SAVE_CSV_FILE(fileName, li, ifprint=False):
    try:
        if ifprint == True:
            print(fileName, li)

        if fileName != '':
            SAVE_LOG_PATH = LOG_DIR + '/' + fileName

        MyLogRecord.instance().SAVE_FILE_LOG(SAVE_LOG_PATH, li)
    except:
        print("PRINTERROR:MY_RECORD_LOG,except")


def MY_ERROR_LOG(str, ifprint=False):
    try:
        if ifprint == True:
            print(str)
        MyLogRecord.instance().ERROR_LOG(str)
    except:
        print("PRINTERROR : MY_LOG_ERROR,except")
