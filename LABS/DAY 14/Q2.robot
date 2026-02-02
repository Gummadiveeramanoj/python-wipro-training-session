*** Settings ***
Library    SeleniumLibrary
Suite Setup       Open Browser To Form
Suite Teardown    Close Browser
Test Teardown     Sleep    2s

*** Variables ***
${URL}        https://demoqa.com/automation-practice-form
${BROWSER}    chrome
${FIRSTNAME}  Manoj
${LASTNAME}   Student
${MOBILE}     9848871919

*** Keywords ***
Open Browser To Form
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Page Contains Element    id=firstName    10s
    Execute JavaScript    document.querySelectorAll("iframe, #fixedban, footer").forEach(e => e.remove());

*** Test Cases ***
Form Submission Test
    [Tags]    smoke    form

    Input Text    id=firstName    ${FIRSTNAME}
    Input Text    id=lastName     ${LASTNAME}
    Input Text    id=userNumber   ${MOBILE}

    ${gender}=    Set Variable    Male
    Run Keyword If    '${gender}' == 'Male'    Click Element    xpath=//label[text()='Male']
    Run Keyword If    '${gender}' == 'Female'  Click Element    xpath=//label[text()='Female']

    Click Element    xpath=//label[text()='Sports']

    # State Dropdown
    Click Element    xpath=//div[contains(text(),'Select State')]
    Input Text       xpath=//input[@id='react-select-3-input']    NCR
    Press Keys       xpath=//input[@id='react-select-3-input']    ENTER
    Sleep    1s

    Execute JavaScript    window.scrollTo(0, document.body.scrollHeight)
    Click Button    id=submit

    Wait Until Element Is Visible    id=example-modal-sizes-title-lg    10s
    ${message}=    Get Text    id=example-modal-sizes-title-lg
    Should Be Equal    ${message}    Thanks for submitting the form