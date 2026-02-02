*** Test Cases ***
IF Condition Example
    ${age}=    Set Variable    20
    IF    ${age} >= 18
        Log    Eligible to vote
    END
