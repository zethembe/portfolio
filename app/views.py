from django.shortcuts import render
from . import forms
from django.http import HttpResponse,HttpResponseRedirect
from app.models import Post
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
# Create your views here.
def blog(request):

      model_view = Post.objects.all()
      
      return render(request,'app/blog.html',{'model_view':model_view})

def profile(request):
    return render(request,'app/profile.html')

def about(request):
    return render(request,'app/about.html')

def post(request):
    if request.method == 'GET':
        form = forms.PostForm()
    
        return render(request,'app/post.html', {'form':form})

    elif request.method == 'POST':
        form = forms.PostForm(request.POST)
        form.save(commit=True)
        return HttpResponse('Posted')

def home(request):
  
    return render(request,'app/home.html')

def signup(request):
    if request.method == 'GET':
        sign = forms.Signup()
        return render(request,'app/signup.html',{'form':sign})

    elif request.method =='POST':

        sign = forms.Signup(request.POST)
        if sign.is_valid():

            f = sign.save()
            f.set_password(f.password)
            f.save()
            return HttpResponse('You have succefully signed up!')
        else:
            return HttpResponse('Invalid')


def login_page(request):
    if request.method == 'GET':
        return render(request,'app/login.html')

    elif request.method == 'POST':

        name_username = request.POST.get('name_username')
        name_password = request.POST.get('name_userpassword')

        fix = authenticate(username = name_username, password=name_password)
        print(fix)

        if fix is not None:
            if fix.is_active:
                login(request,fix)
                return HttpResponse('hello')
                
            return HttpResponse('hi')
            

        else:
            return HttpResponse('not fix')
        