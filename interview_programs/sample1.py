import logging
log = logging.getLogger(__name__)
logging.basicConfig(filename="sample.log", level=logging.DEBUG,
                    format='%(levelname)s:%(asctime)s::%(message)s')


def sum(a, b):
    log.info("Entering into sum method")
    return a+b
print(__name__)

def sub(a,b):
    log.info("Entering into sub method")
    return a-b


add = sum(150, 20)
log.info("the value is {}".format(add))
subt = sub(250, 10)
log.info("the value is {}".format(subt))



import re
output = {'Audit-Session-ID': '010b850d000000b25ac57a08', 'IP Override': '0.0.0.0', 'Lifetime': '1506', 'Station': '6c:40:08:8c:7e:7a', 'Type': 'RSN', 'Username': 'cisco', 'VLAN Override': ''}
output = str(output)
m = re.search(r"\'Station\'\:\s*(\'[\w\:]+\')",output)
print (m)
print (m.group(1))










"""
import sys
sys.stderr.write("apathapa\n")
sys.stderr.flush()
sys.stdout.write("apathapa\n")
print (sys.argv)

sys.path.append("git_practice//")
#from multi_threading.sample2 import sample2
#from multi_threading.sample2 import *
import multi_threading.sample2


class A():
    def __init__(self):

        #sa.test(self)
    def junk(self):
        print("###")
a = A()
print w
"""