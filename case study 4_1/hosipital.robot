*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    http://127.0.0.1:5000

*** Test Cases ***
Register Patient via UI
    Open Browser    ${URL}    Chrome
    Input Text    name=name    Alice
    Input Text    name=age     25
    Click Element    xpath=//input[@value='Female']
    Input Text    name=contact    8888888888
    Input Text    name=disease    Cold
    Select From List By Label    name=doctor    Dr. Smith
    Click Button    xpath=//button[text()='Submit']
    Sleep    2
    Close Browser