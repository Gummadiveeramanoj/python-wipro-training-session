*** Settings ***
Documentation    Keywords for the Home Page of automationexercise.com
Resource         BasePage.robot

*** Keywords ***

Verify Home Page Is Loaded
    Wait Until Element Is Visible    xpath://img[@alt='Website for automation practice']    20s
    Title Should Be    Automation Exercise
    Log    ✓ Home page loaded.

Navigate To Signup Login Page
    Kill All Ads
    Wait Until Element Is Visible    xpath://a[@href='/login']    10s
    Safe Click                       xpath://a[@href='/login']
    Wait Until Location Contains     /login    10s
    Log    ✓ Navigated to /login.

Navigate To Products Page
    Kill All Ads
    Wait Until Element Is Visible    xpath://a[@href='/products']    10s
    Safe Click                       xpath://a[@href='/products']
    Wait Until Location Contains     /products    10s
    Log    ✓ Navigated to /products.

Navigate To Cart Page
    Kill All Ads
    Wait Until Element Is Visible    xpath://a[@href='/view_cart']    10s
    Safe Click                       xpath://a[@href='/view_cart']
    Wait Until Location Contains     /view_cart    10s
    Log    ✓ Navigated to /view_cart.

Logout User
    Kill All Ads
    Wait Until Element Is Visible    xpath://a[@href='/logout']    10s
    Safe Click                       xpath://a[@href='/logout']
    Wait Until Location Contains     /login    10s
    Log    ✓ Logged out successfully.
