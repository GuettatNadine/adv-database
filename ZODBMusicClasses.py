import persistent
import persistent.list
import ZODB
import ZODB.FileStorage
import transaction
import BTrees.OOBTree
import faker
import numpy as np
from faker_music import MusicProvider


class User(persistent.Persistent):  # Make Object unique (add id and track the id)
    def __init__(self, userName, address, email, age, gender, userId, playlistIds=persistent.list.PersistentList()):
        self.userName = userName
        self.address = address
        self.email = email
        self.age = age
        self.gender = gender
        self.playlistIds = playlistIds
        self.userId = userId

    # getters
    def __eq__(self, other):
        return self.userId == other

    def __lt__(self, other):
        return self.userId < other

    def __gt__(self, other):
        return self.userId > other

    def getUserId(self):
        return self.userId

    def getUserName(self):
        return self.userName

    def getAddress(self):
        return self.address

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

    def setAddress(self, newAddress):
        self.address = newAddress

    def setEmail(self, newEmail):
        self.email = newEmail

    def setAge(self, newAge):
        self.age = newAge

    def setGender(self, newGender):
        self.gender = newGender

    def setPlaylistIds(self, newPlayListIds):
        self.playlistIds = newPlayListIds

    def addPlaylistId(self, newPlayListId):
        self.playlistIds.append(newPlayListId)

    def removePlaylistId(self, playlistId):
        self.playlistIds.remove(playlistId)


class Music(persistent.Persistent):
    def __init__(self, title, genre, duration, isVideo, writer, producer, artists, albumId):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.isVideo = isVideo  # determine if the music has a video clip
        self.writer = writer
        self.producer = producer
        self.artists = artists
        self.albumId = albumId

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

    def getAlbumId(self):
        return self.albumId

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
    def __init__(self, musicGroupingId, date, name):
        self.musicGroupingId = musicGroupingId
        self.name = name
        self.date = date
        self.musicIds = persistent.list.PersistentList()

    def setName(self, newName):
        self.name = newName

    def getMusicGroupingId(self):
        return self.musicGroupingId

    def getName(self):
        return self.name

    def getDate(self):
        return self.date

    def getMusics(self):
        return self.musicIds

    def removeMusic(self, musicId):
        self.musicIds.remove(musicId)

    def removeMusics(self):
        self.musicIds = persistent.list.PersistentList()

    def setMusicIds(self, musicIdList):
        self.musicIds = musicIdList

    def addMusic(self, musicId):
        self.musicIds.append(musicId)

    def isMusicInGrouping(self, musicId):
        return musicId in self.musicIds


"""
List of Musics that a user can create and modify
at his own will.
"""


class PlayList(MusicGrouping):  # TO DO allow user to remove music
    def __init__(self, musicGroupingId, date, name):
        MusicGrouping.__init__(self, musicGroupingId, date, name)
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
    def __init__(self, musicGroupingId, date, name, singerName, producerName):
        MusicGrouping.__init__(self, musicGroupingId, date, name)
        self.singerName = singerName
        self.producerName = producerName

    def getSingerName(self):
        return self.singerName

    def getProducerName(self):
        return self.producerName


def createZODB(fileName):
    storage = ZODB.FileStorage.FileStorage(fileName)
    db = ZODB.DB(storage)
    return db


def getTestData(n, tree):
    users = n // 2
    playlistMusics = n // 4
    albumMusics = n // 20
    numberOfObjects = 0
    fake = faker.Faker()
    fake.add_provider(MusicProvider)
    for albums in range(0, albumMusics):
        gender = np.random.choice(["M", "F"], p=[0.5, 0.5])
        artist = fake.first_name_male() if gender == "M" else fake.first_name_female()
        title = fake.word()
        producer = fake.name()
        numberOfObjects += 1
        album = Album(albums, fake.date(), fake.word(), artist, producer)
        for musics in range(5):
            numberOfObjects += 1
            genre = fake.music_genre()
            duration = np.random.randint(179, 250)
            isVideo = np.random.randint(1)
            writer = fake.name()
            producer = fake.name()
            tree["Musics"].insert((albums * 5) + musics, Music(title, genre,
                                                               duration, isVideo, writer, producer, artist,
                                                               (albums * 5) + musics))
            album.addMusic((albums * 5) + musics)
            transaction.commit()
        tree["Albums"].insert(albums, album)
        transaction.commit()

    for music in range(0, playlistMusics):
        numberOfObjects += 1
        playList = PlayList(music, fake.date(), fake.word())
        for i in range(1, np.random.randint(1, 4)):
            m = np.random.randint(albumMusics)
            if not playList.isMusicInGrouping(m):
                playList.addMusic(m)
        tree["PlayLists"].insert(music, playList)
        transaction.commit()

    for userId in range(0, users):
        numberOfObjects += 1
        date = fake.date()
        userName = fake.user_name()
        address = fake.address
        email = fake.email()
        age = np.random.randint(17, 110)
        gender = np.random.choice(["M", "F"], p=[0.5, 0.5])
        playList = persistent.list.PersistentList()
        for i in range(1, np.random.randint(1, 4)):
            m = np.random.randint(playlistMusics)
            if not (m in playList):
                playList.append(m)
        user = User(userName, address,
                    email, age, gender, userId, playList)
        tree["Users"].insert(userId, user)
        transaction.commit()
    return numberOfObjects


def main():
    choice = input("\"start\" to create the db and inserting an object\n"
                   "\'load\" to load the database and see the object\nInput : ")
    if choice == "start":
        db = createZODB("MyZopeOODB.fs")
        connection = db.open()
        root = connection.root()
        root['Users'] = BTrees.OOBTree.BTree()
        root['Albums'] = BTrees.OOBTree.BTree()
        root['PlayLists'] = BTrees.OOBTree.BTree()
        root['Musics'] = BTrees.OOBTree.BTree()
        n = input("approx. number of objects wanted :")
        print(getTestData(int(n), root))
        connection.close()
    if choice == "load":
        storage = ZODB.FileStorage.FileStorage('MyZopeOODB.fs')
        db = ZODB.DB(storage)
        connection = db.open()
        root = connection.root()
        print("Select userName From User where id = 485")
        queryResults = list(root["Users"].values(485,485))
        for queryResult in queryResults:
            print(
                "user : " + queryResult.getUserName() + " | " + "id : " + str(queryResult.getUserId()))
        print("done")
        connection.close()
    return 0


main()
