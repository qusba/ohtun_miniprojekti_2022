*** Settings ***
Resource  resource.robot

*** Variables ***
@{KEY}  Martin09
@{AUTHOR}  Martin, Robert
@{BOOK}  Clean Code: A Handbook of Agile Software Craftsmanship
@{YEAR}  2008
@{PUBLISHER}  Prentice Hall


*** Test Cases ***
Create BibTeX File From Empty Storage
    User Input  3
    Run Application With Inputs
    Output Should Contain  Ei viitteitä \n

Create BibTeX File From Non Empty Storage
    User Input  1
    User Input  @{KEY}
    User Input  @{AUTHOR}
    User Input  @{BOOK}
    User Input  @{YEAR}
    User Input  @{PUBLISHER}
    User Input  3
    Run Application With Inputs
    Output Should Contain  references.bib tiedosto luotu \n