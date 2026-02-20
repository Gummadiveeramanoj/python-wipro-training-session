*** Settings ***
Resource    ../resources/keywords.robot
Suite Setup    Create Foodie Session

*** Test Cases ***
TC01 - Register Restaurant
    [Documentation]    Register a new restaurant and store its ID
    Register Restaurant

TC02 - Add Dish To Restaurant
    [Documentation]    Add a dish to the registered restaurant
    Add Dish

TC03 - Register User
    [Documentation]    Register a new user and store their ID
    Register User

TC04 - Place Order
    [Documentation]    Place an order using registered user, restaurant, and dish
    Place Order

TC05 - Admin Approve Restaurant
    [Documentation]    Admin approves the registered restaurant
    Approve Restaurant

TC06 - Admin View All Orders
    [Documentation]    Admin fetches all orders and verifies response
    View Orders (Admin)
