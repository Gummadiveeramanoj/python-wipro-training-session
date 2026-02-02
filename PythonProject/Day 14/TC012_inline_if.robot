*** Test Cases ***
Inline IF Example
    ${status}=    Set Variable    PASS
    IF    '${status}' == 'PASS'    Log    Test Passed
