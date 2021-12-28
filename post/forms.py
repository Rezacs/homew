from django import forms
from django.core.exceptions import ValidationError
from django.db.models import fields
from grups.models import *
from post.models import *
from commentandlike.models import *
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Simple_form(forms.Form):
    name = forms.CharField(max_length=255 , label='first_name' , help_text='esmeto bezan' )
    name1 = forms.CharField(max_length=255, label='last_name')
    # name2 = forms.CharField(max_length=255, label='user_name')
    # name3 = forms.CharField(max_length=255, label='first_name', disabled='True')
    # phone = forms.IntegerField()
    # text = forms.CharField(label='nazaraat' , widget=forms.Textarea)
    # password = forms.CharField(widget=forms.PasswordInput)
    # choices = forms.ChoiceField(label='alaki' , choices=((1 , 'one') , (2 , 'two')))
    # description = forms.CharField(widget=forms.Textarea)
    # tags = forms.ModelChoiceField(label='model choices',queryset=Tag.objects.all() )
    # multi_tags = forms.ModelMultipleChoiceField(label='model choices',queryset=Tag.objects.all())

class TagForm(forms.Form ) :
    name = forms.CharField(max_length=255 , label='tag' , help_text='esme tago bezan', error_messages={'required' : 'vared kardane tag elzamist!'})
    desc = forms.CharField(label='nazaraat' , widget=forms.Textarea)

    # def save(self):
    #     print(self.cleaned_data)
    #     Tag.objects.create(name = self.cleaned_data['name'] , desc = self.cleaned_data['desc'] )
        

class TagModelForm (forms.ModelForm ) :

    class Meta :
        model = Tag
        fields = "__all__"  # ['name']

class TagDeleteModelForm (forms.ModelForm) :
    class Meta :
        model = Tag
        fields = "__all__"


# python manage.py makemessages -l fa

class CommentModelForm ( forms.ModelForm ) :
    class Meta :
        model = Post_Comments
        fields = ['title' , 'body']
        labels = {
            'title' : 'onvaan',
            'body' : 'tozihat',
        }
        error_messages = {
            'title' : {
                'max_length' : _('this writer name is too long '),
                'required' : _('this field is required required !'),
            },
        }
        help_texts = {
            'title' : _('esme titleto bezaaan ! '),
        }

class SendMessageForm( forms.ModelForm) :
    class Meta :
        model = SendMessage
        fields = ['title' , 'body']
        labels = {
            'title' : 'onvaan e message',
            'body' : 'tozihat e message',
        }

class LoginForm( forms.Form ) :
    username = forms.CharField(max_length=255 , label='username' )
    password = forms.CharField(widget=forms.PasswordInput)

class MobileLoginForm( forms.Form ) :
    mobile = forms.IntegerField( )
    password = forms.CharField(widget=forms.PasswordInput)

class EmailLoginForm( forms.Form ) :
    email = forms.EmailField( )
    password = forms.CharField(widget=forms.PasswordInput)

class EditUsername( forms.Form ) :
    new_username = forms.CharField( )

class UserRegisterFormModel (forms.ModelForm ) :
    class Meta :
        model = User
        fields = ['username' , 'email' , 'password']

class UserEditFormModel (forms.ModelForm ) :
    class Meta :
        model = User
        fields = ['username' , 'email' ]
        
class SetNewPasswordForm (forms.Form ):
    password = forms.CharField(widget=forms.PasswordInput , label='old password')
    password1 = forms.CharField(widget=forms.PasswordInput , label='new password')
    password2 = forms.CharField(widget=forms.PasswordInput , label='new password repeat')

    # def clean_password2(self) :
    #     password2 = self.cleaned_data['password2']
    #     password1 = self.cleaned_data['password1']
    #     if password1 != password2 :
    #         raise ValidationError("password e reapet ba asli yeki nis ")
    #     return password1

    def clean(self) :
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2 :
            raise ValidationError("password e reapet ba asli yeki nis ")


class SetNewUsernameForm (forms.Form ):
    new_username = forms.CharField()

    def clean(self) :
        cleaned_data = super().clean()

        if User.objects.filter(username=self.new_username ) :
            raise ValidationError("this username isnt available ")


class AddPostForm (forms.ModelForm) :
    class Meta :
        model = Post
        exclude = ['writer' , 'customer']

    # def save(self):
    #     print(self.cleaned_data)
    #     Post.objects.create(title = self.cleaned_data['title'],
    #                         body = self.cleaned_data['body'],
    #                         shortdesc = self.cleaned_data['shortdesc'],
    #                         customer = self.cleaned_data['customer'],
    #                         writer = self.cleaned_data['writer'],
    #                         image = self.cleaned_data['image'],
    #                         category = self.cleaned_data['category'],
    #                         location_lat = self.cleaned_data['location_lat'],
    #                         location_lng = self.cleaned_data['location_lng'],
    #                         status = self.cleaned_data['status'],
    #                         )

        # instance = Setupuser.objects.create(organization=org)

        # instance.emails_for_help.set(users)

        # tag.set(self.cleaned_data['tag'])

        # tags = form.cleaned_data.get('tag')
        # emails = form.cleaned_data.get("share_email_with")

        # users = User.objects.filter(email__in=emails)
        # instance = Setupuser.objects.create(organization=org)

        # instance.emails_for_help.set(users)

class CategoryModelForm (forms.ModelForm ) :

    class Meta :
        model = Category
        fields = "__all__"  # ['name']

# class LogoutModelForm (forms.ModelForm) :
#     class Meta :
#         model = User
#         fields = "__all__"

class LikePostForm (forms.ModelForm) :
    class Meta :
        model = Post_Likes
        fields = []

class LikeCommentForm (forms.ModelForm) :
    class Meta :
        model = Post_Comment_likes
        fields = []

class CustomerEditForm (forms.ModelForm) :
    class Meta :
        model = Customer
        exclude = ['user_name' , 'email']

class AddressForm (forms.ModelForm) :
    class Meta :
        model = Address
        exclude = ['customer']

