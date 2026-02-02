*** Settings ***

*** Test Cases ***
Print Names Using For Loop
    FOR    ${name}    IN    Ram    Ravi    Taj
        Log To Console    ${name}
    END

Print Numbers Using While Loop
    ${count}=    Set Variable    1
    WHILE    ${count} <= 5
        Log To Console    ${count}
        ${count}=    Evaluate    ${count} + 1
    END