class Music:
    def __init__(self, title, genre, duration, video, writer, producer artists):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.isVideo = isVideo  #determine if the music has a video clip
        self.writer = writer
        self.producer = producer
        self.artists = artists

    #getters
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

    def getproducer(self):
        return self.producer
    
    def getArtists(self):
        return self.artists


    #setters
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

    def getArtists(self, value):
        self.artists = value
    
        
"""
Mother class that is inherited,
it specifies the base information
that an aggregation of musics should
have.
"""
class MusicGrouping :
    def __init__(self,date):
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
class PlayList(MusicGrouping) :#TO DO allow user to remove music
    def __init__(self,date):
        MusicGrouping.__init__(self,date)
        self.modificationDate = MusicGrouping.getDate(self)

    def getModificationDate(self):
        return self.modificationDate
    def setModificationDate(self, newDate):
        self.modificationDate = newDate

"""
Album released by singers/Producers, once released
it cannot be musics cannot be changed.
"""
class Album(MusicGrouping) :
    def __init__(self,date):
        MusicGrouping.__init__(self,date)
        self.singerName
        self.producerName

    def getSingernName(self):
        return self.singerName
    def getProducerName(self):
        return self.producerName

