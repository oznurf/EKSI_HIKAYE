from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .models import Story
from hikaye.forms import MyUserCreationForm, StoryForm


def index(request):
    if 'title' in request.GET:
        objects = Story.objects.filter(
            title__icontains=request.GET['title'])
    else:
        objects = Story.objects.all()
    return render(request, 'index.html',
                  {'objects': objects})


def stories_detailview(request, story_id):
    if request.method == 'POST':
        yeni_veriler = request.POST.copy()
        yeni_veriler['parent'] = story_id
        yeni_veriler['writer'] = request.user.id

        form = StoryForm(yeni_veriler)
        if form.is_valid():
            form.save()
    elif request.method == 'GET':
        form = StoryForm()
    return render(request, 'stories_detail.html',
                  {
                      'object': Story.objects.get(pk=story_id),
                      'form': form
                  })



def register_user(request):
    form = MyUserCreationForm()

    if request.method == "POST":
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    return render(request, 'register.html', {
        "form": form
    })


def login_user(request):
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')

    return render(request, 'login.html', {
        "form": form
    })


def logout_user(request):
    logout(request)
    return redirect('/')
