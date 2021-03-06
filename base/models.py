from asyncio.windows_events import NULL
from django.db import models
from django.test import tag


class Tag(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    tag_name = models.CharField(max_length=255)

    def __str__(self):
        return self.tag_name



class Note(models.Model):
    note_title = models.CharField(max_length=100)
    note_subject = models.TextField(default=NULL)
    leaf_tag = models.ManyToManyField(Tag, default=NULL, blank=True)

    def __str__(self):
        return self.note_title


