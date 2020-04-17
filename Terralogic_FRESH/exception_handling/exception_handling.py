import xlrd
fd = xlrd.open_workbook("test3.xls")
a = 10
b = 0
try:
    c = a / b
except ArithmeticError,ZeroDivisionError:
    print "error is occured "
try:
    print c
except NameError:
    print "c is not defined"
