*** Settings ***
Library    BuiltIn

*** Variables ***
@{NAMES}    John    Alex    Sam
@{AGES}     25      30      28

*** Test Cases ***
FOR Loop Zip
    FOR    ${name}    ${age}    IN ZIP    @{NAMES}    @{AGES}
        Log To Console    Name: ${name} | Age: ${age}
    END
