*** Settings ***

Library    tests.keywords.libraries.calculator_library

Test Setup       open calculator
Test Teardown    close calculator

*** Test Cases ***

Verify the sum of positive values
   [Tags]    suitability    smoke

   Given the calculator is open
   And the expression "5 + 5" is entered
   When I press the calculate button
   Then the result shown is "10"
