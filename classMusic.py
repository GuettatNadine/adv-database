class User:
    def __init__(self, userName, adress, email, age, gender, playlists):
        self.userName = userName
        self.adress = adress
        self.email = email
        self.age = age
        self.gender = gender
        self.playlists = playlists

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


class Music:
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


class MusicGrouping:
    def __init__(self, date):
        self.musicList = []
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


"""
#TEST
music = Music("HAHA", "POP", 5, True, "Jean", "Frank", "Paul")
playList = PlayList("22-10-2023")
user = User(0,"User01","Rue IDK",
            "User01@gmail.com",20,"M",playList)
user.playlists.addToMusicList(music)
print(user.getUserName()," ",user.getAge()," ",user.getEmail()
      ," ",user.getPlayLists().getMusicList())
"""
