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
    
        
