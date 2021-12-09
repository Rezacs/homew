from django.http import response 
from django.http.response import HttpResponse, HttpResponseNotFound
from django.contrib.auth.models import User

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render

from datetime import datetime
from post.models import *
from commentandlike.models import *
from grups.models import *
from django.views.generic import TemplateView,ListView,DetailView
from django.views import View

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from post.forms import *
from django.urls import reverse
from django.contrib.auth import authenticate , login , logout

from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from post.serializers import *

def class_today_time (request) :
    return HttpResponse(f'today is : {datetime.today()}')

def class_detail_post ( request ,post_id ) :
    # print(post_id)
    title = 'maktab sharif'
    desc = 'desc'
    try :
        post = Post.objects.get(id = post_id)
        body =f'<html><body><h1>{title}</h1><p>{post.title}</p></body></html>'
    except Post.DoesNotExist :
        body = 'yaaft nashod arbaab'
        return HttpResponseNotFound(body)
    return HttpResponse(body)

def class_first_template ( request ) :
    today = datetime.today()
    title = 'maktab'
    post = Post.objects.get(id = 2)
    contex = {'today' : today , 'maktab' : title , 'post' : post}
    return render(request , 'maktab.html', contex)

def class_post_slug_view ( request , given_slug ) :
    post = Post.published.get(slug = given_slug)
    if post.writer != request.user and post.status == 'DRF' :
        return HttpResponse('you dont have permission to do this !')
    user = request.user
    likes = Post_Likes.objects.filter(post = post )
    if user.is_authenticated :
        customer = Customer.objects.get(user_name =user.username)
        check = Post_Likes.objects.filter(post = post).filter(writer = user)

    else :
        customer = Customer.objects.get(user_name ='Anonymous')
    form = CommentModelForm()
    form2 = LikePostForm()
    form3 = LikeCommentForm()
    comments = Post_Comments.objects.filter(post = post.id)
    if request.method == "POST" :
        form = CommentModelForm(request.POST) # validate
        form2 = LikePostForm(request.POST)
        if form.is_valid() :
            print(form.cleaned_data)
            comment = form.save(commit=False)
            comment.post = post
            comment.customer = customer
            comment.writer= user
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'comment was saved !')

        if form2.is_valid() :
            if check :
                check.delete()
            else :
                like = form2.save(commit=False)
                like.writer = user
                like.post = post
                like.save()

        if form3.is_valid() :
                comment_like = form3.save(commit=False)
                comment_like.writer = user
                comment_like.comments = request.POST['comment.id']
                comment_like.save()


    return render(request , 'class_post_detail.html', {
        'post' : post ,
        'comments' : comments ,
        'form' : form,
        'user' : user ,
        'likes' : likes ,
        'form2' : form2 ,
        'check' : check ,
        'form3' : form3
    })

    
def class_post_detail ( request , post_id ) :
    post = Post.objects.get(id = post_id)
    if post.writer != request.user and post.status == 'DRF' :
        return HttpResponse('you dont have permission to do this !')
    user = request.user
    likes = Post_Likes.objects.filter(post__id = post_id )
    if user.is_authenticated :
        customer = Customer.objects.get(user_name =user.username)
        check = Post_Likes.objects.filter(post = post).filter(writer = user)
    else :
        customer = Customer.objects.get(user_name ='Anonymous')
        check = False
    form = CommentModelForm()
    form2 = LikePostForm()
    form3 = LikeCommentForm()
    comments = Post_Comments.objects.filter(post = post.id)
    if request.method == "POST" :
        form = CommentModelForm(request.POST) # validate
        form2 = LikePostForm(request.POST)
        if form.is_valid() :
            print(form.cleaned_data)
            comment = form.save(commit=False)
            comment.post = post
            comment.customer = customer
            comment.writer= user
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'comment was saved !')

        if form2.is_valid() :
            if check :
                check.delete()
            else :
                like = form2.save(commit=False)
                like.writer = user
                like.post = post
                like.save()

        if form3.is_valid() :
                comment_like = form3.save(commit=False)
                comment_like.writer = user
                comment_like.comments = request.POST['comment.id']
                comment_like.save()

                
    return render(request , 'class_post_detail.html', {
        'post' : post ,
        'comments' : comments ,
        'form' : form,
        'user' : user ,
        'likes' : likes ,
        'form2' : form2 ,
        'check' : check ,
        'form3' : form3
    })

#

def add_comment ( request , comment_id ) :
    comment = get_object_or_404(Post_Comments , id =comment_id )
    post = comment.post
    user = request.user
    customer = Customer.objects.get(user_name =user.username)
    form = CommentModelForm()
    if request.method == "POST" :
        form = CommentModelForm(request.POST)
        if form.is_valid() :
            comment = form.save(commit=False)
            comment.post = post
            comment.customer = customer
            comment.writer= user
            comment.parent = Post_Comments.objects.get(id = comment_id)
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'comment was saved !')
            return redirect(f'/class_post_detail/{post.id}')

    return render ( request , 'forms/add_comment.html' , {'form' : form , 'post' : post} )

#

def class_post_list ( request ) :
    posts = Post.published.all()
    return render ( request , 'class_post_list.html' , {'posts' :posts })

def class_category_detail ( request , category_id ) :
    category = Category.objects.get(id = category_id)
    return render(request , 'class_category_detail.html', {'category' : category})

def class_category_list ( request ) :
    categorys = Category.objects.all()
    return render ( request , 'category_list.html' , {'categorys' :categorys }) #category_list

def class_category_posts ( request , category_name ) :
    posts = Post.objects.filter(category__name__contains=f'{category_name}')
    return render(request , 'class_category_posts.html', {'posts' : posts})

class PostDetailView(DetailView):
    model = Post
    # This file should exist somewhere to render your page
    template_name = 'gslug.html'
    # Should match the value after ':' from url <slug:the_slug>
    # slug_url_kwarg = 'the_slug'
    # Should match the name of the slug field on the model 
    # slug_field = 'slug' # DetailView's default value: optional
    context_object_name = 'post'


class ModelListView(ListView):
    model = Post
    template_name = ".html"

# class PostDetailView(DetailView):
#     #more  https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-display/  
#     model= Post


@api_view(['GET'])
def post_list_2(request):

    posts = Post.objects.all()

    serializer = PostListSerializer(posts , many = True)

    return Response(data = serializer.data , status=200)

# PostSerializer

@api_view(['GET'])
def post_detail_2(request , input_id):

    post = Post.objects.get(id = input_id)

    serializer = PostSerializer(post)

    return Response(data = serializer.data , status=200)

#HW17

@api_view(['GET'])
def post_comments_list_2(request):

    comments = Post_Comments.objects.all()

    serializer = PostCommentListSerializer(comments , many = True)

    return Response(data = serializer.data , status=200)

@api_view(['GET'])
def post_comments_detail_2(request , comment_id):

    comments = Post_Comments.objects.filter(id = comment_id).all()

    serializer = PostCommentListSerializer(comments , many = True)

    return Response(data = serializer.data , status=200)

@api_view(['GET'])
def post_comments_list_3(request , post_id):

    comments = Post_Comments.objects.filter( post__id=post_id)

    serializer = PostCommentListSerializer(comments , many = True)

    return Response(data = serializer.data , status=200)

#CW 16 azar 


@api_view(['GET'])
def customer_list (request):

    customers = Customer.objects.all()

    serializer = AccountSerializer(customers , many = True)

    return Response(data = serializer.data , status=200)

@api_view(['GET'])
def customer_detailed (request , username):

    customers = Customer.objects.get(user_name=username)

    serializer = AccountSerializer(customers )

    return Response(data = serializer.data , status=200)

def CW_ajax (request) :
    return render (request , 'forms/CW20.html', {'variable': 'world'})

#HW18


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([])
def post_detail_update_delete(request, id):

    post = get_object_or_404(Post, id=id)

    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(data=serializer.data, status=200)

    elif request.method == 'PUT':
        if post.writer != request.user:
            return Response(data={'msg': 'this post owned by another user'}, status=400)

        serializer = PostUpdateSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_post = serializer.save()
        resp_serializer = PostSerializer(updated_post)
        return Response(resp_serializer.data, status=200)

    elif request.method == 'DELETE':
        if post.writer != request.user:
            return Response(data={'msg': 'this post owned by another user'}, status=400)
        post.delete()

        return Response(status=204)

# form


def get_name(request) :
    form = Simple_form()
    if request.method == "POST" :
        form = Simple_form(request.POST)
        print(request.POST)
        if form.is_valid() :
            print(form.cleaned_data)
            print('form is valid')
        else :
            print('form is invalid')
    return render (request , "forms/name_form2.html" , {'form' : form})

# @login_required(login_url='login-mk')
def add_tag_form ( request ) :
    # form = TagForm(request.POST or None )
    form = TagModelForm(request.POST or None )
    print(request.user)
    if form.is_valid() :
        print(form.cleaned_data)
        # tag = Tag.objects.create(name = form.cleaned_data['name'])
        form.save()
        messages.add_message(request, messages.INFO, 'new tag saved !')
        return redirect(reverse('tag-list')) #app_name : url name
    return render(request,'forms/tag_form.html' ,{
        'form' : form
    })

class AddTagView ( View ) :
    form = TagModelForm
    def get (self , request , *args , **kwargs) :
        return render(request,'forms/tag_form.html' ,{'form' : self.form})
    def post (self , request , *args , **kwargs) :
        post_form = self.form(request.POST)
        messages.add_message(request, messages.SUCCESS, 'new tag saved !')
        return redirect(reverse('tag-list'))



# balaye in chera nemishe login gozasht ??
class TagListView ( ListView ) :
    model = Tag
    #context_object_name = 'publisher'
    #queryset = Tag.objects.all()
    template_name = "tag_list.html"

    def get_context_data(self , **kwargs) :
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context

    def get_queryset(self):
        #return super().get_queryset()
        return Tag.objects.all()

@login_required(login_url='login-mk')
def edit_tag_form ( request , tag_id ) :
    tag = get_object_or_404(Tag , id =tag_id )
    # print(request.user)
    # print(request.user.email)
    form = TagModelForm(instance=tag)
    if request.method == "POST" :
        form = TagModelForm(request.POST , instance=tag) # validate
        if form.is_valid() :
            print(form.cleaned_data)
            form.save()
            return redirect(reverse('tag-list')) #app_name : url name
    return render ( request , 'forms/edit_tag_form.html',{'form' : form , 'tag':tag })

def delete_tag_form(request , tag_id) :
    tag = get_object_or_404(Tag , id =tag_id )
    form = TagDeleteModelForm(instance=tag)
    if request.method == "POST" :
        tag.delete()
        print('delete')
        return redirect(reverse('tag-list'))
    return render ( request , 'forms/delete_tag_form.html',{'form' : form , 'tag' : tag})

def login_maktab ( request ) :
    form = LoginForm()
    if request.method == "POST" :
        form = LoginForm(request.POST)
        if form.is_valid() :
            # cleaned data
            user = authenticate(username=form.cleaned_data.get('username'),password=form.cleaned_data.get('password'))
            if user is not None :
                login(request,user)
                q = request.GET.get('next')
                if q :
                    return redirect(reverse(f'{q}'))
                messages.add_message(request, messages.SUCCESS , 'loged in !')
                return redirect(reverse('dashboard'))

    return render (request , 'forms/login.html' , {'form' : form})

def register_maktab(request) :
    form = UserRegisterFormModel(None or request.POST)
    if request.method == "POST" :
        if form.is_valid() :
            user = User.objects.create_user(form.cleaned_data['username'],form.cleaned_data['email'],form.cleaned_data['password'])
            customer = Customer.objects.create(user_name=form.cleaned_data.get('username'))
            user = authenticate(username=form.cleaned_data.get('username'),password=form.cleaned_data.get('password'))
            if user is not None :
                login(request,user)
            # user.save()
            # print('new user is :' , user)
            # message = {'text':"salam daaawsh !" , 'class_css' : 'text-primary'}
            # return HttpResponse('user register !')
            messages.add_message(request, messages.INFO , 'user created and logged in !')
            return redirect(reverse('dashboard'))

    return render (request , 'forms/register.html' , {'form' : form })


@login_required(login_url='login-mk')
def set_new_password ( request ) :
    form = SetNewPasswordForm()
    user = request.user
    if request.method == "POST" :
        form = SetNewPasswordForm(request.POST)
        if form.is_valid() :
            print(user.check_password(form.cleaned_data.get('password')))
            if user.check_password(form.cleaned_data.get('password')) :
                user.set_password(form.cleaned_data.get('password1'))
                user.save()
                messages.add_message(request, messages.INFO , 'new password was set !')
            print(request.user)
    return render (request , 'forms/set_new_password.html' , {'form' : form , 'user' : user})

# mini poroje

@login_required(login_url='login-mk')
def dashboard ( request ) :
    user = request.user
    posts = Post.published.filter(writer = user)
    customer = Customer.objects.get(user_name=user.username)
    return render ( request , 'forms/dashboard.html' , {'posts' :posts , 'user' : user , 'customer' : customer })

@login_required(login_url='login-mk')
def add_new_post (request) :
    form = AddPostForm(None or request.POST , request.FILES)
    if request.method == "POST" :
        if form.is_valid() :

            # print(form.cleaned_data)
            # form.writer = request.user
            # form.save()

            bad_post = form.save(commit=False)
            bad_post.writer = request.user
            bad_post.customer = Customer.objects.get(user_name=request.user.username)
            form.save()
            
            # user.save()
            # print('new user is :' , user)
            # message = {'text':"salam daaawsh !" , 'class_css' : 'text-primary'}
            # return HttpResponse('post created !')

            # print(form.cleaned_data)
            # # form.save()
            # print(form.cleaned_data)
            # bad_post = form.save()
            # tags = form.cleaned_data.get('tag')
            # bad_post.tag.set(tags)
            # #
            # bad_post.title = form.cleaned_data['title'],
            # bad_post.body = form.cleaned_data['body']
            # bad_post.shortdesc = form.cleaned_data['shortdesc']
            # bad_post.customer = form.cleaned_data['customer']
            # bad_post.writer = request.user
            # bad_post.image = form.cleaned_data['image']
            # categorys = form.cleaned_data.get('category')
            # bad_post.category.set(categorys)
            # bad_post.location_lat = form.cleaned_data['location_lat']
            # bad_post.location_lng = form.cleaned_data['location_lng']
            # bad_post.status = form.cleaned_data['status']
            # #
            # bad_post.save()

            messages.add_message(request, messages.INFO , 'new post was saved !')
            return redirect(reverse('dashboard'))

    return render (request , 'forms/new_post.html' , {'form' : form })


@login_required(login_url='login-mk')
def add_category_form ( request ) :
    # form = TagForm(request.POST or None )
    form = CategoryModelForm(request.POST or None )
    print(request.user)
    if form.is_valid() :
        print(form.cleaned_data)
        # tag = Tag.objects.create(name = form.cleaned_data['name'])
        form.save()
        messages.add_message(request, messages.SUCCESS , 'new category was saved !')
        return redirect('/class_category_list') #app_name : url name
    return render(request,'poroje/add_category.html' ,{
        'form' : form
    })


@login_required(login_url='login-mk')
def edit_category_form ( request , category_id ) :
    category = get_object_or_404(Category , id =category_id )
    # print(request.user)
    # print(request.user.email)
    form = CategoryModelForm(instance=category)
    if request.method == "POST" :
        form = CategoryModelForm(request.POST , instance=category) # validate
        if form.is_valid() :
            form.save()
            messages.add_message(request, messages.SUCCESS , 'category was edited !')
            #messages.add_message(request, messages.SUCCESS , 'category was edited !' , extra_tag="danger")
            return redirect(reverse('category-list')) #app_name : url name
    return render ( request , 'poroje/edit_category.html',{'form' : form , 'category' : category})


@login_required(login_url='login-mk')
def delete_category_form(request , category_id) :
    category = get_object_or_404(Category , id =category_id )
    form = CategoryModelForm(instance=category)
    if request.method == "POST" :
        category.delete()
        messages.add_message(request, messages.WARNING, 'category was deleted !')
        return redirect(reverse('category-list'))
    return render ( request , 'poroje/delete_category.html',{'form' : form , 'category' : category})

@login_required(login_url='login-mk')
def user_logout(request) :
    user = request.user
    # form = LogoutModelForm(instance=user)
    if request.method == "POST" :
        logout(request)
        return redirect(reverse('dashboard'))
    return render ( request , 'poroje/logout.html',{ 'user' : user})


@login_required(login_url='login-mk')
def edit_post ( request , post_id ) :
    specified_post = get_object_or_404(Post , id =post_id )
    form = AddPostForm(instance=specified_post)
    if request.method == "POST" :
        if request.user == specified_post.writer :
            form = AddPostForm(request.POST , request.FILES , instance=specified_post)
            if form.is_valid() :
                # print(form)
                form.save()
                messages.add_message(request, messages.SUCCESS, 'post was edited !')
                return redirect(reverse('dashboard'))
        else :
            return HttpResponse('you dont have permission to do this !')
    return render ( request , 'poroje/edit_post.html',{'form' : form , 'specified_post' : specified_post})

@login_required(login_url='login-mk')
def delete_post(request , post_id) :
    post = get_object_or_404(Post , id =post_id )
    form = AddPostForm(instance=post)
    if request.method == "POST" :
        if request.user == post.writer :
            post.delete()
            messages.add_message(request, messages.INFO , 'post was deleted !')
            return redirect(reverse('dashboard'))
        else :
            return HttpResponse('you dont have permission to do this !')
    return render ( request , 'poroje/delete_post.html',{'form' : form , 'post' : post})


def user_list ( request ) :
    users = User.objects.all()
    return render ( request , 'poroje/user_list.html' , {'users' :users }) 

def user_page (request , username ) :
    if username == 'None' :
        next = request.GET.get('next')
        if next : 
            return redirect(request.GET.get('next'))
        else :
            return HttpResponse('old data - no such page !')
            # messages.add_message(request, messages.SUCCESS, 'old data - no such page !')
            # return redirect(request.GET.get('next'))
    else :
        user = User.objects.get(username=username)
        # user = get_object_or_404(User, id=news_pk)
        posts = Post.published.filter(writer = user)
        customer = Customer.objects.get(user_name=username)
            #messages.add_message(request, messages.SUCCESS, 'old data - no such page !')
        return render ( request , 'poroje/page_view.html' , {'posts' :posts , 'pointed_user' : user , 'customer' : customer })


def search_post_title ( request ) :
    if ( request.method == 'POST') :
        input = request.POST['word']
        posts = Post.published.filter(title__contains=input)
        return render ( request , 'poroje/search_title.html' , {'posts' :posts })

def search_username ( request ) :
    if ( request.method == 'POST') :
        input = request.POST['word']
        users = User.objects.filter(username__contains=input)
        return render ( request , 'poroje/search_username.html' , {'users' :users })

def delete_comment(request,comment_id):
    
    comment = get_object_or_404(Post_Comments,id=comment_id)
    if request.user == comment.writer :    
        comment.delete()
        post = comment.post
        messages.add_message(request, messages.SUCCESS, 'comment was deleted !')
        return redirect(f'/class_post_detail/{post.id}')
    else :
        return HttpResponse('you dont have permission to do this !')
    # return redirect(reverse('delete-comment') , kwargs={'comment_id' : comment.id}) 
    #reverse('app_name:name_url')

def edit_comment ( request , comment_id ) :
    comment = get_object_or_404(Post_Comments , id =comment_id )
    post = comment.post
    # print(request.user)
    # print(request.user.email)
    form = CommentModelForm(instance=comment)
    if request.method == "POST" :
        if request.user == comment.writer : 
            form = CommentModelForm(request.POST , instance=comment)
            if form.is_valid() :
                form.save()
                messages.add_message(request, messages.SUCCESS , 'commment was edited !')
                return redirect(f'/class_post_detail/{post.id}')
        else :
            return HttpResponse('you dont have permission to do this !')
    return render ( request , 'forms/edit_comment.html',{'form' : form , 'comment' : comment , 'post' : post})

def search_post_body (request) :
    if ( request.method == 'POST') :
        input = request.POST['word']
        posts = Post.published.filter(body__contains=input)
        return render ( request , 'poroje/search_title.html' , {'posts' :posts })

@login_required(login_url='login-mk')
def edit_personal_info ( request ) :
    customer = get_object_or_404(Customer , user_name =request.user.username )
    form = CustomerEditForm(instance=customer)
    user = User.objects.get(username =request.user.username)
    if request.method == "POST" :
        form = CustomerEditForm(request.POST , request.FILES , instance=customer)
        if form.is_valid() :
            form.save()
            messages.add_message(request, messages.SUCCESS , 'profile was edited !')
            return redirect(reverse('dashboard'))
    return render ( request , 'poroje/edit_personal_info.html',{'form' : form , 'customer':customer ,'user':user })

def search_trash (request) :
    keyword = request.GET.get("keyword")
    if keyword :
        posts = Post.objects.filter(title__contains = keyword )
        return render (request , "poroje/search_title.html" , {'posts' :posts } ) 
    posts = Post.objects.all()
    return render (request , "poroje/search_title.html" , {'posts' :posts } )

class searchPageView(ListView):
    # model = Post
    template_name = "poroje/search_title.html"
    context_object_name = 'posts'
    def get_queryset(self):
        queryset = Post.objects.all()

        # q = self.request.GET.get('q')
        # if q :
        #     queryset = Post.objects.filter(title__contains=q)

        return queryset

@login_required(login_url='login-mk')
def drafted_posts ( request ) :
    user = request.user
    posts = Post.drafted.filter(writer = user)
    customer = Customer.objects.get(user_name=user.username)
    return render ( request , 'forms/drafted_posts.html' , {'posts' :posts , 'user' : user , 'customer' : customer })

def contact_us (request) :
    # print('post : ' ,request.POST)
    # print('get : ' ,request.GET)
    # print(request.POST['email'])
    if ( request.method == 'POST') :
        if  request.POST['email'] :
            if  request.POST['subject'] :
                if  request.POST['message'] :
                    send_mail(
                        f"{request.POST['subject']}",
                        f"{request.POST['message']} - email:{request.POST['email']}",
                        "atccereza@gmail.com",
                        ['ralmassizx@gmail.com'],
                        fail_silently=False,
                    )
                    messages.add_message(request, messages.SUCCESS , 'thank for your feedback !')
                    return render ( request , "poroje/simple_form.html" , {})
        messages.add_message(request, messages.WARNING , 'please fill all of the inputs !')
    return render ( request , "poroje/simple_form.html" , {})

def login_mobile (request) :
    form = MobileLoginForm()
    if request.method == "POST" :
        form = MobileLoginForm(request.POST)
        if form.is_valid() :
            customer = Customer.objects.get(phone = form.cleaned_data.get('mobile') )
            user_name = customer.user_name
            user = authenticate(username=user_name,password=form.cleaned_data.get('password'))
            if user is not None :
                login(request,user)
                messages.add_message(request, messages.SUCCESS , 'logged in successfuly')
                return redirect(reverse('dashboard'))
        messages.add_message(request, messages.WARNING , 'wrong phone or password !')

    return render (request , 'poroje/login_mobile.html' , {'form' : form})

    # if ( request.method == 'POST') :
    #     if  request.POST['mobile'] :
    #         if type(request.POST['mobile']) != str :
    #             messages.add_message(request, messages.WARNING , 'wrong entry')
    #             return render (request , 'poroje/login_mobile.html' , {})
    #         if  request.POST['password'] :
    #             customer = Customer.objects.get(phone = request.POST['mobile'] )
    #             user_name = customer.user_name
    #             print('user_name :' + user_name)
    #             user = authenticate(username=user_name,password=request.POST['password'])
    #             if user is not None :
    #                 login(request,user)
    #                 return redirect(reverse('dashboard'))

    # return render (request , 'poroje/login_mobile.html' , {})

def login_email (request) :
    form = EmailLoginForm()
    if request.method == "POST" :
        form = EmailLoginForm(request.POST)
        if form.is_valid() :
            bad_user = User.objects.get(email = form.cleaned_data.get('email') )
            user_name = bad_user.username
            user = authenticate(username=user_name,password=form.cleaned_data.get('password'))
            if user is not None :
                login(request,user)
                messages.add_message(request, messages.SUCCESS , 'logged in successfuly')
                return redirect(reverse('dashboard'))
        messages.add_message(request, messages.WARNING , 'wrong phone or password !')

    return render (request , 'poroje/login_email.html' , {'form' : form})

@login_required(login_url='login-mk')
def edit_personal_info_user ( request ) :
    specified_user = get_object_or_404(User , username =request.user.username )
    form = UserEditFormModel(instance=specified_user)
    print('username' , request.user.username)
    if request.method == "POST" :
        form = UserEditFormModel(request.POST , instance=specified_user)
        if form.is_valid() :
            form.save()
            messages.add_message(request, messages.SUCCESS , 'profile was edited !')
            return redirect(reverse('dashboard'))
    return render ( request , 'poroje/edit_personal_info_user.html',{'form' : form , 'user':specified_user })

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('login-mk')

@login_required(login_url='login-mk')
def send_message ( request , username ) :
    reciever_user = get_object_or_404(User , username=username )
    user = request.user
    form = SendMessageForm()
    if request.method == "POST" :
        form = SendMessageForm(request.POST)
        if form.is_valid() :
            message = form.save(commit=False)
            message.writer= user
            message.reciever = reciever_user
            message.save()

            messages.add_message(request, messages.SUCCESS, 'message sent !')
            return redirect(f'/user/{reciever_user.username}')

    return render ( request , 'poroje/send_message.html' , {'form' : form , 'reciever_user' : reciever_user} )

@login_required(login_url='login-mk')
def inbox (request ) :

        user = User.objects.get(username=request.user.username)
        messages = SendMessage.objects.filter(reciever = user)

        return render ( request , 'poroje/inbox.html' , {'pointed_user' : user , 'posts' : messages })

@login_required(login_url='login-mk')
def delete_message(request,message_id):
    
    message = get_object_or_404(SendMessage ,id=message_id)
    if request.user == message.reciever :    
        message.delete()
        messages.add_message(request, messages.SUCCESS, 'message was deleted !')
        return redirect('/post_urls/inbox')
    else :
        return HttpResponse('you dont have permission to do this !')

@login_required(login_url='login-mk')
def follow(request,username):
    
    target_user = get_object_or_404(User ,username=username)    
    UserConnections.objects.create(following=request.user , follower=target_user)
    messages.add_message(request, messages.SUCCESS, 'user was followed !')
    return redirect('/post_urls/inbox')




        
