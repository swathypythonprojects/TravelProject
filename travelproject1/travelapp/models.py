from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    descr=models.TextField()

    def __str__(self):
        return self.name

class Team(models.Model):
    img1=models.ImageField(upload_to='pics')
    name1=models.CharField(max_length=250)
    about=models.TextField()

    def __str__(self):
        return self.name1
