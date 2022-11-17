*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0 seconds
${HOME URL}  http://${SERVER}
${LOGIN URL}  http://${SERVER}/login
${REGISTER URL}  http://${SERVER}/register
${OHTU URL}  http://${SERVER}/ohtu

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Ohtu Application Page Should Be Open
    Title Should Be  Ohtu Application main page

Login Page Should Be Open
    Title Should Be  Login

Main Page Should Be Open
    Title Should Be  Ohtu Application main page

Welcome Page Should Be Open
    Title Should Be  Welcome to Ohtu Application!

Register Page Should Be Open
    Title Should Be  Register  

Go To Login Page
    Go To  ${LOGIN URL}

Go To Main Page
    Go To  ${HOME URL}    

Go To Register Page
    Go To  ${REGISTER URL}
