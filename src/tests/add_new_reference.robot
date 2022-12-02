*** Settings ***
Resource  resource.robot
Test Setup  Clear Testing File

*** Variables ***
@{KEY}  'Martin09'
@{AUTHOR}  'Martin, Robert'
@{BOOK}  'Clean Code: A Handbook of Agile Software Craftsmanship'
@{YEAR}  '2008'
@{PUBLISHER}  'Prentice Hall'
${BOOKREFERENCE}  1  @{KEY}  @{AUTHOR}  @{BOOK}  @{YEAR}  @{PUBLISHER}


*** Test Cases ***
Add Book Reference
    Run With Parameters  ${BOOKREFERENCE}
    Print References
    Output Should Contain  "Clean Code"


#*** Keywords ***
#Input New Command And Input Reference
#    #Add Book Reference  Martin09  'Martin, Robert'  'Clean Code: A Handbook of Agile Software Craftsmanship'  2008  'Prentice Hall'
#    Input Add  1
#    Input Reference  Martin09  'Martin, Robert'  'Clean Code: A Handbook of Agile Software Craftsmanship'  2008  'Prentice Hall'
#    Input New Command