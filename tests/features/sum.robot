*** Settings ***

Library    tests.keywords.libraries.calculator_library.CalculatorLibrary

Force Tags    sum    suitability

Suite Setup       open calculator
Suite Teardown    close calculator

Test Teardown    clean result

*** Test Cases ***

Verify the sum of positive values
   [Tags]    smoke

   Given the calculator is open
   And the expression "5 + 5" is entered
   When I press the calculate button
   Then the result shown is "10"

Verify the sum of negative values
   [Tags]    sanity

   Given the calculator is open
   And the expression "−5 + 5" is entered
   When I press the calculate button
   Then the result shown is "0"
