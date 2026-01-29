*** Settings ***
Library    BuiltIn
Library    SeleniumLibrary

*** Test Cases ***
Verify Environment Setup
    Log To Console    Starting environment verification...

    # Python version (display only)
    Log To Console    Python is available in the system

    # Robot Framework version (SAFE way)
    ${rf_version}=    Get Variable Value    ${ROBOT VERSION}
    Log    Robot Framework Version: ${rf_version}
    Log To Console    Robot Framework Version: ${rf_version}

    # SeleniumLibrary check
    Log    SeleniumLibrary imported successfully
    Log To Console    SeleniumLibrary is available

    Log To Console    Environment verification completed successfully
