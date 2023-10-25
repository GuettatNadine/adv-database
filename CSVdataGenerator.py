import faker
import numpy as np
from faker_music import MusicProvider
import csv


def getTestData(n, filename):
    filename += ".csv"
    albumFile = "Album" + filename
    playListFile = "PlayList" + filename
    userFile = "User" + filename
    musicFile = "Music" + filename
    albumToMusic = "albumToMusic" + filename  # for relational database
    playListToMusic = "playListToMusic" + filename  # for relational database
    userToPlayList = "userToPlayList" + filename  # for relational database

    users = n // 2
    playlistMusics = n // 4
    albumMusics = n // 20
    numberOfObjects = 0
    fake = faker.Faker()
    fake.add_provider(MusicProvider)

    with open(albumFile, 'w', newline='') as Afile, open(playListFile, 'w', newline='') as Pfile, \
            open(userFile, 'w', newline='') as Ufile, open(musicFile, 'w', newline='') as Mfile, \
            open(albumToMusic, 'w', newline='') as AMfile, open(playListToMusic, 'w', newline='') as PMfile, \
            open(userToPlayList, 'w', newline='') as UPfile:

        Awriter = csv.writer(Afile)
        Awriter.writerow(["albumId", "date", "title", "arist", "producer"])  # musicId(s)

        AMwriter = csv.writer(AMfile)  # for relational database
        AMwriter.writerow(["albumId", "musicId"])

        Pwriter = csv.writer(Pfile)
        Pwriter.writerow(["playListId", "date", "title"])  # musicId(s)

        PMwriter = csv.writer(PMfile)  # for relational database
        PMwriter.writerow(["playListId", "musicId"])

        Uwriter = csv.writer(Ufile)
        Uwriter.writerow(["userId", "userName", "address", "email", "age", "gender"])  # playlistId(s)

        UPwriter = csv.writer(UPfile)  # for relational database
        UPwriter.writerow(["userId", "playListId"])

        Mwriter = csv.writer(Mfile)
        Mwriter.writerow(
            ["musicId", "title", "genre", "duration", "isVideo", "writer", "producer", "artists", "albumId"])

        # writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
        for albums in range(0, albumMusics):
            gender = np.random.choice(["M", "F"], p=[0.5, 0.5])
            artist = fake.first_name_male() if gender == "M" else fake.first_name_female()
            title = fake.word()
            producer = fake.name()
            numberOfObjects += 1
            Awriter.writerow([albums, fake.date(), fake.word(), artist, producer])  # write on the album file
            for musics in range(5):
                numberOfObjects += 1
                genre = fake.music_genre()
                duration = np.random.randint(179, 250)
                isVideo = np.random.randint(1)
                writer = fake.name()
                producer = fake.name()
                Mwriter.writerow([(albums * 5) + musics, title, genre,
                                  duration, isVideo, writer, producer, artist])
                AMwriter.writerow([albums, (albums * 5) + musics])

        for music in range(0, playlistMusics):
            numberOfObjects += 1
            Pwriter.writerow([music, fake.date(), fake.word()])
            for albums in np.random.choice(albumMusics, np.random.randint(1, 4), replace=False):
                PMwriter.writerow([music, albums])

        for userId in range(0, users):
            numberOfObjects += 1
            # date = fake.date()
            userName = fake.user_name()
            address = fake.address
            email = fake.email()
            age = np.random.randint(17, 110)
            gender = np.random.choice(["M", "F"], p=[0.5, 0.5])
            for playList in np.random.choice(playlistMusics, np.random.randint(2, 4), replace=False):
                UPwriter.writerow([userId, playList])
            Uwriter.writerow([userId, userName, address,
                              email, age, gender])
    return numberOfObjects


sampleSize = input("sample size (number of objects) : ")
fileName = input("file name : ")
fileName += sampleSize
print(getTestData(int(sampleSize), fileName))
