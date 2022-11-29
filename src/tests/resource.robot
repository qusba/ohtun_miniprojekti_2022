*** Settings ***
Library  ../ReferenceLibrary.py

#*** Variables ***
#${KEY}  'Martin09'
#${AUTHOR}  'Martin, Robert'
#${BOOK}  'Clean Code: A Handbook of Agile Software Craftsmanship'
#${YEAR}  '2008'
#${PUBLISHER}  'Prentice Hall'
#${ADD}  1

*** Keywords ***
Input New Command
    Input  new

Input Add
    [Arguments]  ${ADD}
    Input  ${ADD}

Input Reference
    [Arguments]  ${KEY}  ${AUTHOR}  ${BOOK}  ${YEAR}  ${PUBLISHER}
    Input  ${KEY}
    Input  ${AUTHOR}
    Input  ${BOOK}
    Input  ${YEAR}
    Input  ${PUBLISHER}
    Run Application