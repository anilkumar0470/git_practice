import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# to set file name in loger we will use fileHandler
file_handler = logging.FileHandler("new_employee.log")
# to add any handler to logger we will use addHandler
logger.addHandler(file_handler)
# specifying the format
formatter = logging.Formatter("%(asctime)s:%(name)s:%(levelname)s::%(message)s")
# adding the format to the filehandler
file_handler.setFormatter(formatter)



class Employee(object):

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

        logger.info("object created successfully for {} with email {}".format(
            self.fullname, self.email))

    @property
    def fullname(self):
        return "{} {}".format(self.fname, self.lname)

    @property
    def email(self):
        return "{}.{}@terralogic.com".format(self.fname, self.lname)


e1 = Employee("Anil", 'Pathapati')
e2 = Employee("sri", "b")

# when we set basicConfig in the class the attributes of basicConfig like filename,
# format and level will be treated as default logger
# to apply your values we need create a logger and attach your requirement to logger
# when we keep logger in your class in the output root logger  is not appearing and
# instead of that your logger will be applied
