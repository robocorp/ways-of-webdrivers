*** Settings ***
Library           CustomSelenium
Library           ExtendedSelenium

*** Tasks ***
My Robot Task using Python Selenium Webdriver
    Set Webdriver
    Open Url    https://docs.robocorp.com    screenshot=${OUTPUT_DIR}${/}screen.png
    [Teardown]    Driver Quit

My Robot Task using Extended Selenium Library
    Open Available Browser    https://docs.robocorp.com
    Looking At Element    //a[@href="/docs/courses"]
