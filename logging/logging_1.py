# why we need use logging when we have print?
# when we will use everything will print .. logging module provide different log levels
# so that depending on the necessary we can set the mode.
# For example , while running the regression we no need to entire log ..that we will keep
# log as INFO
import logging
print(dir(logging))


def add(x, y):
    return x + y


def sub(x, y):
    return x -y


def multiply(x, y):
    return x * y


def divide(x, y):
    try:
        result =  x/y
    except Exception:
        logger.exception("Zero division error")



# x = 10
# y = 2
# add1 = add(x, y)
# logging.warning("the sum of x {} and y {} is {}".format(x, y, add1))
#
# sub1 = sub(x, y)
# logging.warning("the difference between x {} and y{} is {}".format(x, y, sub1))
#
# mul1 = multiply(x, y)
# logging.warning("the multiplication of  x {} and y {} is {}".format(x, y, mul1))
#
# div1 = divide(x, y)
# logging.warning("the divison of x {} by y {} is {}".format(x, y, div1))

# different log levels are
# debug : typically intersted when u r diagnosing the problem
# info : confirmation that things are working fine
# warning : Indication that in future we have problem the software still works as expected
# example low memory
# error : due to serious problem the software is not able to perform some functions
# critical : due to serious error programm not able to continue further

# Default level for logging is WARNING means above warning everything will print like error and
# critical will automatically displayed during the log

# to set the logging level we will use basicConfig method in which we can specify the
# level and format and filename to create a log
import class_example_with_logging

x = 100
y = 0

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# to set file name in loger we will use fileHandler
file_handler = logging.FileHandler("sample.log")
# to add any handler to logger we will use addHandler
logger.addHandler(file_handler)
# specifying the format
formatter = logging.Formatter("%(asctime)s:%(name)s:%(levelname)s::%(message)s")
# adding the format to the filehandler
file_handler.setFormatter(formatter)
# we can also specify the logging level at file handler as well
file_handler.setLevel(logging.ERROR)

# when we run the above code console output is empty. to add messages into we will
# stream handler
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
stream_handler.setFormatter(formatter)
add1 = add(x, y)
logger.debug("the sum of x {} and y {} is {}".format(x, y, add1))

sub1 = sub(x, y)
logger.debug("the difference between x {} and y{} is {}".format(x, y, sub1))

mul1 = multiply(x, y)
logger.debug("the multiplication of  x {} and y {} is {}".format(x, y, mul1))

div1 = divide(x, y)
logger.debug("the divison of x {} by y {} is {}".format(x, y, div1))


# try to import the employee module and observe the output
# Even we have set the basicConfig in the logging_1.py still we are not able to see
# any logging messages in log file because ..initially we are importing the employee
# module so the code available in the employee module will be executed and logging
# level set according to employee and it is consider as root logging so even if you
# keep any changes in the current file it will not reflect in the log file
# to overcome this add logger in current file
# when we set basicConfig in the class the attributes of basicConfig like filename,
# format and level will be treated as default logger
# to apply your values we need create a logger and attach your requirement to logger
# when we keep logger in your class in the output root logger  is not appearing and
# instead of that your logger will be applied


# Exception method in logger will allow to add traceback also into the log
