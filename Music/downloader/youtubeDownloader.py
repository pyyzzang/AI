import os
from operator import truediv
from turtle import TurtleGraphicsError

from pytubefix import YouTube;
#from pytube import YouTube;
from pytubefix.cli import on_progress

import requests as reqeust;
import json;
from ..models import musicModel, playListModel;
from ..data.staticData import staticData;

from .baseDownloader import baseDownloader

class youtubeDownloader(baseDownloader):
    def __init__(self):
        pass

    def __getYoutubeKey(self) -> str:
        return "&key=" + os.environ.get("GOOGLE_API_KEY", "");

    def __getPlayListUrl(self):
        return "https://www.googleapis.com/youtube/v3/playlists?part=snippet&maxResults=50" + self.__getYoutubeKey();

    def __getPlayListItmeUrl(self):
        return "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50" + self.__getYoutubeKey();

    def __getChannelId(self):
        return "&channelId=UCB8pKQfAKIPx3fLCSHi_w2g";

    def __getPlayListId(self, __id):
        return "&playlistId=" + __id;

    def __getChannelPlayList(self):
        getPlayListUrl = self.__getPlayListUrl() + self.__getChannelId();
        response = reqeust.get(getPlayListUrl);
        responseJsonData = json.loads(response.text);
        return responseJsonData["items"];

    def __getPlayListItem(self, playListId):
        playListIdUrl = self.__getPlayListItmeUrl() + self.__getChannelId() + self.__getPlayListId(playListId);

        print("playListIdUrl : " + playListIdUrl);

        response = reqeust.get(playListIdUrl);
        playListItems = json.loads(response.text);
        return playListItems["items"];

    def __downloadFile(self, __items):
        for item in __items:
            downloadFolderPath = "";
            try:
                youtubeId = item["snippet"]["resourceId"]["videoId"];
                if 0 < musicModel.objects.filter(id=youtubeId).count() :
                    continue;

                youtubeVideoUrl = "https://www.youtube.com/watch?v=" + youtubeId;
                yt = YouTube(youtubeVideoUrl, on_progress_callback=on_progress);
                audioStream = yt.streams.filter(progressive=True, file_extension='mp4' ).order_by("resolution").desc().first()
                audioStream.download(staticData.getMusicPath(), filename=youtubeId);
                self._saveItem(item, "Y");

            except Exception as e:
                self._saveItem(item, "N");
        return None;
    def __getPlayListFromDb(self):
        return playListModel.objects.all();

    def downloadFile(self):

        yt = YouTube("https://www.youtube.com/watch?v=qLJq2muxhWc", on_progress_callback=on_progress);
        title = yt.title;
        streams = yt.streams.get_audio_only().download(output_path=staticData.getMusicPath());
        '''
        yt = YouTube('https://www.youtube.com/watch?v=qLJq2muxhWc', on_progress_callback = on_progress)
        yt.streams.order_by('resolution').desc().first().download();
        '''

    def download(self):
        playItemList = self.__getChannelPlayList();
        #playItemList = self.__getPlayListFromDb();

        if None == playItemList:
            return ;

        for item in playItemList:
            playListItems = self.__getPlayListItem(item["id"]);
            self.__downloadFile(playListItems);
        return None;
