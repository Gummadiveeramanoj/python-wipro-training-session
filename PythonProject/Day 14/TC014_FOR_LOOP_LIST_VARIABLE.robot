*** Variables ***
@{COLORS}    Red    Green    Blue

*** Test Cases ***
FOR Loop With List
    FOR    ${color}    IN    @{COLORS}
        Log    Color: ${color}
    END