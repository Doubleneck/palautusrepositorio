*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  pentti  p1entti23
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ab  salasana1234
    Output Should Contain  Username must have at least 3 characters and contain only lower-case-letters

Register With Valid Username And Too Short Password
    Input Credentials  pentti  sa
    Output Should Contain  Password must have at least 8 characters and must not contain only letters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  pentti  salasana
    Output Should Contain  Password must have at least 8 characters and must not contain only letters

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command    