from objectbox.model import *

@Entity(id=1, uid=1)
class Person:
    identifier = Id(id = 1, uid = 1001)
    name = Property(str, id = 2, uid = 1002)
    age = Property(int, id = 3, uid = 1003)
    
    def __init__(self, identifier,  name, age, string: str = ""):
        self.str = string
        self.identifier = identifier
        self.name = name
        self.age = age
    
    def __str__(self):  # Print
        return f"{self.identifier} {self.name} {self.age}"

    def getIdentifier(self):
        return self.identifier

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

@Entity(id=2, uid=2)
class MilitaryPerson:
    identifier = Id(id = 1, uid = 2001)
    name = Property(str, id = 2, uid = 2002)
    age = Property(int, id = 3, uid = 2003)
    rank = Property(int, id = 4, uid = 2004)
    specialization = Property(str, id = 5, uid = 2005)        
    
    def __init__(self, identifier, name, age, rank, specialization, string: str = ""):
        self.str = string
        self.identifier = identifier
        self.name = name
        self.age = age
        self.rank = rank
        self.specialization = specialization
    
    def __str__(self):  # Print
        base_class = super().__str__()
        return f"{base_class} {self.rank} {self.specialization}"

    def getRank(self):
        return self.rank

    def getSpecialization(self):
        return self.specialization

    def setRank(self, rank):
        self.rank = rank

    def setSpecialization(self, specialization):
        self.specialization = specialization

@Entity(id=3, uid=3)
class CivilianPerson():
    identifier = Id(id = 1, uid = 3001)
    name = Property(str, id = 2, uid = 3002)
    age = Property(int, id = 3, uid = 3003)
    occupation = Property(str, id = 4,   uid = 3004)
    
    def __init__(self, identifier, name, age, occupation, string: str = ""):
        self.str = string
        identifier = self.identifier
        name = self.name
        age = self.age
        occupation = self.occupation

    def __str__(self):  # Print
        base_class = super().__str__()
        return f"{base_class} {self.occupation}"

    def getOccupationRank(self):
        return self.occupation

    def setOccupation(self, occupation):
        self.occupation = occupation
