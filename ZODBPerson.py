import persistent
import persistent.list


class Person(persistent.Persistent):
    def __init__(self, identifier, name, age):
        self.identifier = identifier
        self.name = name
        self.age = age

    def getIdentifier(self):
        return self.identifier

    def getNameBrand(self):
        return self.name

    def getAge(self):
        return self.age

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age


class MilitaryPerson(Person):
    def __init__(self, identifier, name, age, rank, specialization):
        super().__init__(identifier, name, age)
        self.rank = rank
        self.specialization = specialization

    def getRank(self):
        return self.rank

    def getSpecialization(self):
        return self.specialization

    def setRank(self, rank):
        self.rank = rank

    def setSpecialization(self, specialization):
        self.specialization = specialization


class CivilianPerson(Person):
    def __init__(self, identifier, name, age, occupation):
        super().__init__(identifier, name, age)
        self.occupation = occupation

    def getOccupationRank(self):
        return self.occupation

    def setOccupation(self, occupation):
        self.occupation = occupation
