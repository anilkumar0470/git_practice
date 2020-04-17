class Sample():
    """a virtual pet"""
    def __init__(self,name,mood):
        print "a new critter has been created"
        self.name = name    #public attribute
        self.__mood = mood  #private attribute

    def talk(self):
        print "\n i'm",self.name
        print "right now i feeling",self.__mood,""

    def __private_method(self):
        print "this is a private method"
    def public_method(self):
        print "this is a public method"
        self.__private_method()
s = Sample(name = "kumar",mood="happy because of classes are over")
s.talk()
s.public_method()
print s