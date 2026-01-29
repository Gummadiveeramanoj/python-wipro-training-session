*** Settings ***
Library           SeleniumLibrary


*** Test Cases ***
TC002.robot
    Open browser        https://www.google.com      chrome
    Title Should Be         Google
    Close Browser