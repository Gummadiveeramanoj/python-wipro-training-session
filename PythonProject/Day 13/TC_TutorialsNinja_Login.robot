*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=testdata.xlsx    sheet_name=Sheet1
Test Template    Login To TutorialsNinja
Test Setup       Open TutorialsNinja
Test Teardown    Close Browser

*** Variables ***
${URL}        https://tutorialsninja.com/demo/
${BROWSER}    chrome

*** Test Cases ***
TC_TutorialsNinja_Login
    # Data is taken automatically from Excel

*** Keywords ***
Open TutorialsNinja
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    xpath=//span[text()='My Account']    20s
    Click Element    xpath=//span[text()='My Account']
    Click Link       Login
    Wait Until Element Is Visible    id=input-email    15s

Login To TutorialsNinja
    [Arguments]    ${email}    ${password}
    Input Text     id=input-email       ${email}
    Input Text     id=input-password    ${password}
    Click Button   xpath=//input[@value='Login']
    Sleep          3s
    Capture Page Screenshot
