*** Settings ***
Documentation
...    RegistrationPage.robot — Registration flow keywords.
...    Used ONLY by TC001_Register.robot.
...    Login flow is handled separately in LoginPage.robot + TC002_Login.robot.
...
...    NOTE: SeleniumLibrary must NOT be imported here.
...    It is imported ONCE only in the test suite file.

Resource    BasePage.robot

*** Keywords ***

# ─────────────────────────────────────────────────────────────────────────────
# STEP 1 — /login page: "New User Signup!" section
# ─────────────────────────────────────────────────────────────────────────────

Fill Signup Form
    [Arguments]    ${name}    ${email}
    Wait Until Element Is Visible    xpath://h2[text()='New User Signup!']              15s
    Wait Until Element Is Visible    xpath://input[@data-qa='signup-name']              10s
    Type Into Field                  xpath://input[@data-qa='signup-name']              ${name}
    Type Into Field                  xpath://input[@data-qa='signup-email']             ${email}
    Click Button                     xpath://button[@data-qa='signup-button']
    Log    ✓ Signup button clicked.

Check Signup Outcome
    [Documentation]
    ...    Polls every 0.5s for up to 30s waiting for EITHER:
    ...    A) URL becomes /signup   → new account    → return "register"
    ...    B) Error p tag appears   → email exists   → return "login"
    ...    Whichever appears first wins immediately — no long sequential waits.
    [Arguments]    ${email}
    ${timeout}=    Set Variable    ${30}
    ${interval}=   Set Variable    ${0.5}
    ${elapsed}=    Set Variable    ${0}
    WHILE    ${elapsed} < ${timeout}
        ${url}=    Get Location
        ${on_signup}=    Run Keyword And Return Status
        ...    Should Contain    ${url}    /signup
        IF    ${on_signup}
            Log    ✓ Outcome: new account — on /signup page.
            RETURN    register
        END
        ${error_visible}=    Run Keyword And Return Status
        ...    Element Should Be Visible
        ...    xpath://p[contains(text(),'Email Address already exist!')]
        IF    ${error_visible}
            Log    ⚠ Outcome: email already exists — ${email}
            RETURN    login
        END
        Sleep    ${interval}
        ${elapsed}=    Evaluate    ${elapsed} + ${interval}
    END


# ─────────────────────────────────────────────────────────────────────────────
# STEP 2 — /signup page: Account Information
# ─────────────────────────────────────────────────────────────────────────────

Fill Account Information
    [Arguments]    ${password}
    Scroll Into View                 id=id_gender1
    Click Element                    id=id_gender1
    Wait Until Element Is Visible    id=password                                        10s
    Type Into Field                  id=password                                        ${password}
    Scroll Into View                 id=days
    Select From List By Value        id=days                                            15
    Select From List By Label        id=months                                          June
    Select From List By Value        id=years                                           1990
    Log    ✓ Account information filled.

Tick Checkboxes
    Scroll Into View    id=newsletter
    ${nl}=    Run Keyword And Return Status    Checkbox Should Be Selected    id=newsletter
    Run Keyword If    not ${nl}    Select Checkbox    id=newsletter
    ${op}=    Run Keyword And Return Status    Checkbox Should Be Selected    id=optin
    Run Keyword If    not ${op}    Select Checkbox    id=optin
    Log    ✓ Checkboxes ticked.

# ─────────────────────────────────────────────────────────────────────────────
# STEP 3 — /signup page: Address Information
# ─────────────────────────────────────────────────────────────────────────────

Fill Address Information
    [Arguments]    ${first_name}    ${last_name}    ${address}    ${city}
    ...            ${state}         ${zip}          ${country}    ${mobile}
    Wait Until Element Is Visible    id=first_name                                      10s
    Type Into Field                  id=first_name                                      ${first_name}
    Type Into Field                  id=last_name                                       ${last_name}
    Type Into Field                  id=address1                                        ${address}
    Scroll Into View                 id=country
    Select From List By Label        id=country                                         ${country}
    Type Into Field                  id=state                                           ${state}
    Type Into Field                  id=city                                            ${city}
    Type Into Field                  id=zipcode                                         ${zip}
    Type Into Field                  id=mobile_number                                   ${mobile}
    Log    ✓ Address information filled.

Submit Create Account
    Scroll Into View    xpath://button[@data-qa='create-account']
    Click Button        xpath://button[@data-qa='create-account']
    Log    ✓ Create Account button clicked.

# ─────────────────────────────────────────────────────────────────────────────
# STEP 4 — /account_created page
# ─────────────────────────────────────────────────────────────────────────────

Verify Account Created
    Wait Until Element Is Visible
    ...    xpath://b[contains(translate(text(),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'ACCOUNT CREATED')]
    ...    20s
    Log    ✓ ACCOUNT CREATED page confirmed.

Click Continue After Registration
    Wait Until Element Is Visible    xpath://a[@data-qa='continue-button']    10s
    Click Element                    xpath://a[@data-qa='continue-button']
    Log    ✓ Continue clicked.
