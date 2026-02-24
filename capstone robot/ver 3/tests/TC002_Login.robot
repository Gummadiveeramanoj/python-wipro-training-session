*** Settings ***
Documentation
...    TC002 — Login All Users, Add Product to Cart Twice, Remove All, Logout
...
...    Run AFTER TC001_Register.robot has completed.
...
...    Run:  robot --outputdir results tests\TC002_Login.robot

Library      SeleniumLibrary
...              timeout=15s
...              implicit_wait=0s
...              run_on_failure=Nothing

Resource     ../resources/pages/BasePage.robot
Resource     ../resources/pages/HomePage.robot
Resource     ../resources/pages/LoginPage.robot
Resource     ../resources/pages/ProductsPage.robot
Resource     ../resources/pages/CartPage.robot

Variables    ../config/variables.py

Suite Setup       Log    ═══ TC002 Start: Login → Cart → Remove → Logout ═══
Suite Teardown    Log    ═══ TC002 End ═══

Test Teardown     Run Keyword If Test Failed    Capture Page Screenshot

Test Tags    login    cart    tc002


*** Test Cases ***

TC002 Login And Cart All Users
    FOR    ${user}    IN    @{USERS}
        Login And Cart Flow    ${user}
    END
*** Keywords ***

Login And Cart Flow
    [Arguments]    ${user}
    Log    ══════════════════════════════════════════════════════
    Log    USER: ${user}[name] | ${user}[email] | ${user}[product]
    Log    ══════════════════════════════════════════════════════

    # ── 1. Open browser ─────────────────────────────────────────
    Open Application        ${APP_URL}    ${BROWSER}
    Dismiss Ads And Overlays
    Verify Home Page Is Loaded

    # ── 2. Login ────────────────────────────────────────────────
    Navigate To Signup Login Page
    Dismiss Ads And Overlays
    Login User              ${user}[email]      ${user}[password]
    Verify Logged In As     ${user}[name]
    Log    ✓ Logged in: ${user}[name]

    # ── 3. First add to cart ────────────────────────────────────
    Dismiss Ads And Overlays
    Navigate To Products Page
    Verify Products Page Is Loaded
    Dismiss Ads And Overlays
    Search For Product              ${user}[product]
    Verify Search Results Displayed
    Open First Product Detail
    Verify Product Detail Page Loaded
    Add Product To Cart From Detail Page
    Log    ✓ First add to cart done.

    # ── 4. Second add to cart ───────────────────────────────────
    Dismiss Ads And Overlays
    Navigate To Products Page
    Verify Products Page Is Loaded
    Dismiss Ads And Overlays
    Search For Product              ${user}[product]
    Verify Search Results Displayed
    Open First Product Detail
    Verify Product Detail Page Loaded
    Add Product To Cart From Detail Page
    Log    ✓ Second add to cart done.

    # ── 5. Verify cart ──────────────────────────────────────────
    Navigate To Cart Page
    Verify Cart Page Is Loaded
    Verify Cart Is Not Empty
    Verify Product In Cart          ${user}[product]
    Log    ✓ Product verified in cart.

    # ── 6. Remove items ─────────────────────────────────────────
    Remove All Items From Cart
    Verify Cart Is Empty
    Log    ✓ Cart cleared.

    # ── 7. Logout ───────────────────────────────────────────────
    Logout User
    Log    ✓ Logged out.

    # ── 8. Close browser ────────────────────────────────────────
    Close Application
    Log    ✓ COMPLETE: ${user}[name] done.