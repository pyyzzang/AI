from django.db.migrations.state import ModelState
from django.http import JsonResponse, HttpResponse, FileResponse;
from ..models import musicModel;
import django.core.serializers as serializers;
from ..data.staticData import staticData;
import os;
from django.core.files.storage import FileSystemStorage;

class fileApi:
    @staticmethod
    def MusicList(response):
        allFiles = musicModel.objects.filter(enable="Y");

        for file in allFiles:
            if "" == file.fileName:
                file.fileName = file.title;

        json_dic = serializers.serialize("json", allFiles);
        return HttpResponse(json_dic);

    @staticmethod
    def DownloadFile(request):

        id = request.GET.get("id");
        musicModelData = musicModel.objects.filter(id=id)

        if 0 == musicModelData.count():
            return HttpResponse("File Not Exists");
        fileName = musicModelData[0].fileName;
        fileFullPath = staticData.getMusicPath() + id;

        if False == os.path.isfile(fileFullPath):
            return HttpResponse("File Not Exists");

        fs = FileSystemStorage(fileFullPath);
        response = FileResponse(fs.open(fileFullPath, "rb"), content_type="application/file");
        response['Content-Disposition'] = 'attachment; filename="' + fileName + '"';
        return response;

    @staticmethod
    def StreamingFile(request):
        fileName = request.GET.get("fileName");
        print("fileName : " + 'attachment; filename="' + fileName + '"');
        fileFullPath = staticData.getMusicPath() + fileName;

        if False == os.path.isfile(fileFullPath):
            return HttpResponse("File Not Exists");

        fs = FileSystemStorage(fileFullPath);
        response = FileResponse(fs.open(fileFullPath, "rb"), content_type="video/mp4");
        response['Accept-Ranges'] = 'bytes';
        return response;