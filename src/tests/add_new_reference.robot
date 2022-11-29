*** Settings ***
Resource  resource.robot
Test setup  Input New Command And Add Book Reference


*** Test Cases ***
Add Book Reference
    Input Reference  Martin09  'Martin, Robert'  'Clean Code: A Handbook of Agile Software Craftsmanship'  2008  'Prentice Hall'
    Output Should Contain  ""


*** Keywords ***
Input New Command And Input Reference
    #Add Book Reference  Martin09  'Martin, Robert'  'Clean Code: A Handbook of Agile Software Craftsmanship'  2008  'Prentice Hall'
    Input Add  1
    Input Reference  Martin09  'Martin, Robert'  'Clean Code: A Handbook of Agile Software Craftsmanship'  2008  'Prentice Hall'
    Input New Command