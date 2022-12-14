*** Settings ***
Resource  resource.robot

*** Test Cases ***
Reference Can Be Tagged Upon Creation
    User Input  1
    User Input  @{KEY_3}
    User Input  @{AUTHOR_FIRST_NAME_3}
    User Input  @{AUTHOR_LAST_NAME_3}
    User Input  @{BOOK_3}
    User Input  @{YEAR_3}
    User Input  @{PUBLISHER_3}
    User Input  @{TAG_3}
    User Input  \
    User Input  2
    User Input  2
    User Input  \

    Run Application With Inputs
    Output Should Contain  \x1b[0;33mkey\x1b[0m: \x1b[1;31m3\x1b[0m, \x1b[0;33mauthor\x1b[0m: \x1b[1;32mCharles\x1b[0m, \x1b[1;32mDickens\x1b[0m, \x1b[0;33mtitle\x1b[0m: \x1b[1;34mOliver Twist\x1b[0m, \x1b[0;33myear\x1b[0m: \x1b[1;35m1837\x1b[0m, \x1b[0;33mpublisher\x1b[0m: \x1b[1;36mKaristo\x1b[0m, \x1b[0;33mtagit\x1b[0m: \x1b[1;37mSeikkailu\x1b[0m

Reference Can Be Tagged After Creation
    User Input  1
    User Input  @{KEY_2}
    User Input  @{AUTHOR_FIRST_NAME_2}
    User Input  @{AUTHOR_LAST_NAME_2}
    User Input  @{BOOK_2}
    User Input  @{YEAR_2}
    User Input  @{PUBLISHER_2}
    User Input  \
    User Input  5
    User Input  @{KEY_2}
    User Input  @{TAG_2}
    User Input  \
    User Input  2
    User Input  2
    User Input  \
    
    Run Application With Inputs
    Output Should Contain  \x1b[0;33mkey\x1b[0m: \x1b[1;31m2\x1b[0m, \x1b[0;33mauthor\x1b[0m: \x1b[1;32mSophie\x1b[0m, \x1b[1;32mKinsella\x1b[0m, \x1b[0;33mtitle\x1b[0m: \x1b[1;34mHimoshoppaajan salaiset unelmat\x1b[0m, \x1b[0;33myear\x1b[0m: \x1b[1;35m1995\x1b[0m, \x1b[0;33mpublisher\x1b[0m: \x1b[1;36mWSOY\x1b[0m, \x1b[0;33mtagit\x1b[0m: \x1b[1;37mTalous\x1b[0m

Reference Can Have Multiple Tags
    User Input  1
    User Input  @{KEY}
    User Input  @{AUTHOR_FIRST_NAME}
    User Input  @{AUTHOR_LAST_NAME}
    User Input  @{BOOK}
    User Input  @{YEAR}
    User Input  @{PUBLISHER}
    User Input  @{TAG}
    User Input  @{TAG_2}
    User Input  @{TAG_3}
    User Input  \
    User Input  2
    User Input  2
    User Input  \

    Run Application With Inputs
    Output Should Contain  \x1b[0;33mkey\x1b[0m: \x1b[1;31mMartin09\x1b[0m, \x1b[0;33mauthor\x1b[0m: \x1b[1;32mMartin\x1b[0m, \x1b[1;32mRobert\x1b[0m, \x1b[0;33mtitle\x1b[0m: \x1b[1;34mClean Code: A Handbook of Agile Software Craftsmanship\x1b[0m, \x1b[0;33myear\x1b[0m: \x1b[1;35m2008\x1b[0m, \x1b[0;33mpublisher\x1b[0m: \x1b[1;36mPrentice Hall\x1b[0m, \x1b[0;33mtagit\x1b[0m: \x1b[1;37mTestitag, Talous, Seikkailu\x1b[0m