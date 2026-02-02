*** Settings ***
Library    SeleniumLibrary
Suite Setup       Open Application
Suite Teardown    Close Application
Test Setup        Start Test
Test Teardown     End Test

*** Variables ***
${URL}      https://www.google.com
${BROWSER}  chrome

*** Keywords ***
Open Application
    Log    ===== SUITE SETUP: Opening browser =====
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Close Application
    Log    ===== SUITE TEARDOWN: Closing browser =====
    Close Browser

Start Test
    Log    ----- TEST SETUP: Starting test -----

End Test
    Log    ----- TEST TEARDOWN: Ending test -----

*** Test Cases ***
Verify Google Title
    [Tags]    smoke
    Title Should Be    Google
    Capture Page Screenshot

Verify Page Contains Text
    [Tags]    regression
    Page Should Contain    Google
    Capture Page Screenshot