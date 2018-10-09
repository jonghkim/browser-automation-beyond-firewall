#-*- coding: utf-8 -*-
import os
import warnings
warnings.filterwarnings('ignore')

def trick_save(url, fname):
    cmd = "./save_page_as '{}' --destination '{}'".format(url, fname)
    os.system(cmd)

if __name__ == "__main__":
    url = 'https://www.example.com'
    cwd = os.getcwd()

    trick_save(url, cwd + "/example.html")