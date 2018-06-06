from django.shortcuts import render
from . import forms
from django.http import HttpResponse
from app.models import Post


# Create your views here.
def blog(request):


    model_view = Post.objects.all()
    return render(request,'app/blog.html',{'model_view':model_view})



def about(request):
    return render(request,'app/about.html')

def post(request):
    if request.method == 'GET':
        form = forms.PostForm()
    
        return render(request,'app/post.html', {'form':form})

    elif request.method == 'POST':

        form = forms.PostForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        
            return render(request,'app/blog.html')

def home(request):
  
    return render(request,'app/home.html')



