*** Settings ***
Resource  resource.robot

*** Variables ***
@{KEY}  Martin09
@{AUTHOR}  Martin, Robert
@{BOOK}  Clean Code: A Handbook of Agile Software Craftsmanship
@{YEAR}  2008
@{PUBLISHER}  Prentice Hall


*** Test Cases ***
Delete Reference From Empty Storage
    User Input  4
    Run Application With Inputs
    Output Should Contain  Ei vastaavaa viitettä \n

Delete Reference From Non Empty Storage
    User Input  1
    User Input  @{KEY}
    User Input  @{AUTHOR}
    User Input  @{BOOK}
    User Input  @{YEAR}
    User Input  @{PUBLISHER}
    User Input  4
    User Input  Martin09
    Run Application With Inputs
    Output Should Contain  Viite poistettu \n

Delete Reference With Non Existing Key
    User Input  1
    User Input  @{KEY}
    User Input  @{AUTHOR}
    User Input  @{BOOK}
    User Input  @{YEAR}
    User Input  @{PUBLISHER}
    User Input  4
    User Input  CantFindThis
    Run Application With Inputs
    Output Should Contain  Ei vastaavaa viitettä \n