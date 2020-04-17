class Parent():
    parentattr = 100

    def __init__(self):
        print "calling  parent constructor"

    def parentmethod(self):
        print 'calling parent method'

    def setattr(self,attr):
        Parent.parentattr = attr

    def getattr(self):
        print 'parrent attribute:',Parent.parentattr


class child(Parent):#define child class
    def __init__(self):
        print "calling child constructor"

    def childmethod(self):
        print 'calling child method'
p = Parent()     #calling  parent constructor
p.parentmethod() #calling parent method
p.getattr()      #parrent attribute: 100
p.setattr(500)   #setting attr as 500
p.getattr()      #parrent attribute: 500
c = child()      #instance of child @calling child constructor
c.childmethod()  #child calls its method @calling child method
c.parentmethod() #calls parent method@calling parent method
c.setattr(200)   #again call parent method@ sett attr as 200
c.getattr()      #again call parent method@parrent attribute: 200
print dir(c)