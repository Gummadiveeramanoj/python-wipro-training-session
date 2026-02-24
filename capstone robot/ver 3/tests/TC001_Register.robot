*** Settings ***
Documentation
...    TC001 — Register All Users from Excel
...    Run this FIRST. TC002_Login.robot runs after.
...
...    If email already exists → test is marked PASS with a skip message.
...    Never fails due to duplicate email.
...
...    Run:
...        robot --outputdir results tests\TC001_Register.robot

Library      SeleniumLibrary
...              timeout=15s
...              implicit_wait=0s
...              run_on_failure=Screenshot On Failure
Library      DateTime

Resource     ../resources/pages/BasePage.robot
Resource     ../resources/pages/HomePage.robot
Resource     ../resources/pages/RegistrationPage.robot

Variables    ../config/variables.py

Suite Setup       Log    ═══ TC001 Registration Suite Started ═══
Suite Teardown    Log    ═══ TC001 Registration Suite Completed ═══

Test Tags    registration    tc001

*** Test Cases ***

TC001 Register All Users
    FOR    ${user}    IN    @{USERS}
        Register Single User    ${user}
    END
*** Keywords ***

Register Single User
    [Arguments]    ${user}
    ${start}=    Get Current Date    result_format=%H:%M:%S
    Log    ══════════════════════════════════════════════════════
    Log    USER : ${user}[name] | ${user}[email] | START: ${start}
    Log    ══════════════════════════════════════════════════════

    Open Application        ${APP_URL}    ${BROWSER}
    Dismiss Ads And Overlays
    Verify Home Page Is Loaded
    Navigate To Signup Login Page
    Dismiss Ads And Overlays

    Fill Signup Form        ${user}[name]    ${user}[email]
    ${outcome}=             Check Signup Outcome    ${user}[email]

    IF    '${outcome}' == 'register'
        Fill Account Information    ${user}[password]
        Tick Checkboxes
        Fill Address Information
        ...    ${user}[first_name]    ${user}[last_name]    ${user}[address]    ${user}[city]
        ...    ${user}[state]         ${user}[zip]          ${user}[country]    ${user}[mobile]
        Submit Create Account
        Verify Account Created
        Click Continue After Registration
        Log    ✓ Registration SUCCESS: ${user}[name]

    ELSE
        # Email already exists — pass the test gracefully, TC002 will login
        Log    ⚠ Already registered: ${user}[email] — marking as PASS.
        Close Application
        Pass Execution    Account already exists for ${user}[email] — skipping registration.

    END

    ${end}=    Get Current Date    result_format=%H:%M:%S
    Log    ✓ DONE: ${user}[name] | Start: ${start} | End: ${end}
    Close Application
