*** Settings ***
Documentation    LoginPage.robot — Login keywords for TC002_Login.robot
...              NOTE: SeleniumLibrary must NOT be imported here.

Resource    BasePage.robot

*** Keywords ***

Login User
    [Arguments]    ${email}    ${password}
    Wait Until Element Is Visible    xpath://h2[text()='Login to your account']    15s
    Wait Until Element Is Visible    xpath://input[@data-qa='login-email']        10s
    Type Into Field                  xpath://input[@data-qa='login-email']        ${email}
    Type Into Field                  xpath://input[@data-qa='login-password']     ${password}
    Safe Click                       xpath://button[@data-qa='login-button']
    Log    ✓ Login submitted for: ${email}

Verify Logged In As
    [Arguments]    ${name}
    Wait Until Element Is Visible    xpath://li/a[contains(.,'Logged in as')]    15s
    Element Should Contain           xpath://li/a[contains(.,'Logged in as')]    ${name}
    Log    ✓ Logged in as: ${name}
