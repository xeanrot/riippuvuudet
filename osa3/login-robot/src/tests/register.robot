*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Register With Valid Username And Password
    Input  mikko
    Input  mikko123

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input Login Command