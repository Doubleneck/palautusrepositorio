*** Settings ***
Resource  resource.robot
Resource  login_resource.robot 
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  newuser
    Set Password  1newus23
    Set Password Confirmation  1newus23
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  us
    Set Password  1newus23
    Set Password Confirmation  1newus23
    Submit Credentials
    Register Should Fail With Message  Username must have at least 3 characters and contain only lower-case-letters

Register With Valid Username And Too Short Password
    Set Username  useri 
    Set Password  kalle4
    Set Password Confirmation  kalle4
    Submit Credentials 
    Register Should Fail With Message  Password must have at least 8 characters and must not contain only letters

Register With Nonmatching Password And Password Confirmation  
    Set Username  useri 
    Set Password  salasana123
    Set Password Confirmation  salasana124
    Submit Credentials
    Register Should Fail With Message  Password and Password confirmation don't match

Login After Successful Registration
    Set Username  newuser
    Set Password  1newus23
    Set Password Confirmation  1newus23
    Submit Credentials
    Register Should Succeed
    Submit Ohtumain
    Access Ohtu main Succeed
    Submit Logout
    Login Page Should Be Open
    Set Username  newuser
    Set Password  1newus23
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration     
    Set Username  useri 
    Set Password  salasana123
    Set Password Confirmation  salasana124
    Submit Credentials
    Register Should Fail With Message  Password and Password confirmation don't match
    Submit Login
    Login Page Should Be Open
    Set Username  useri
    Set Password  salasana123
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Access Ohtu main Succeed
    Ohtu Application Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}  
    Input Password  password  ${password}

Set Password Confirmation  
    [Arguments]  ${password_confirmation}      
    Input Password  password_confirmation  ${password_confirmation}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

Submit Ohtumain
    Click Link  ohtu  

Submit Logout
    Click Button  Logout      

Submit Login
    Click Link  Login   