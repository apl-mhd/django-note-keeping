from asyncio.windows_events import NULL
from django.db import models
from django.test import tag


class Tag(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, default= '0', related_name='children', on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=255)

    def __str__(self):
        return self.tag_name



class Note(models.Model):
    note_title = models.CharField(max_length=100)
    note_subject = models.TextField(default=NULL)
    note_tag = models.TextField(default=NULL)

    def __str__(self):
        return self.note_title


