from ast import Not
from . import views
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Note, Tag
from . serializers import NoteSerrializer, TagSerializer
from base import api

from base.api import serializers


@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		'Last Note':'/note-last/',
		'Leaf Tag': '/leaf-tag/',
		
		}

	return Response(api_urls)


@api_view(['GET'])
def leafTag(request):
	
	parentId = {i[0] for i in Tag.objects.values_list('parent_id')}
	childTags = Tag.objects.exclude(id__in = parentId)
	serializers = TagSerializer(childTags, many=True)
	return Response(serializers.data)

@api_view(['GET'])
def noteLast(request):
	lastNote = Note.objects.latest('id')
	serializers = NoteSerrializer(lastNote, many=False)
	return Response(serializers.data)
	


@api_view(['GET'])
def noteList(request):
    notes = Note.objects.all().order_by('-id')
    serializer = NoteSerrializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def noteDetail(request, pk):

    note = Note.objects.get(id=pk)
    serializer = NoteSerrializer(note, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def noteCreate(request):
	print(request.data)
	#{'id': 44, 'note_title': 'api', 'note_subject': 'Hello', 'leaf_tag': [2, 3, 4, 5]}
	#javascrip form {'note_title': 'api2', 'note_subject': 'aoafa'}
	serializer =NoteSerrializer(data = request.data)
	
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['POST'])
def noteUpdate(request, pk):
	note = Note.objects.get(id=pk)
	serializer = NoteSerrializer(instance=note,  data=request.data)

	if serializer.is_valid():
	  	serializer.save()

	return Response(serializer.data)

# @api_view(['DELETE'])
# def noteDelete(request, pk):
# 	note = Note.objects.get(id=pk)
# 	note.delete()

# 	return Response("Item successfully deleted")
