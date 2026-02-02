*** Test Cases ***
IF ELSE IF Example
    ${marks}=    Set Variable    75
    IF    ${marks} >= 90
        Log    Grade A
    ELSE IF    ${marks} >= 75
        Log    Grade B
    ELSE
        Log    Grade C
    END
