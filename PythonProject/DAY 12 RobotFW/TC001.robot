*** Settings ***
Library    SeleniumLibrary
*** Test Cases ***
    Open Browser    https://www.google.com    chrome
    Title Should Be    Google
    Close Browser
*** Keywords ***
Open Application
    Open Browser    https://example.com    chrome
    Maximize Browser Window
*** Test Cases ***
Launch App Test
    Open Application
    Close Browser
