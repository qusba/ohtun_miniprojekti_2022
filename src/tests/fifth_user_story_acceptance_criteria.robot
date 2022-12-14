*** Settings ***
Resource  resource.robot

*** Test Cases ***
User Can Not Create BibTeX File From Empty Storage
    User Input  3
    
    Run Application With Inputs
    Output Should Contain  Ei viitteitä \n

User Can Give Command To Create BibTeX File From References In Storage
    User Input  1
    User Input  @{KEY}
    User Input  @{AUTHOR_FIRST_NAME}
    User Input  @{AUTHOR_LAST_NAME}
    User Input  @{BOOK}
    User Input  @{YEAR}
    User Input  @{PUBLISHER}
    User Input  \
    User Input  3
    User Input  \

    Run Application With Inputs
    Output Should Contain  references.bib tiedosto luotu sijaintiin ${EXECDIR}\n

Program Can Create BibTeX File
    User Input  1
    User Input  @{KEY_2}
    User Input  @{AUTHOR_FIRST_NAME_2}
    User Input  @{AUTHOR_LAST_NAME_2}
    User Input  @{BOOK_2}
    User Input  @{YEAR_2}
    User Input  @{PUBLISHER_2}
    User Input  \
    User Input  3
    User Input  \

    Run Application With Inputs
    Output Should Contain  references.bib tiedosto luotu sijaintiin ${EXECDIR}\n

Program Outputs Absolute Path Where BibTeX File Was Created Into Terminal
    User Input  1
    User Input  @{KEY_3}
    User Input  @{AUTHOR_FIRST_NAME_3}
    User Input  @{AUTHOR_LAST_NAME_3}
    User Input  @{BOOK_3}
    User Input  @{YEAR_3}
    User Input  @{PUBLISHER_3}
    User Input  \
    User Input  3
    User Input  \

    Run Application With Inputs
    Output Should Contain  references.bib tiedosto luotu sijaintiin ${EXECDIR}\n