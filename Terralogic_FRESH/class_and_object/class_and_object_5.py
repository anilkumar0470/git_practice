#if both parrent and child class containing same method then
#parent class method is override with child  class method
class Parent:
    parentAttr = 100
    def __init__(self):
        print "calling parent constructor"
    def Method(self):
        print 'calling parent method'

class Child(Parent):#define child class
    def __init__(self):
        print "calling child constructor"
    def Method(self):
        print 'calling child method'
p = Parent()
print dir(p)
print p.Method()
print "====child===="
c = Child()
print dir(c)
c.Method()