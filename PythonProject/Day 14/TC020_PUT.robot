*** Settings ***
Library    RequestsLibrary

*** Variables ***
${baseurl}  http://127.0.0.1:5000
*** Test Cases ***
Create new user
     Create Session    postingsession    ${baseurl}
    ${data}=    Create Dictionary    name=varsha
    ${response}=    POST On Session    postingsession    /users    json=${data}
    Status Should Be    201    ${response}
    ${user_json}=    Evaluate    $response.json()
     Log    ${user_json}=    console=True
update user
         Create Session    postingsession    ${baseurl}
         ${data}=    Create Dictionary    name=Pooja
         ${response}=    PUT On Session    postingsession    /users/1    json=${data}
         Status Should Be    200    ${response}
         ${user_json}=    Evaluate    $response.json()
         Log    ${user_json}=    console=True

patch user
         Create Session    postingsession    ${baseurl}
         ${data}=    Create Dictionary    name=Pooja patched
         ${response}=    PUT On Session    postingsession    /users/1    json=${data}
         Status Should Be    200    ${response}
         ${user_json}=    Evaluate    $response.json()
         Log    ${user_json}=    console=True

Verify Get All Users
        Create Session     mysession       ${baseurl}
        ${response}=  GET On Session    mysession   /users
        Status Should Be    200      ${response}
        ${res_jon}=     To Json    ${response.content}
        log       ${res_jon}=   console=True

Verify Get Single user
        Create Session    mysession             ${baseurl}
        ${response}=  GET On Session    mysession   /users/3
        Status Should Be    200      ${response}
        ${res_jon}=     To Json    ${response.content}
        log       ${res_jon}=   console=True
Verify Get Single user not gound
        Create Session    mysession             ${baseurl}
        ${response}=  GET On Session    mysession   /users/99999
        Status Should Be    404      ${response}
        ${res_jon}=     To Json    ${response.content}
        log       ${res_jon}=   console=True

Verify Delete user by userid
        Create Session    mysession             ${baseurl}
        ${response}=  GET On Session    mysession   /users/1
        Status Should Be    200     ${response}
        ${res_jon}=     To Json    ${response.content}
        log       ${res_jon}=   console=True

