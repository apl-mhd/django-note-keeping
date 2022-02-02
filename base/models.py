from asyncio.windows_events import NULL
from django.db import models
from django.test import tag


class Tag(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    tag_name = models.CharField(max_length=255)
    ordering = models.IntegerField(default=0)

    def __str__(self):
        return self.tag_name



class Note(models.Model):
    title = models.CharField(max_length=100)
    note_subject = models.TextField(default=NULL)
    note_tag = models.TextField(default=NULL)

    def __str__(self):
        return self.title


