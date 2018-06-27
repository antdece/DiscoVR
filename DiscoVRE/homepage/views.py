from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import PostForm

def index(request):
	posts = Post.objects.order_by('-date_added')

	context = {'posts' : posts}

	return render(request, 'homepage/index.html', context)

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)

		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('index')
	else:
		form = UserCreationForm()
	form = UserCreationForm()
	context = {'form' : form}
	return render(request, 'registration/register.html', context)

@login_required
def logout(request):
	

@login_required
def post(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)

		if form.is_valid():
			print('valid form')
			post = form.save(commit=False)
			post.username = request.user
			print(post.username.username)
			post.save()
			return redirect('index')

	else:
		form = PostForm()

	form = PostForm()

	context = {'form' : form}

	return render(request, 'homepage/post.html', context)
