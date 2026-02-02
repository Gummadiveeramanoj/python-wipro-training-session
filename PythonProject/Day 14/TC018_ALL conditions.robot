# Nested FOR loop
*** Test Cases ***
Nested FOR Loop
    FOR    ${i}    IN RANGE    1    4
        FOR    ${j}    IN RANGE    1    3
            Log    i=${i}, j=${j}
        END
    END
# FOR loop with IF condition
*** Test Cases ***
FOR Loop With IF
    FOR    ${n}    IN RANGE    1    6
        IF    ${n} == 3
            Log    Found 3
        END
#BREAK (exit loop)
*** Test Cases ***
BREAK Example
    FOR    ${i}    IN RANGE    1    10
        IF    ${i} == 5
            BREAK
        END
        Log    ${i}
    END
#CONTINUE (skip iteration)
*** Test Cases ***
CONTINUE Example
    FOR    ${i}    IN RANGE    1    6
        IF    ${i} == 3
            CONTINUE
        END
        Log    ${i}
    END
#WHILE loop (Robot Framework 4+)
*** Test Cases ***
WHILE Loop Example
    ${i}=    Set Variable    1
    WHILE    ${i} <= 5
        Log    Value: ${i}
        ${i}=    Evaluate    ${i} + 1
    END
#WHILE with BREAK
*** Test Cases ***
WHILE Loop With BREAK
    ${i}=    Set Variable    1
    WHILE    True
        IF    ${i} == 4
            BREAK
        END
        Log    ${i}
        ${i}=    Evaluate    ${i} + 1
    END
#ERROR HANDLING (Control Structure)
*** Test Cases ***
Try Except Example
    TRY
        Fail    Something went wrong
    EXCEPT
        Log    Error handled
    FINALLY
        Log    Always executed
    END
#CONDITIONAL KEYWORD EXECUTION
# Run Keyword If
*** Test Cases ***
Run Keyword If Example
    ${status}=    Set Variable    PASS
    Run Keyword If    '${status}' == 'PASS'    Log    Test Passed
#Run Keyword Unless
*** Test Cases ***
Run Keyword Unless Example
    ${status}=    Set Variable    FAIL
    Run Keyword Unless    '${status}' == 'PASS'    Log    Test Failed
