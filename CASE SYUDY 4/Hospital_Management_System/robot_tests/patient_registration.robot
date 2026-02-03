*** Settings ***
Library    SeleniumLibrary
Suite Setup    Open Browser    http://127.0.0.1:5000    chrome
Suite Teardown    Close Browser

*** Test Cases ***
Register Patient
    Wait Until Element Is Visible    name=name    10s
    Input Text    name=name    Ramesh
    Input Text    name=age     40
    Input Text    name=disease    Fever
    Click Button    xpath=//button[@type='submit']
