from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from . models import Tag
from . models import Note


def home(request):
  
    notes = Note.objects.all()
    context = { 'notes': notes}
    return render(request, 'base/home.html', context)

@csrf_exempt
def save_note(request):

    print(request.POST)

    if request.method == 'POST':
        title = request.POST['title']
        subject = request.POST['subject']
        note = Note(title = title, note_subject = subject)
        note.save()
        notes = list(Note.objects.values())
    return JsonResponse({'status':1, 'notes':notes})
    
    # else:
    #     return JsonResponse({'status':0, 'notes':no})
