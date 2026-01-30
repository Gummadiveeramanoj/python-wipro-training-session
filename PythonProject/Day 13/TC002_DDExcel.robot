*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=C:/PythonProject/Day 13/testdata.xlsx
Test Template    OrangeHRM Login With Excel

*** Variables ***
${URL}       https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}   firefox

*** Test Cases ***
TC002_DDExcel_Login
    [Documentation]    Data driven login using Excel

*** Keywords ***
OrangeHRM Login With Excel
    [Arguments]    ${username}    ${password}
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    3s
    Input Text      name=username    ${username}
    Input Text      name=password    ${password}
    Click Button    xpath=//button[@type='submit']
    Sleep           3s
    Capture Page Screenshot
    Close Browser
