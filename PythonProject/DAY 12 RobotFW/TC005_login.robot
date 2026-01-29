*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login\
${Browser}    chrome
${Username}    Admin
${Password}    admin123

*** Keywords ***
Open Application
    Open Browser    ${URL}    ${Browser}
    Maximize Browser Window
    Sleep    2s

Logging in
    Input Text    name:username     ${Username}
    Sleep    2s
    Input Text    name:password     ${Password}
    Sleep    2s
    Click Button    xpath://button[@type="submit"]

*** Test Cases ***
log Into Website
    Open Application
    Sleep    10s
    Capture Page Screenshot    beforelogin.png
    Logging in
    Sleep    5s
    Capture Page Screenshot    afterlogin.png
    ${title}=    Get Title
    Title Should Be    ${title}    OrangeHRM
    Sleep    4s
    Close Browser