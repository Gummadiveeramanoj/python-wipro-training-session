*** Test Cases ***
IF ELSE Example
    ${num}=    Set Variable    5
    IF    ${num} > 10
        Log    Greater than 10
    ELSE
        Log    Less than or equal to 10
    END
