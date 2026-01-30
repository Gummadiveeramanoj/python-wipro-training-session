*** Settings ***
Library    SeleniumLibrary
Test Template    Login Test With Data

*** Variables ***
${BROWSER}    chrome
${URL}        https://example.com/login

*** Test Cases ***
Login Using CSV Data
    ${username}    ${password}

*** Keywords ***
Login Test With Data
    [Arguments]    ${username}    ${password}
    Open Browser    ${URL}    ${BROWSER}
    Input Text    id=username    ${username}
    Input Text    id=password    ${password}
    Click Button    id=login
    Page Should Contain    Welcome
    Close Browser
