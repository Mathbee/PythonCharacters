# coding=utf-8

class AudioFile(object):
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")
        self.filenaem = filename

class MP3File(AudioFile):
    ext = 'mp3'
    def play(self):
        print("playing {} as mp3".format(self.filename))

class OggFile(AudioFile):
    ext = ogg
    def play(self):
        print("playing {} as off".format(self.filename))

class FlacFile(object):
    """
    Though FlacFile class doesn't inherit AudioFile class,
    it also has the same interface as three subclass of AudioFile
    It is called duck typing.
    """
    def __init__(self, filename):
        if not filename.endswith(".flac"):
            raise Exception("Invalid file format")
        self.filename = filename

    def play(self):
        print("playing {} as flac".format(self.filename))

def printClassType(audioFile):
    print(audioFile.play())

if __name__ == '__main__':
mp3 = 

