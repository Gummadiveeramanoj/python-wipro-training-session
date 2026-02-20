*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    BuiltIn

*** Test Cases ***
Register Restaurant
    Create Session    foodie    http://127.0.0.1:5000

    ${rand}=    Evaluate    __import__('random').randint(1000,9999)
    ${name}=    Set Variable    SpicyHub_${rand}

    ${payload}=    Create Dictionary
    ...    name=${name}
    ...    category=Non-Veg
    ...    location=Delhi

    ${resp}=    POST On Session
    ...    foodie
    ...    /api/v1/restaurants
    ...    json=${payload}

    Status Should Be    201    ${resp}
