#-*- coding: utf-8 -*-
import os
from appscript import *
import warnings
import webbrowser

warnings.filterwarnings('ignore')

def trick_save(url, fname):
        cmd = """osascript -e 'tell document 1 of application "Safari"
            set URL to "{url}"
            set the_state to missing value
            repeat until the_state is "complete"
                set the_state to (do JavaScript "document.readyState")
                delay 0.2
            end repeat
            delay 4
            set html_returned to missing value
            set html_returned to (do JavaScript "document.body.innerHTML")
            set myFile to open for access "{write_path}" with write permission
            write html_returned to myFile
            close access myFile
            end tell'""".format(url=url, write_path = fname)
        os.system(cmd)
        
if __name__ == "__main__":
    browser = webbrowser.get('safari')
    browser.open("https://www.example.com")

    safari = app("Safari")

    url = 'https://www.example.com'
    cwd = os.getcwd()

    trick_save(url, cwd + "/example.html")


