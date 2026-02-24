*** Settings ***
Documentation    BasePage.robot — Shared browser, interaction, ad-handling and assertion keywords.
...              SeleniumLibrary is NOT imported here — imported ONCE in the main test suite.
Library    Collections
Library    String

*** Keywords ***

# ─────────────────────────────────────────────────────────────────────────────
# Browser
# ─────────────────────────────────────────────────────────────────────────────

Open Application
    [Arguments]    ${url}    ${browser}=chrome
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys
    Call Method    ${options}    add_argument    --disable-notifications
    Call Method    ${options}    add_argument    --disable-popup-blocking
    Call Method    ${options}    add_argument    --disable-infobars
    Call Method    ${options}    add_argument    --disable-extensions
    Call Method    ${options}    add_argument    --no-sandbox
    Call Method    ${options}    add_argument    --disable-dev-shm-usage
    Call Method    ${options}    add_argument    --disable-gpu
    Call Method    ${options}    add_argument    --start-maximized
    ${prefs}=    Create Dictionary
    ...    profile.default_content_setting_values.notifications=${2}
    ...    profile.default_content_setting_values.popups=${2}
    Call Method    ${options}    add_experimental_option    prefs    ${prefs}
    Create Webdriver    Chrome    options=${options}
    Go To    ${url}
    Set Selenium Page Load Timeout    30s
    Set Selenium Implicit Wait        0s
    Log    ✓ Browser opened → ${url}

Close Application
    Close Browser

# ─────────────────────────────────────────────────────────────────────────────
# Kill All Ads — MUST be called before every navigation click
# Uses JS to nuke every ad iframe on the page so nothing intercepts clicks
# ─────────────────────────────────────────────────────────────────────────────

Kill All Ads
    Execute Javascript
    ...    (function(){
    ...        var selectors = [
    ...            'iframe[src*="google"]',
    ...            'iframe[src*="doubleclick"]',
    ...            'iframe[src*="googlesyndication"]',
    ...            'iframe[id*="aswift"]',
    ...            'iframe[name*="aswift"]',
    ...            'ins.adsbygoogle',
    ...            'div[id*="google_ads"]',
    ...            'div[class*="adsbygoogle"]'
    ...        ];
    ...        selectors.forEach(function(sel){
    ...            document.querySelectorAll(sel).forEach(function(el){
    ...                el.style.display = 'none';
    ...                el.style.pointerEvents = 'none';
    ...                el.style.height = '0';
    ...                el.style.width = '0';
    ...            });
    ...        });
    ...    })();
    Sleep    0.5s

Dismiss Ads And Overlays
    Sleep    2s
    Kill All Ads
    ${vignette}=    Run Keyword And Return Status
    ...    Element Should Be Visible    id=dismiss-button
    Run Keyword If    ${vignette}    Click Element    id=dismiss-button
    ${cookie}=    Run Keyword And Return Status
    ...    Element Should Be Visible    xpath://button[contains(text(),'Accept')]
    Run Keyword If    ${cookie}    Click Element    xpath://button[contains(text(),'Accept')]
    Kill All Ads
    Sleep    0.5s

# ─────────────────────────────────────────────────────────────────────────────
# Safe Click — kills ads then JS-clicks the element (bypasses interceptors)
# ─────────────────────────────────────────────────────────────────────────────

Safe Click
    [Arguments]    ${locator}
    Kill All Ads
    Wait Until Element Is Visible    ${locator}    15s
    Scroll Into View                 ${locator}
    Kill All Ads
    ${el}=    Get WebElement    ${locator}
    Execute Javascript    arguments[0].click();    ARGUMENTS    ${el}
    Log    ✓ Safe clicked: ${locator}

# ─────────────────────────────────────────────────────────────────────────────
# Type Into Field — JS nativeInputValueSetter, no double typing
# ─────────────────────────────────────────────────────────────────────────────

Type Into Field
    [Arguments]    ${locator}    ${value}
    Wait Until Element Is Visible    ${locator}    10s
    Wait Until Element Is Enabled    ${locator}    10s
    Scroll Into View                 ${locator}
    Click Element                    ${locator}
    ${el}=    Get WebElement    ${locator}
    Execute Javascript
    ...    var el = arguments[0];
    ...    var setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
    ...    setter.call(el, arguments[1]);
    ...    el.dispatchEvent(new Event('input',  { bubbles: true }));
    ...    el.dispatchEvent(new Event('change', { bubbles: true }));
    ...    ARGUMENTS    ${el}    ${value}
    Log    ✓ Typed '${value}' into ${locator}

# ─────────────────────────────────────────────────────────────────────────────
# Scroll
# ─────────────────────────────────────────────────────────────────────────────

Scroll Into View
    [Arguments]    ${locator}
    ${el}=    Get WebElement    ${locator}
    Execute Javascript
    ...    arguments[0].scrollIntoView({behavior:'smooth', block:'center'});
    ...    ARGUMENTS    ${el}
    Sleep    0.4s

# ─────────────────────────────────────────────────────────────────────────────
# Assertions
# ─────────────────────────────────────────────────────────────────────────────

Element Text Should Be
    [Arguments]    ${locator}    ${expected}    ${msg}=Text mismatch
    ${actual}=    Get Text    ${locator}
    Should Be Equal    ${actual}    ${expected}    msg=${msg}    values=True

Element Text Should Contain
    [Arguments]    ${locator}    ${expected}    ${msg}=Text not found
    ${actual}=    Get Text    ${locator}
    Should Contain    ${actual}    ${expected}    msg=${msg}

Screenshot On Failure
    [Documentation]
    ...    Used as run_on_failure handler for SeleniumLibrary.
    ...    Only captures a screenshot when the TEST has actually failed —
    ...    NOT when Run Keyword And Return Status or similar silently fails.
    ...    This stops screenshots being taken during passing tests.
    ${test_failed}=    Run Keyword And Return Status
    ...    Should Be Equal    ${TEST STATUS}    FAIL
    Run Keyword If    ${test_failed}
    ...    Capture Page Screenshot    filename=EMBED
