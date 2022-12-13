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
    User Input  \
    User Input  2
    User Input  1
    Run Application With Inputs
    Print References
    Output Should Contain  \x1b[0;33mkey\x1b[0m: \x1b[1;31mMartin09\x1b[0m, \x1b[0;33mauthor\x1b[0m: \x1b[1;32mMartin\x1b[0m, \x1b[1;32mRobert\x1b[0m, \x1b[0;33mtitle\x1b[0m: \x1b[1;34mClean Code: A Handbook of Agile Software Craftsmanship\x1b[0m, \x1b[0;33myear\x1b[0m: \x1b[1;35m2008\x1b[0m, \x1b[0;33mpublisher\x1b[0m: \x1b[1;36mPrentice Hall\x1b[0m

Print All References In Reversed Order
    User Input  1
    User Input  @{KEY}
    User Input  @{AUTHOR_FIRST_NAME}
    User Input  @{AUTHOR_LAST_NAME}
    User Input  @{BOOK}
    User Input  @{YEAR}
    User Input  @{PUBLISHER}
    User Input  \
    User Input  1
    User Input  @{SECOND_KEY}
    User Input  @{SECOND_AUTHOR_FIRST_NAME}
    User Input  @{SECOND_AUTHOR_LAST_NAME}
    User Input  @{SECOND_BOOK}
    User Input  @{YEAR}
    User Input  @{SECOND_PUBLISHER}
    User Input  \
    User Input  2
    User Input  2
    Run Application With Inputs
    Print Reversed References
    First Reference Should Be  \x1b[0;33mkey\x1b[0m: \x1b[1;31mkey2\x1b[0m, \x1b[0;33mauthor\x1b[0m: \x1b[1;32mAntti\x1b[0m, \x1b[1;32mArvuuttaja\x1b[0m, \x1b[0;33mtitle\x1b[0m: \x1b[1;34mTestikirja\x1b[0m, \x1b[0;33myear\x1b[0m: \x1b[1;35m2008\x1b[0m, \x1b[0;33mpublisher\x1b[0m: \x1b[1;36mOtava\x1b[0m

Print All References In Alphabetical Order
    User Input  1
    User Input  @{KEY}
    User Input  @{AUTHOR_FIRST_NAME}
    User Input  @{AUTHOR_LAST_NAME}
    User Input  @{BOOK}
    User Input  @{YEAR}
    User Input  @{PUBLISHER}
    User Input  \
    User Input  1
    User Input  @{SECOND_KEY}
    User Input  @{SECOND_AUTHOR_FIRST_NAME}
    User Input  @{SECOND_AUTHOR_LAST_NAME}
    User Input  @{SECOND_BOOK}
    User Input  @{YEAR}
    User Input  @{SECOND_PUBLISHER}
    User Input  \
    User Input  2
    User Input  3
    Run Application With Inputs
    Print References In Alphabetical Order
    First Reference Should Be  \x1b[0;33mkey\x1b[0m: \x1b[1;31mkey2\x1b[0m, \x1b[0;33mauthor\x1b[0m: \x1b[1;32mAntti\x1b[0m, \x1b[1;32mArvuuttaja\x1b[0m, \x1b[0;33mtitle\x1b[0m: \x1b[1;34mTestikirja\x1b[0m, \x1b[0;33myear\x1b[0m: \x1b[1;35m2008\x1b[0m, \x1b[0;33mpublisher\x1b[0m: \x1b[1;36mOtava\x1b[0m

Print All References In Reversed Alphabetical Order
    User Input  1
    User Input  @{KEY}
    User Input  @{AUTHOR_FIRST_NAME}
    User Input  @{AUTHOR_LAST_NAME}
    User Input  @{BOOK}
    User Input  @{YEAR}
    User Input  @{PUBLISHER}
    User Input  \
    User Input  1
    User Input  @{SECOND_KEY}
    User Input  @{SECOND_AUTHOR_FIRST_NAME}
    User Input  @{SECOND_AUTHOR_LAST_NAME}
    User Input  @{SECOND_BOOK}
    User Input  @{YEAR}
    User Input  @{SECOND_PUBLISHER}
    User Input  \
    User Input  2
    User Input  4
    Run Application With Inputs
    Print References In Reversed Alphabetical Order
    First Reference Should Be  \x1b[0;33mkey\x1b[0m: \x1b[1;31mMartin09\x1b[0m, \x1b[0;33mauthor\x1b[0m: \x1b[1;32mMartin\x1b[0m, \x1b[1;32mRobert\x1b[0m, \x1b[0;33mtitle\x1b[0m: \x1b[1;34mClean Code: A Handbook of Agile Software Craftsmanship\x1b[0m, \x1b[0;33myear\x1b[0m: \x1b[1;35m2008\x1b[0m, \x1b[0;33mpublisher\x1b[0m: \x1b[1;36mPrentice Hall\x1b[0m