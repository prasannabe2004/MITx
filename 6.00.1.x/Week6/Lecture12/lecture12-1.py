import datetime

class Person(object):
    def __init__(self, name):
        """create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        """return self's last name"""
        return self.lastName

    def setBirthday(self,month,day,year):
        """sets self's birthday to birthDate"""
        self.birthday = datetime.date(year,month,day)

    def getAge(self):
        """returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """return True if self's ame is lexicographically
           less than other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """return self's name"""
        return self.name

me = Person("Prasanna Mohanasundaram")
print me.getLastName()
print me.setBirthday(1,9,1983)
print me.getAge()/365.0

her = Person("Saranya Narayanasamy")
print her.getLastName()
print her.setBirthday(1,9,1988)
print her.getAge()/365.0

daughter = Person("Harshitaa Prasanna")
print daughter.getLastName()
print daughter.setBirthday(3,22,2013)
print daughter.getAge()/365.0

plist = [her, me, daughter]
for p in plist: print p
print plist.sort()
print
for p in plist: print p

