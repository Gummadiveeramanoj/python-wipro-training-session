*** Settings ***
Documentation    Keywords for the Products page of automationexercise.com
Resource         BasePage.robot

*** Keywords ***

Verify Products Page Is Loaded
    Wait Until Element Is Visible    xpath://h2[contains(text(),'All Products')]    15s
    Log    ✓ All Products page loaded.

Search For Product
    [Arguments]    ${product_name}
    Kill All Ads
    Wait Until Element Is Visible    id=search_product    10s
    Type Into Field                  id=search_product    ${product_name}
    Safe Click                       id=submit_search
    Wait Until Element Is Visible    xpath://h2[contains(text(),'Searched Products')]    15s
    Log    ✓ Searched for: ${product_name}

Verify Search Results Displayed
    ${count}=    Get Element Count    xpath://div[@class='productinfo text-center']
    Should Be True    ${count} > 0    msg=Search returned 0 results.
    Log    ✓ Search returned ${count} product(s).

Open First Product Detail
    Kill All Ads
    Wait Until Element Is Visible    xpath:(//a[contains(@href,'/product_details/')])[1]    10s
    Safe Click                       xpath:(//a[contains(@href,'/product_details/')])[1]
    Wait Until Location Contains     /product_details/    10s
    Log    ✓ Product detail page opened.

Verify Product Detail Page Loaded
    Wait Until Element Is Visible    xpath://div[@class='product-information']//h2    10s
    ${name}=    Get Text    xpath://div[@class='product-information']//h2
    Log    ✓ Product detail loaded: ${name}
    RETURN    ${name}

Add Product To Cart From Detail Page
    Kill All Ads
    Wait Until Element Is Visible
    ...    xpath://div[@class='product-information']//button[contains(@class,'cart')]    10s
    Safe Click
    ...    xpath://div[@class='product-information']//button[contains(@class,'cart')]
    Log    ✓ Add to Cart clicked.
    Handle Add To Cart Modal

Handle Add To Cart Modal
    ${visible}=    Run Keyword And Return Status
    ...    Wait Until Element Is Visible
    ...    xpath://button[contains(text(),'Continue Shopping')]    8s
    Run Keyword If    ${visible}
    ...    Safe Click    xpath://button[contains(text(),'Continue Shopping')]
    Log    ✓ Modal handled — continuing shopping.
