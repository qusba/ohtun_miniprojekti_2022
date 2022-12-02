*** Settings ***
Resource  resource.robot

*** Variables ***
@{KEY}  Martin09
@{AUTHOR}  Martin, Robert
@{BOOK}  Clean Code: A Handbook of Agile Software Craftsmanship
@{YEAR}  2008
@{PUBLISHER}  Prentice Hall


*** Test Cases ***
Add Book Reference
    User Input  1
    User Input  @{KEY}
    User Input  @{AUTHOR}
    User Input  @{BOOK}
    User Input  @{YEAR}
    User Input  @{PUBLISHER}
    Run Application With Inputs
    Print References
    Output Should Contain  \nViite lisätty \n
