from os import listdir;
import os;
from ..models import musicModel
from ..data.staticData import staticData;
import requests;

class baseDownloader:
    def download(self):
        pass;

    def _getFileList(self, __dirPath):
        dirFileList = listdir(__dirPath);
        return dirFileList;

    def _getFileListWithoutExt(self, __dirPath):
        retFileListWithoutExt = {};
        dirFileList = self._getFileList(__dirPath);

        for file in dirFileList:
            retFileListWithoutExt[os.path.splitext(file)[0]] = file;

        return retFileListWithoutExt;


    def _saveItem(self, __item, __downloadComplete):

        try:
            music = musicModel();
            music.id = __item["snippet"]["resourceId"]["videoId"];
            music.title = __item["snippet"]["title"];

            muticThumbnail = __item["snippet"]["thumbnails"]["high"]["url"];
            thumbnailResponse = requests.get(muticThumbnail);
            music.thumbnail = thumbnailResponse.content;

            music.enable = __downloadComplete;
        except :
            music.fileName = "";
            music.title = "";
            music.enable = "N";
        music.save();

        pass;