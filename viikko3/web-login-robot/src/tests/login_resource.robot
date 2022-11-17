
*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Submit Login Credentials
    Click Button  Login    

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}