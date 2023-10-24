import persistent
import persistent.list
import ZODB
import ZODB.FileStorage
import transaction
import BTrees.OOBTree


class User(persistent.Persistent):
    def __init__(self, userName, adress, email, age, gender, playlists):
        self.userName = userName
        self.adress = adress
        self.email = email
        self.age = age
        self.gender = gender
        self.playlists = playlists

    def __eq__(self, other):
        return self.userName == other.userName

    def __gt__(self, other):
        return self.age > other.age

    def __lt__(self, other):
        return self.age < other.age

    def __ne__(self, other):
        return self.userName != other.userName

    # getters

    def getUserName(self):
        return self.userName

    def getAdress(self):
        return self.adress

    def getEmail(self):
        return self.email

    def getAge(self):
        return self.age

    def getGender(self):
        return self.gender

    def getPlayLists(self):
        return self.playlists

    # setters

    def setUserName(self, newUserName):
        self.userName = newUserName

    def setAdress(self, newAdress):
        self.adress = newAdress

    def setEmail(self, newEmail):
        self.email = newEmail

    def setAge(self, newAge):
        self.age = newAge

    def setGender(self, newGender):
        self.gender = newGender

    def setPlayLists(self, newPlayLists):
        self.playlists = newPlayLists


class Music(persistent.Persistent):
    def __init__(self, title, genre, duration, isVideo, writer, producer, artists):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.isVideo = isVideo  # determine if the music has a video clip
        self.writer = writer
        self.producer = producer
        self.artists = artists

    # getters
    def getTitle(self):
        return self.title

    def getGenre(self):
        return self.genre

    def getDuration(self):
        return self.duration

    def getIsVideo(self):
        return self.isVideo

    def getWriter(self):
        return self.writer

    def getProducer(self):
        return self.producer

    def getArtists(self):
        return self.artists

    # setters
    def setTitle(self, value):
        self.title = value

    def setGenre(self, value):
        self.genre = value

    def setDuration(self, value):
        self.duration = value

    def setIsVideo(self, value):
        self.isVideo = value

    def setWriter(self, value):
        self.writer = value

    def setProducer(self, new_producer):
        self.producer = new_producer


"""
Mother class that is inherited,
it specifies the base information
that an aggregation of musics should
have.
"""


class MusicGrouping(persistent.Persistent):
    def __init__(self, date):
        self.musicList = persistent.list.PersistentList()
        self.name = ""
        self.date = date

    def getMusicList(self):
        return self.musicList

    def addToMusicList(self, music):
        self.musicList.append(music)

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDate(self):
        return self.date


"""
List of Musics that a user can create and modify
at his own will.
"""


class PlayList(MusicGrouping):  # TO DO allow user to remove music
    def __init__(self, date):
        MusicGrouping.__init__(self, date)
        self.modificationDate = MusicGrouping.getDate(self)

    def getModificationDate(self):
        return self.modificationDate

    def setModificationDate(self, newDate):
        self.modificationDate = newDate


"""
Album released by singers/Producers, once released
it cannot be musics cannot be changed.
"""


class Album(MusicGrouping):
    def __init__(self, date):
        MusicGrouping.__init__(self, date)
        self.singerName = ""
        self.producerName = ""

    def getSingerName(self):
        return self.singerName

    def getProducerName(self):
        return self.producerName


def createZODB(fileName):
    storage = ZODB.FileStorage.FileStorage(fileName)
    db = ZODB.DB(storage)
    return db


def getTestUsers(n, tree):
    for i in range(0, n):
        print(i)
        name = "HAHA" + str(i)
        genre = "POP" + str(i)
        duration = i
        isVideo = (i % 2 == 0)
        writer = "Jean" + str(i)
        producer = "Frank" + str(i)
        artists = "Paul" + str(i)
        date = "22-10-2023"
        userName = "User" + str(i)
        adress = "Rue idk" + str(i)
        email = userName + "@gmail.com"
        age = 20 + i
        gender = "M" if i % 2 == 0 else "F"

        music = Music(name, genre, duration,
                      isVideo, writer, producer, artists)
        playList = PlayList(date)
        user = User(userName, adress,
                    email, age, gender, playList)
        user.playlists.addToMusicList(music)
        tree.insert(user, str(i))
        transaction.commit()
        # print(user.getUserName(), " ", user.getAge(), " ", user.getEmail()
        #  , " ", user.getPlayLists().getMusicList())


def main():
    choice = input("\"start\" to create the db and inserting an object\n"
                   "\'load\" to load the database and see the object\nInput : ")
    if choice == "start":
        db = createZODB("MyZopeOODB.fs")
        connection = db.open()
        root = connection.root()
        root['Users'] = BTrees.OOBTree.BTree()
        getTestUsers(20, root['Users'])
        connection.close()
    if choice == "load":
        storage = ZODB.FileStorage.FileStorage('MyZopeOODB.fs')
        db = ZODB.DB(storage)
        connection = db.open()
        root = connection.root()
        usersTree = root["Users"]
        print("done")
        for userKey in usersTree:
            user = usersTree[userKey]
            print(user, ': ', userKey.getUserName())
            # print(user.getUserName(), " ", user.getAge(), " ", user.getEmail(),
            #      " ", user.getPlayLists().getMusicList())
        connection.close()
    return 0


main()
