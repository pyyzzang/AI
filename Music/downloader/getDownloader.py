from .youtubeDownloader import youtubeDownloader


class getDownloader:
    @staticmethod
    def getDownloader(type):
        return youtubeDownloader();
