*** Settings ***
Library    SeleniumLibrary
Suite Setup    Open Browser    http://localhost/register.html    chrome
Suite Teardown    Close Browser

*** Test Cases ***
Register Patient
    Input Text    id:name    Manoj
    Input Text    id:age     24
    Click Element    xpath://input[@value='Male']
    Input Text    id:contact    9876543210
    Input Text    id:disease    Fever
    Select From List By Index    id:doctor    1
    Click Button    xpath://button[text()='Submit']
