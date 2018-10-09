# browser-automation-beyond-firewall
- This repository automates google-chrome browser on MacOS and Ubuntu (neither using chrome-driver or Selenium which are often prohibited by target sites)

- For MacOS, I deploy Appscript to control AppleScriptable Mac OS X applications from Python
- For Ubuntu, I use xdotool to simulate keyboard input and mouse activity, move and resize windows, etc

## Usage
- For MacOS
    - python mac_automation_example.py
- For Ubuntu
    - export DISPLAY=:0
    - python ubuntu_automation_example.py

## References
- For Ubuntu, this code wrapped the automation code from [automate-save-page-as](https://github.com/abiyani/automate-save-page-as) by Python