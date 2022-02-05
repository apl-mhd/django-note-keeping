from . import views
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Note
from . serializers import NoteSerrializer


@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(api_urls)



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
