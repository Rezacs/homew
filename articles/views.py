from django.http.response import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from .models import Article
from django.shortcuts import render
from post.models import *
from grups.models import *
from articles.forms import *
from django.http import HttpResponseRedirect

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

def postDetail ( request , id ) :
    post = Post.objects.get(id = id)
    return render ( request , 'detail.html' , {'post' : post})

def postList ( request ) :
    posts = Post.objects.all()
    categorys = Category.objects.all()
    return render ( request , 'list.html' , {'posts' : posts , 'categorys' : categorys})

class ShowTemplate (TemplateView):
    template_name = 'theme.html'

# class MainPageView (TemplateView) :
#     template_name = 'index.html'

class MainPageView (ListView) :
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'

class PostDetailView (DetailView ) :
    model = Post
    template_name = 'detail.html'

def simple_form (request) :
    print(request)
    print(request.method)
    print('post : ' ,request.POST)
    print('get : ' ,request.GET)
    # print(request.POST['email'])
    message = ''
    if ( request.method == 'POST') :
        # if ( request.POST['search']) :
        #     filter_posts = Post.objects.filter(title_contains = request.POST['search'] )
        if ( request.POST['email'] == 'maktab') :
            message = {'text':"salam maktab !" , 'class_css' : 'text-danger'}
        else :
            message = {'text':"salam daaawsh !" , 'class_css' : 'text-primary'}
        # Category.objects.create(title = request.POST['email'])
    return render ( request , "simple_form.html" , {'message' : message})

def get_name(request) :
    if request.method == "POST" :
        form = NameForm(request.POST)
        if form.is_valid() :
            return HttpResponseRedirect("/thanks/")
    else :
        form = NameForm()
        return render (request , "name.html" , {"form" : form })



from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# start form :

def get_name_2(request):
    
    form = SimpleForm()

    if request.method == "POST":

        form = SimpleForm(request.POST)
        if form.is_valid():
            print(form)
            print(form.cleaned_data)
            print('name',form.cleaned_data['name'])
            # newtag = Tag()
            # newtag.title =  form.cleaned_data['name']
            form.save()
        # else :
        #     print(form.cleaned_data)
            # 
    return render(request,'forms/name_form.html',{
        'form':form
    })

