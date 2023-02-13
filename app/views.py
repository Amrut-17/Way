from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import PostForm
from .models import Post


def homepage(request):
    posts = Post.objects.all()
    return render(request, 'app/homepage.html', {'posts':posts})


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                message = "Username already exist. Please create another"
                return render(request, 'app/signup.html', {'message':message})

            elif User.objects.filter(email=email).exists():
                message = "Email already exist, please try with different mail id"
                return render(request, 'app/signup.html', {'message':message})

            else:
                user = User.objects.create_user(username=username, email=email, password=pass2)
                user.save()
                return redirect('signin')
        else:
            messages = 'Password do not match'
            return redirect('signup')
    
    return render(request, 'app/signup.html')



def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            message = "Please enter a correct username and password."
            return render(request, 'app/login.html', {'message': message})

    return render(request, 'app/login.html')

def signout(request):
    logout(request)
    return redirect('signin')


def addPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('homepage')
    else:
        form = PostForm()

    return render(request, 'app/addPost.html', {'form': form})


def postDetails(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    all_posts = Post.objects.all().exclude(pk=post_id)
    return render(request, 'app/postDetails.html', {'post':post, 'all_posts':all_posts})