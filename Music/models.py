from django.db import models

from django.db import models;

class musicModel(models.Model):
    id = models.CharField(max_length=100, primary_key=True);
    title = models.CharField(max_length=100);
    fileName = models.CharField(max_length=100);
    thumbnail = models.BinaryField();
    enable = models.CharField(max_length=1);

class playListModel(models.Model):
    id = models.CharField(max_length=100, primary_key=True);
    name = models.CharField(max_length=100);
