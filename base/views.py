from django.db.models import F
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from .models import Note, Tag


def allTags():

    ulS = '<ul>'
    ulE = '</ul>'
    liS = '<li>'
    liE = '</li>'
    htmltag = '<ul>' 

    def recur(id, x): 
        child = Tag.objects.filter(parent_id = id )
        if(len(child) != 0):
            x += '<ul>'
            for j in child:
                id = str(j.id)
                x += '<li> <a class="tagclick" id="'+id +'" href="#">'+ j.tag_name + '</a>'
                x = recur(j.id, x)
            
            x += '</ul>'
        x += '</li>'
        return x

    tags = Tag.objects.filter(parent_id = None)
    
   # print(categories)

    for tag in tags:
        id = str(tag.id)
        htmltag += '<li> <a class="tagclick" id="'+id +'"tag  href="#">'+ tag.tag_name + '</a>'
        htmltag = recur(tag.id, htmltag)

    htmltag += '</ul>'
    return htmltag


def home(request):
    # SELECT * FROM tag WHERE id not IN (SELECT parent_id FROM child)

    
    parentId = {i[0] for i in Tag.objects.values_list('parent_id')}
    childTags = Tag.objects.exclude(id__in = parentId)

    notes = Note.objects.all().order_by('-id')
    tags = allTags()
    
    context = { 'notes': notes, 'tags':tags, 'childTags': childTags}

    return render(request, 'base/home.html', context)


@csrf_exempt
def save_category(request):
    print(request.POST)
    #{'catName': ['a'], 'catId': ['5']}>
    if request.method == 'POST':
        tagName = request.POST['tagName']

        parentId = request.POST['tagId']
        if parentId == '0':
            parentId = None

        tag = Tag(tag_name=tagName, parent_id=parentId)
        tag.save()

         
        parentId = {i[0] for i in Tag.objects.values_list('parent_id')}
        childTags = list(Tag.objects.exclude(id__in = parentId).values())

    htmltag = allTags()

    return JsonResponse({'status': 1, 'htmltag':htmltag, 'childTags': childTags })


@csrf_exempt
def save_note(request):


    if request.method == 'POST':
        title = request.POST['title']
        subject = request.POST['subject']
        leaf_tag_id = request.POST.getlist('checkBox[]') 

        leaf_tag_id = Tag.objects.filter(id__in = leaf_tag_id)
        Note.objects.create(note_title = title, note_subject = subject).leaf_tag.add(* leaf_tag_id)
        notes = list(Note.objects.values())


    return JsonResponse({'status':1, 'notes':notes})

