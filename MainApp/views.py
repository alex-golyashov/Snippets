from django.http import Http404
from django.shortcuts import render, redirect
# from MainApp.models import items, count
from MainApp.models import Snippet
from django.db.models import Max

def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    context = {'pagename': 'Добавление нового сниппета'}
    return render(request, 'pages/add_snippet.html', context)

# Можно так: создать объекты в файле models

# def snippets_page(request):
#     context = {'snippets': items,
#                'count': count,
#                'pagename': 'Просмотр сниппетов'}
#     return render(request, 'pages/view_snippets.html', context)

def snippets_page(request):
    snippets = Snippet.objects.all()
    count = Snippet.objects.aggregate(id=Max('id'))
    context = {'pagename': 'Просмотр сниппетов', 'snippets': snippets, 'count': count}
    return render(request, 'pages/view_snippets.html', context)

def snippets_details_page(request, num):
    # snippets = Snippet.objects.all()
    # for snippet in snippets:
    #     if snippet.id == num:
    #         context = {'snippet': snippet}
    snippet = Snippet.objects.get(pk=num)
    context = {'snippet': snippet}
    return render(request, 'pages/snippet_details.html', context)