from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm, PostForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import Post


@login_required(login_url='login')
def home(request):
    posts = Post.objects.all()

    return render(request, 'home.html', {'posts':posts})


@login_required(login_url='login')
def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('home')

@login_required(login_url='login')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form':form})


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=True)
            login(request,user)
            return redirect('home')
    else:
        form = RegisterForm()
    

    return render(request, 'registration/sign_up.html', {'form':form})

from django.core.mail import send_mail
from django.conf import settings

def index(request):
    if request.method=='POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(
            'contacto desde la web', # subject
            message, # message
            settings.EMAIL_HOST_USER, # from email
            [email], # to email
            fail_silently=False
        )
    return render(request, 'index.html')




