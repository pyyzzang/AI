from django.http import HttpResponse, JsonResponse
from ..models import playListModel
import django.core.serializers as serializers;

class listApi:
    @staticmethod
    def InsertMusicList(request):
        playListId = request.GET.get("PlayListId");
        PlayListName = request.GET.get("PlayListName");
        responseJson = {"Result": "Success", "Message": "", "Code":"0"};

        if("" == playListId or None == playListId or "" == PlayListName):
            responseJson["Result"] = "Fail";
            responseJson["Message"] = "Parameter Missiong";
            return JsonResponse(responseJson);


        if(0 < playListModel.objects.filter(id=playListId).count()):
            responseJson["Result"] = "Fail";
            responseJson["Message"] = "PlayList Exists";
            return JsonResponse(responseJson);

        insertModel = playListModel();
        insertModel.id = playListId;
        insertModel.name = PlayListName;
        insertModel.save();

        return JsonResponse(responseJson);

    @staticmethod
    def GetMusicList(request):
        allLists = playListModel.objects.all();
        json_dic = serializers.serialize("json", allLists);
        return HttpResponse(json_dic);