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

Add Book Reference With Empty Input
    User Input  1
    User Input  \
    Run Application With Inputs
    Output Should Contain  \nSyöte ei saa olla tyhjä\n

Add Book Reference With Only Whitespace Input
    User Input  1
    User Input  ${SPACE}
    Run Application With Inputs
    Output Should Contain  \nSyöte ei saa olla tyhjä\n

Add Book Reference With Negative Year
    User Input  1
    User Input  @{KEY}
    User Input  @{AUTHOR}
    User Input  @{BOOK}
    User Input  -1
    User Input  @{PUBLISHER}
    Run Application With Inputs
    Output Should Contain  \nJulkaisuvuoden tulee olla positiivinen luku\n

Add Book Reference With String As Year
    User Input  1
    User Input  @{KEY}
    User Input  @{AUTHOR}
    User Input  @{BOOK}
    User Input  Otava
    User Input  @{PUBLISHER}
    Run Application With Inputs
    Output Should Contain  \nJulkaisuvuoden tulee olla positiivinen luku\n

Add Book Reference With Existing Key
    User Input  1
    User Input  @{KEY}
    User Input  @{AUTHOR}
    User Input  @{BOOK}
    User Input  @{YEAR}
    User Input  @{PUBLISHER}
    Run Application With Inputs
    Output Should Contain  \nViite lisätty \n

    User Input  1
    User Input  @{KEY}
    Run Application With Inputs
    Output Should Contain   \nTällä avaimella löytyy jo viite\n