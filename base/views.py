from cgi import print_directory
from itertools import chain
from traceback import print_tb
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F


from . models import Tag
from . models import Note

def allTags():

    htmltag = '<ul>'

    def recur(id, x): 
        child = Tag.objects.filter(parent_id = id )
        if(len(child) != 0):
            x += '<ul>'
            for j in child:
                id = str(j.id)
                x += '<li> <a class="tagclick" id="'+id +'" href="#">'+ j.tag_name + '</a>'
                x = recur(j.id, x)
            
            x +='</ul>'
        x += '</li>'
        return x

    categories = Tag.objects.filter(parent_id = None)
    
   # print(categories)

    for cat in categories:
        id = str(cat.id)
        htmltag += '<li> <a class="tagclick" id="'+id +'"  href="#">'+ cat.tag_name + '</a>'
        htmltag = recur(cat.id, htmltag)

    htmltag += '</ul>'
    return htmltag


def home(request):



#    SELECT * FROM child WHERE id not IN (SELECT parent_id FROM child);

    #query = """SELECT * FROM base_tag WHERE id not in SELECT parent_id FROM base_tag"""

    #employee_query = Employee.objects.filter(company='Private').only('id').all()
    #Person.objects.value('name', 'age').filter(id__in=employee_query)
    a = Tag.objects.all()
    b = Tag.objects.exclude(id__in = a)
   # print(b)
    c = Tag.objects.all()
    d = Tag.objects.exclude(parent_id__in = c)
    print(d)


    # table1.objects.exclude(id__in=
    # table2.objects.filter(your_condition).values_list('id', flat=True))


    #a = Tag.objects.exclude(parent_id__in = Tag.objects.all().values_list('id', flat=True))
    #print(a)

    notes = Note.objects.all()
    tags = allTags()
    childTags = list(Tag.objects.values())
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

    htmltag = allTags()


    return JsonResponse({'status': 1, 'htmltag':htmltag})


@csrf_exempt
def save_note(request):


    if request.method == 'POST':
        title = request.POST['title']
        subject = request.POST['subject']
        note_tag = request.POST.get('checkBox')
        print(note_tag)
        note = Note(note_title = title, note_subject = subject, note_tag = note_tag)
        note.save()
        notes = list(Note.objects.values())
    return JsonResponse({'status':1, 'notes':notes})

