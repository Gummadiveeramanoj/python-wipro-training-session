*** Settings ***
Documentation    Keywords for the Cart page of automationexercise.com
...
...    CART HTML STRUCTURE (from page source):
...        Table  : <table id="cart_info_table">
...        Body   : <tbody> inside the table (no id on tbody)
...        Rows   : <tr id="product-1">, <tr id="product-2"> etc.
...        Name   : <td class="cart_description"><h4><a>Blue Top</a></h4>
...        Qty    : <button class="disabled">1</button>  ← disabled, cannot update
...        Delete : <a class="cart_quantity_delete" data-product-id="1">
...        Empty  : <span id="empty_cart" style="display:none"> shown by JS after delete

Library          String
Resource         BasePage.robot

*** Keywords ***

Verify Cart Page Is Loaded
    Kill All Ads
    Wait Until Location Contains     /view_cart                                15s
    Wait Until Element Is Visible    id=cart_info_table                        15s
    Log    ✓ Cart page loaded.

Verify Cart Is Not Empty
    ${count}=    Get Element Count    xpath://table[@id='cart_info_table']//tbody//tr
    Should Be True    ${count} > 0    msg=Cart is empty — expected at least 1 row.
    Log    ✓ Cart has ${count} item(s).

Verify Product In Cart
    [Arguments]    ${expected_product}
    @{items}=          Get WebElements
    ...    xpath://table[@id='cart_info_table']//td[@class='cart_description']//h4/a
    ${expected_lc}=    Convert To Lower Case    ${expected_product}
    ${found}=          Set Variable    ${FALSE}
    FOR    ${item}    IN    @{items}
        ${text}=      Get Text    ${item}
        ${text_lc}=   Convert To Lower Case    ${text}
        ${match}=     Run Keyword And Return Status
        ...    Should Contain    ${text_lc}    ${expected_lc}
        IF    ${match}
            ${found}=    Set Variable    ${TRUE}
            BREAK
        END
    END
    Should Be True    ${found}
    ...    msg=Product '${expected_product}' not found in cart.
    Log    ✓ Product '${expected_product}' confirmed in cart.

Remove All Items From Cart
    [Documentation]
    ...    Deletes every item from the cart by clicking each
    ...    <a class="cart_quantity_delete"> link one by one.
    ...    After each click waits 1.5s for the row to animate out,
    ...    then recounts rows and repeats until 0 remain.
    Kill All Ads
    ${count}=    Get Element Count
    ...    xpath://table[@id='cart_info_table']//tbody//tr
    Log    Removing ${count} item(s) from cart...
    WHILE    ${count} > 0
        Kill All Ads
        # Always click the first remaining delete link
        ${del_exists}=    Run Keyword And Return Status
        ...    Element Should Be Visible
        ...    xpath:(//a[@class='cart_quantity_delete'])[1]
        IF    not ${del_exists}    BREAK
        Safe Click    xpath:(//a[@class='cart_quantity_delete'])[1]
        Sleep    1.5s
        ${count}=    Get Element Count
        ...    xpath://table[@id='cart_info_table']//tbody//tr
        Log    Rows remaining: ${count}
    END
    Log    ✓ All items removed from cart.

Verify Cart Is Empty
    [Documentation]
    ...    The site shows <span id="empty_cart"> after all items deleted.
    ...    Waits up to 10s for it to become visible.
    Wait Until Element Is Visible    id=empty_cart    10s
    Log    ✓ Cart is empty confirmed.
