from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import User, Post
from django.contrib.auth import authenticate, login, logout
from .forms import RegisForm, PostForm

# # Create your views here.
def home (request):
    header = 'Home'
    context = {'header' : header}
    return render(request, 'app/home.html', context)

def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)  # Perbaiki menjadi email=email
        except User.DoesNotExist:
            messages.error(request, 'email tidak valid')
            return render(request, 'app/login_register.html', {'page': page})

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'password anda tidak valid')

    context = {'page': page}
    return render(request, 'app/login_register.html', context)

def registerPage(request):
    form = RegisForm()
    context = {'form' : form}

    if request.method == 'POST':
        form = RegisForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            for field in form.errors:
                for error in form.errors[field]:
                    messages.error(request, f"{error.capitalize()}")
    return render(request, 'app/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def userProfile(request):
    return render(request, 'app/profile.html')

@login_required(login_url='login')
def temanBelajar(request):
    header = 'Teman Belajar'
    user_post = Post.objects.filter(user=request.user) 
    all_post = Post.objects.all()
    context = {'header': header,
               'user_post' : user_post,
               'all_post' : all_post,}
    return render(request, 'app/teman_belajar.html', context)

@login_required(login_url='login')
def createPost (request):
    form = PostForm()
    if request.method == 'POST':
        Post.objects.create(
            user = request.user,
            message = request.POST.get('message'),
        )
        return redirect('teman-belajar')

    context = {'form' : form}
    return render(request, 'app/post_form.html', context)