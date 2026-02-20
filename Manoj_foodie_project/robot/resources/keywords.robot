*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    String

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000

*** Keywords ***
Create Foodie Session
    ${headers}=    Create Dictionary    Content-Type=application/json
    Create Session    foodie    ${BASE_URL}    headers=${headers}

Register Restaurant
    ${rand}=    Generate Random String    6    [NUMBERS]
    ${name}=    Set Variable    FoodHub_${rand}

    ${body}=    Create Dictionary
    ...    name=${name}
    ...    category=Indian
    ...    location=Hyderabad

    ${resp}=    POST On Session
    ...    foodie
    ...    /api/v1/restaurants
    ...    json=${body}

    Status Should Be    201    ${resp}
    ${json}=    Set Variable    ${resp.json()}
    Set Suite Variable    ${RESTAURANT_ID}    ${json["id"]}

Add Dish
    ${body}=    Create Dictionary
    ...    name=Chicken Biryani
    ...    price=250

    ${resp}=    POST On Session
    ...    foodie
    ...    /api/v1/restaurants/${RESTAURANT_ID}/dishes
    ...    json=${body}

    Status Should Be    201    ${resp}
    ${json}=    Set Variable    ${resp.json()}
    Set Suite Variable    ${DISH_ID}    ${json["id"]}

Register User
    ${rand}=    Generate Random String    5    [NUMBERS]
    ${email}=    Set Variable    manu${rand}@gmail.com

    ${body}=    Create Dictionary
    ...    name=Manu
    ...    email=${email}

    ${resp}=    POST On Session
    ...    foodie
    ...    /api/v1/users/register
    ...    json=${body}

    Status Should Be    201    ${resp}
    ${json}=    Set Variable    ${resp.json()}
    Set Suite Variable    ${USER_ID}    ${json["id"]}

Place Order
    ${body}=    Create Dictionary
    ...    user_id=${USER_ID}
    ...    restaurant_id=${RESTAURANT_ID}
    ...    dishes=Chicken Biryani

    ${resp}=    POST On Session
    ...    foodie
    ...    /api/v1/orders
    ...    json=${body}

    Status Should Be    201    ${resp}

Approve Restaurant
    ${resp}=    PUT On Session
    ...    foodie
    ...    /api/v1/admin/restaurants/${RESTAURANT_ID}/approve
    Status Should Be    200    ${resp}

View Orders (Admin)
    ${resp}=    GET On Session
    ...    foodie
    ...    /api/v1/admin/orders
    Status Should Be    200    ${resp}
