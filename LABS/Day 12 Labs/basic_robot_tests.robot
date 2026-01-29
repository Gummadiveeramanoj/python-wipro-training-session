*** Settings ***
Library    BuiltIn

*** Variables ***
${NAME}        Manu
${COURSE}      Robot Framework
@{TOOLS}       Python    Robot    Selenium

*** Test Cases ***
Test Case One - Logging and Scalar Variable
    Log    Hello ${NAME}, welcome to ${COURSE}
    Log To Console    Executing first test case
    Log    Course Name: ${COURSE}

Test Case Two - List Variable Demo
    Log To Console    Available tools are:
    Log    Tools List: ${TOOLS}
    Log To Console    First tool is ${TOOLS}[0]
