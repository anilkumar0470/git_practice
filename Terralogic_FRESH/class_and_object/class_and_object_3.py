class Std():
    '''this is example of initializer taking parameters'''
    def __init__(self,name,age):
        self.name =name
        self.age = age
    def display_std_details(self):
        print "Name:",self.name,"Age:",self.age
s=Std("something",20)
print "hello", s.__doc__
print "hai",s.__module__
print "he",s.__dict__
s.display_std_details()