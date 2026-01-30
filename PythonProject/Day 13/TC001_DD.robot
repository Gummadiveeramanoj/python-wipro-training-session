*** Settings ***
Library   SeleniumLibrary

*** Variables ***
${url}     https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}       firefox
*** Keywords ***
open orangehrm
    open browser    ${url}     ${browser}
    maximize browser window
orangehrmlogin
    [Arguments]    ${username}  ${password}
    Input text    name=username    ${username}
    input text      name=password    ${password}
    sleep           5s
     capture page screenshot    beforelogin.png
    click button    xpath=//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button
     sleep           5s
    capture page screenshot    afterlogin.png
    close browser

*** Test Cases ***
Robo5.robot
    open orangehrm
    Sleep       5s
    orangehrmlogin    Admin     admin123