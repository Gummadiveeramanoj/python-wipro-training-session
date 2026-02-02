*** Test Cases ***
FOR Loop Enumerate
    FOR    ${index}    ${value}    IN ENUMERATE    a    b    c
        Log    ${index} = ${value}
    END
