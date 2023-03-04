from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib import auth
# from MainApp.models import items, count
from MainApp.models import Snippet
from django.db.models import Max
from MainApp.forms import SnippetForm, UserRegistrationForm
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.decorators import login_required


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)

# def add_snippet_page(request):
#     context = {'pagename': 'Добавление нового сниппета'}
#     return render(request, 'pages/add_snippet.html', context)

@login_required
def add_snippet_page(request):
    if request.method == "GET":
        form = SnippetForm()
        context = {'pagename': 'Добавление нового сниппета', 'snippet_form': form}
        return render(request, 'pages/add_snippet.html', context)
    elif request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.user = request.user
            snippet.save()
            return redirect("snippets-page")

# Можно так: создать объекты в файле models
# def snippets_page(request):
#     context = {'snippets': items,
#                'count': count,
#                'pagename': 'Просмотр сниппетов'}
#     return render(request, 'pages/view_snippets.html', context)

# CBV - Class Based Views (подход основанный на классах, а не на функциях обработки)

def snippets_page(request):
    snippets = Snippet.objects.all()
    count = Snippet.objects.aggregate(id=Max('id'))
    context = {'pagename': 'Просмотр сниппетов', 'snippets': snippets, 'count': count}
    return render(request, 'pages/view_snippets.html', context)

def snippets_page_mine(request):
    snippets_mine = Snippet.objects.filter(user=request.user)
    count = Snippet.objects.filter(user=request.user).count()
    context = {'pagename': 'Просмотр моих сниппетов', 'snippets_mine': snippets_mine, 'count': count}
    return render(request, 'pages/view_snippets_mine.html', context)

def snippets_details_page(request, num):
    # snippets = Snippet.objects.all()
    # for snippet in snippets:
    #     if snippet.id == num:
    #         context = {'snippet': snippet}
    snippet = Snippet.objects.get(pk=num)
    context = {'snippet': snippet}
    return render(request, 'pages/snippet_details.html', context)

# def create_snippet(request):
#     if request.method == "POST":
#         print("form data = ", request.POST)
#         form_data = request.POST
#         # del form_data["csrfmiddlewaretoken"]
#         # snippet = Snippet(**form_data)
#         snippet = Snippet(
#             name=form_data["name"],
#             lang=form_data["lang"],
#             code=form_data["code"]
#         )
#         snippet.save()
#         return redirect("snippets-page")

# def create_snippet(request):
#     if request.method == "POST":
#         form = SnippetForm(request.POST)
#         if form.is_valid():
#             form.save()
#     return redirect("snippets-page")


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print("username =", username) # выводит результат в консоли при запущенном сервере
        # print("password =", password)
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            context ={
                'pagename': 'PythonBin',
                'errors': ["username or password incorrect"]
            }
            return render(request, 'pages/index.html', context)
        return redirect("index-page")
    raise Http404


def logout_page(request):
    auth.logout(request)
    return redirect(request.META.get('HTTP_REFERER', '/'))

def registration_page(request):
    if request.method == "GET":
        form = UserRegistrationForm()
        context = {'pagename': 'Регистрация пользователя', 'registration_form': form}
        return render(request, 'pages/registration.html', context)
    elif request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index-page")
        else:
            context = {'pagename': 'Регистрация пользователя', 'registration_form': form}
            return render(request, 'pages/registration.html', context)