from dataclasses import fields
from rest_framework import serializers
from base.models import Note, Tag


class NoteSerrializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
