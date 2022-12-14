*** Settings ***
Resource  resource.robot

*** Test Cases ***
References Can Be Sorted By First Surname Of First Author In Alphabetical Order
    User Input  1
    User Input  @{KEY}
    User Input  @{AUTHOR_FIRST_NAME}
    User Input  @{AUTHOR_LAST_NAME}
    User Input  @{BOOK}
    User Input  @{YEAR}
    User Input  @{PUBLISHER}
    User Input  \
    User Input  2
    User Input  3
    User Input  Martin09
    Run Application With Inputs
    Output Should Contain  \x1b[0;33mkey\x1b[0m: \x1b[1;31mMartin09\x1b[0m, \x1b[0;33mauthor\x1b[0m: \x1b[1;32mMartin\x1b[0m, \x1b[1;32mRobert\x1b[0m, \x1b[0;33mtitle\x1b[0m: \x1b[1;34mClean Code: A Handbook of Agile Software Craftsmanship\x1b[0m, \x1b[0;33myear\x1b[0m: \x1b[1;35m2008\x1b[0m, \x1b[0;33mpublisher\x1b[0m: \x1b[1;36mPrentice Hall\x1b[0m