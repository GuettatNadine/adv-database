from objectbox.model import *

@Entity(id=1, uid=1)
class Person:
    def __init__(self, identifier, name, age):
        self.identifier = Property(id = 1, uid = 1001)
        self.name = Property(str, id = 2, uid = 1002)
        self.age = Property(int, id = 3, uid = 1003)

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
class MilitaryPerson(Person):
    def __init__(self, identifier, name, age, rank, specialization):
        super().__init__(identifier, name, age)
        self.rank = Property(int, id = 1, uid = 2001)
        self.specialization = Property(str, id = 2, uid = 2002)

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
class CivilianPerson(Person):
    def __init__(self, identifier, name, age, occupation):
        super().__init__(identifier, name, age)
        self.occupation = Property(str, id = 1,   uid = 3001)

    def __str__(self):  # Print
        base_class = super().__str__()
        return f"{base_class} {self.occupation}"

    def getOccupationRank(self):
        return self.occupation

    def setOccupation(self, occupation):
        self.occupation = occupation
