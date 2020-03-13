import sys
sys.path.append("git_practice")
from practice_info.sample3 import sample3
#from interview_programs.sample1 import A
w=1
class megs():
    def __init__(self):
        print ("apathapa")
    def test(self,l):
        print("junk")
        #a = A()
        print(type(l))
        print (dir(l))
        l.junk()
        s = sample3()
        s.execute_test()
