*** Settings ***

Library    OperatingSystem
Library    Collections
Library    C:\\Users\\pathapaa\\Videos\\git_practice\\utils\\common_lib.py

*** Test Cases ***

Testcase1
    ${calculatedTotalPrice} =    set variable    ${42.42}
    ${productPrice1} =    set variable    ${43.15}
    ${calculatedTotalPrice} =    Evaluate    ${calculatedTotalPrice}+${productPrice1}
    log to console   ${calculatedTotalPrice}

Testcase2
    SAMPLE  hi everyone

