# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django import forms
from django.core import validators
from ke.core.models import Story, Photo

class UserRegForm(forms.Form):
    username = forms.CharField(max_length=8, min_length=2, error_messages={'invalid': u'Длина ника от 2 до 8 букв'})
    password = forms.CharField()
    email = forms.EmailField(error_messages={'invalid': u'Мыло не правильно'})
    fn = forms.CharField(max_length=50, error_messages={'invalid': u'Имя неправильно написана'})
    ln = forms.CharField(max_length=50, error_messages={'invalid': u'Фамилия неправильно написана'})
    bd = forms.DateField(error_messages={'invalid': u'ДР неправильно написана'})

    def clean_username(self):
        name = self.cleaned_data['username']
        try:
            User.objects.get(username=name)
        except User.DoesNotExist:
            return name
        raise validators.ValidationError(u'Такой ник уже существует')

    def save(self, commit=True):
        username = self.cleaned_data["username"]
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]
        first_name = self.cleaned_data['fn']
        last_name=self.cleaned_data['ln']
        user = User(username=username,email=email,first_name= first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        #user.email_user(u"Активация аккаунта","Салам")
        #from django.core.mail import send_mail
        #send_mail('Subject here', 'Here is the message.', 'from@example.com',['brox2319@gmail.com'], fail_silently=False)

        profile = user.get_profile()
        profile.bd = self.cleaned_data['bd']
        profile.save()
        return user

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        exclude=('user','thumb')

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('photo',)

    def save(self,commit=True):

        from django.core.files.uploadedfile import InMemoryUploadedFile
        from PIL import Image
        from StringIO import StringIO

        view = self.files['photo']
        f = StringIO(view.read())
        thumb = StringIO()
        newImage = Image.open(f)
        if newImage.mode != "RGB":
            newImage = newImage.convert("RGB")
        newImage.thumbnail((800, 600), Image.ANTIALIAS)
        newImage.save(thumb, 'JPEG')

        resultFile = InMemoryUploadedFile(thumb, view.field_name, view.name, view.content_type, thumb.len, view.charset)
        self.instance.view = resultFile
        self.instance.save()


