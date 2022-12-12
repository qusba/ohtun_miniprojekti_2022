*** Settings ***
Resource  resource.robot

*** Test Cases ***
Create BibTeX File From Empty Storage
    User Input  3
    Run Application With Inputs
    Output Should Contain  Ei viitteitä \n

Create BibTeX File From Non Empty Storage
    User Input  1
    User Input  @{KEY}
    User Input  @{AUTHOR_FIRST_NAME}
    User Input  @{AUTHOR_LAST_NAME}
    User Input  @{BOOK}
    User Input  @{YEAR}
    User Input  @{PUBLISHER}
    User Input  3
    Run Application With Inputs
    Output Should Contain  references.bib tiedosto luotu sijaintiin ${EXECDIR}\n