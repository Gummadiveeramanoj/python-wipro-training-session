*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}      https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}      firefox
${username}     Admin
${password}     admin123


*** Test Cases ***
TC004_Login.robot
    open browser    ${url}     ${browser}
    sleep           5s
    input text    name=username    ${username}
    input text    name=password    ${password}
    click button    xpath=//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button
    close browser