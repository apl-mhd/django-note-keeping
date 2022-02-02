from django.shortcuts import render

from . models import Tag


def home(request):

    tags = Tag.objects.values()

    context = {
        'tags':list(tags),
    }

    return render(request, 'base/home.html', context)