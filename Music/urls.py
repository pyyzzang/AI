from django.urls import path;
from .api.downloadApi import downloadApi;
from .api.fileApi import fileApi;
from .api.listApi import listApi;


urlpatterns = [
    path('Download/', downloadApi.Download)
    , path('DownloadTest/', downloadApi.DownloadTest)
    , path('MusicList/', fileApi.MusicList)
    , path('InsertMusicList/', listApi.InsertMusicList)
    , path('GetMusicList/', listApi.GetMusicList)
    , path('DownloadFile/', fileApi.DownloadFile)
    , path('StreamingFile/', fileApi.StreamingFile)

]
