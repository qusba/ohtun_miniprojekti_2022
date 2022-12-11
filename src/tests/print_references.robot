*** Settings ***
Resource  resource.robot

*** Test Cases ***
Print All References From Empty Storage
    User Input  2
    Run Application With Inputs
    Print References
    Output Should Contain  Syötä 1 lisätäksesi viite

Print All References From Non Empty Storage
    User Input  1
    User Input  @{KEY}
    User Input  @{AUTHOR_FIRST_NAME}
    User Input  @{AUTHOR_LAST_NAME}
    User Input  @{BOOK}
    User Input  @{YEAR}
    User Input  @{PUBLISHER}
    User Input  2
    User Input  1
    Run Application With Inputs
    Print References
    Output Should Contain  \x1b[0;33mkey\x1b[0m: \x1b[1;31mMartin09\x1b[0m, \x1b[0;33mauthor\x1b[0m: \x1b[1;32mMartin, Robert\x1b[0m, \x1b[0;33mtitle\x1b[0m: \x1b[1;34mClean Code: A Handbook of Agile Software Craftsmanship\x1b[0m, \x1b[0;33myear\x1b[0m: \x1b[1;35m2008\x1b[0m, \x1b[0;33mpublisher\x1b[0m: \x1b[1;36mPrentice Hall\x1b[0m