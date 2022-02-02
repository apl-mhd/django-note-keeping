from multiprocessing import context
from traceback import print_tb
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from . models import Tag
from . models import Note


def home(request):
  
    notes = Note.objects.all()
    tags = Tag.objects.all()
    children = Tag.objects.get(id=8).children.all()
    t = list(Tag.objects.values())
    context = { 'notes': notes, 'tags':tags, 't':t, 'children':children}
    return render(request, 'base/home.html', context)

@csrf_exempt
def save_note(request):

    print("-----------")
    print(request.POST['checkBox'])
    print("-----------")



    if request.method == 'POST':
        title = request.POST['title']
        subject = request.POST['subject']
        note_tag = request.POST.get('checkBox')
        print(note_tag)
        note = Note(title = title, note_subject = subject, note_tag = note_tag)
        note.save()
        notes = list(Note.objects.values())
    return JsonResponse({'status':1, 'notes':notes})
    
    # else:
    #     return JsonResponse({'status':0, 'notes':no})
