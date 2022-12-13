*** Settings ***
Resource  resource.robot

*** Test Cases ***
Add Book Reference With Tag
    User Input  1
    User Input  @{KEY}
    User Input  @{AUTHOR_FIRST_NAME}
    User Input  @{AUTHOR_LAST_NAME}
    User Input  @{BOOK}
    User Input  @{YEAR}
    User Input  @{PUBLISHER}
    User Input  @{TAG}
    User Input  \
    Run Application With Inputs
    Output Should Contain  \nViite lisätty \n

Add Book Reference With Two Tags
    User Input  1
    User Input  @{KEY}
    User Input  @{AUTHOR_FIRST_NAME}
    User Input  @{AUTHOR_LAST_NAME}
    User Input  @{BOOK}
    User Input  @{YEAR}
    User Input  @{PUBLISHER}
    User Input  @{TAG}
    User Input  Testitagi2
    User Input  \
    Run Application With Inputs
    Output Should Contain  \nViite lisätty \n

Add Tag For Existing Book Reference
    User Input  1
    User Input  @{KEY}
    User Input  @{AUTHOR_FIRST_NAME}
    User Input  @{AUTHOR_LAST_NAME}
    User Input  @{BOOK}
    User Input  @{YEAR}
    User Input  @{PUBLISHER}
    User Input  \
    Run Application With Inputs
    Output Should Contain  \nViite lisätty \n
    
    User Input  5
    User Input  @{KEY}
    User Input  @{TAG}
    User Input  \
    Run Application With Inputs
    Output Should Contain  \nTägit lisätty \n

Add Two Tags For Existing Book Reference
    User Input  1
    User Input  @{KEY}
    User Input  @{AUTHOR_FIRST_NAME}
    User Input  @{AUTHOR_LAST_NAME}
    User Input  @{BOOK}
    User Input  @{YEAR}
    User Input  @{PUBLISHER}
    User Input  \
    Run Application With Inputs
    Output Should Contain  \nViite lisätty \n
    
    User Input  5
    User Input  @{KEY}
    User Input  @{TAG}
    User Input  Toinen Tag
    User Input  \
    Run Application With Inputs
    Output Should Contain  \nTägit lisätty \n

Add Empty Tag For Existing Book Reference
    User Input  1
    User Input  @{KEY}
    User Input  @{AUTHOR_FIRST_NAME}
    User Input  @{AUTHOR_LAST_NAME}
    User Input  @{BOOK}
    User Input  @{YEAR}
    User Input  @{PUBLISHER}
    User Input  \
    Run Application With Inputs
    Output Should Contain  \nViite lisätty \n
    
    User Input  5
    User Input  @{KEY}
    User Input  \
    Run Application With Inputs
    Output Should Contain  \nTägejä ei lisätty \n

Add Tag For Non Existing Book Reference
    User Input  5
    User Input  1a2b3c4d5e6f7g
    Run Application With Inputs
    Output Should Contain  Ei vastaavaa viitettä \n