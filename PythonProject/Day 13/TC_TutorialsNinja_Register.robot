*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=testdata.xlsx    sheet_name=Sheet3
Library    DateTime
Test Template    Register TutorialsNinja User
Test Setup       Open Registration Page
Test Teardown    Close Browser

*** Variables ***
${URL}        https://tutorialsninja.com/demo/
${BROWSER}    chrome

*** Test Cases ***
TC_TutorialsNinja_Register
    # Data taken automatically from Excel

*** Keywords ***
Open Registration Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    xpath=//span[text()='My Account']    20s
    Click Element    xpath=//span[text()='My Account']
    Click Link       Register
    Wait Until Element Is Visible    id=input-firstname    15s

Register TutorialsNinja User
    [Arguments]    ${firstname}    ${lastname}    ${telephone}    ${password}    ${confirm}

    ${timestamp}=    Get Current Date    result_format=%Y%m%d%H%M%S
    ${email}=        Set Variable    ${firstname}.${lastname}.${timestamp}@mail.com

    Input Text    id=input-firstname    ${firstname}
    Input Text    id=input-lastname     ${lastname}
    Input Text    id=input-email        ${email}
    Input Text    id=input-telephone    ${telephone}
    Input Text    id=input-password     ${password}
    Input Text    id=input-confirm      ${confirm}

    Click Element    xpath=//input[@name='agree']
    Click Button     xpath=//input[@value='Continue']

    Wait Until Page Contains    Your Account Has Been Created!    15s
    Capture Page Screenshot

Close Browser
    Close Browser
