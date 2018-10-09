#-*- coding: utf-8 -*-
import os
import warnings
import time
warnings.filterwarnings('ignore')

def trick_open(url, fname):
    cmd = "./save_page_as_multiple_open '{}' --destination '{}'".format(url, fname)
    os.system(cmd)

def trick_save(url, fname):
    cmd = "./save_page_as_multiple_save '{}' --destination '{}'".format(url, fname)
    os.system(cmd)

if __name__ == "__main__":
    url = 'https://www.example.com'
    cwd = os.getcwd()

    for i in range(5):
        trick_open(url, cwd + "/example{}.html".format(i))
    
    time.sleep(10)

    for i in reversed(range(5)):
        trick_save(url, cwd + "/example{}.html".format(i))
        