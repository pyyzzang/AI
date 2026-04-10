from django.http import JsonResponse;
from ..downloader.getDownloader import getDownloader;
from django.http import HttpResponse;


class downloadApi:
    @staticmethod
    def Download(request):
        downloader = getDownloader.getDownloader("youtube");
        downloader.download();
        retData = {"message": "Success", "code": "0222200"};
        return JsonResponse(retData);

    @staticmethod
    def DownloadTest(request):
        downloader = getDownloader.getDownloader("youtube");
        downloader.downloadFile();
        retData = {"message": "Success", "code": "00044440"};
        return JsonResponse(retData);