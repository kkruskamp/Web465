from django.db import models

# Create your models here.
class Suggestion(models.Model):

    suggestion = models.CharField(max_length=140)
    artist = models.ForeignKey('Artist', on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return self.suggestion

class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
