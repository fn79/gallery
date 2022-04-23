from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from artist.models import Paint
from artist.forms import ArtistForm,SignupForm


def page_0(request):
    if request.method == 'POST' :
        form = ArtistForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    artist = Paint.objects.all()
    form = ArtistForm()
    user_form = SignupForm()

    context={
        'artist':artist,
        'form' : form,
        'user_form' : user_form
    }
    return render(request,'page_0.html',context)


@login_required

def retrieve(request,id):
    paint=Paint.objects.get(id=id)
    if request.method == "POST":
            form = ArtistForm(request.POST, request.FILES, instance=paint)
            if form.is_valid():
                form.save()
    else:
        form = ArtistForm(instance=paint)
        user = User.objects.get(username='admin')

    context={
        'paint': paint,
        'user' : user,
        'form' : form,
        'request_user' : request.user
        }
    return render(request,'retrieve.html',context)

def About(request):
    return render(request,'about.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            logout(request)
            return redirect('/')
            # Redirect to a success page.
    return render(request, 'login.html')