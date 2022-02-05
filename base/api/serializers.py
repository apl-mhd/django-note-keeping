from dataclasses import fields
from rest_framework import serializers
from base.models import Note


class NoteSerrializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = '__all__'
