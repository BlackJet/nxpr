# -*- coding:utf-8 -*-
from django.http import Http404
from django.contrib.auth.models import User
import django
from django.shortcuts import render
from ke.core.forms import UserRegForm
from django.contrib.auth import authenticate
import logging
from ke.core.utils import render_to_json, view
from ke.photo.models import Photo
from ke.photo.classes import AvatarThumbPhotoView, StoryViewPhotoView, PhotoPreviewPhotoView, AvatarViewPhotoView
from django.utils.html import escape
logger = logging.getLogger(__name__)

@view(url=r'^$')
def index(request): return render(request,'index.html')

@view(url=r'^register/$')
def register(request): return render(request,'index.html')

@view(url=r'^register.html/$')
def register_htlm(request): return render(request,'register.html')

@view(url=r'^profile/$')
def profile(request): return index(request)

@view(url=r'^profile.html/$')
def profile_page(request): return render(request,'profile.html')

@view(url=r'^profile_edit/$')
def profile_edit(request): return index(request)

@view(url=r'^profile_edit.html/$')
def profile_edit_page(request): return render(request,'profile_edit.html')

def add(request):
    form = UserRegForm(request.POST)
    if form.is_valid():
        form.save()
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None: django.contrib.auth.login(request, user)
        return dict(success=True)
    return dict(success=False, errors=[(k, v[0].encode('utf-8')) for k, v in form.errors.items()])

@render_to_json
def upload_photo(request):
    photo = Photo(photo=request.FILES['photo'],
        photoViews=[AvatarThumbPhotoView(), StoryViewPhotoView(), PhotoPreviewPhotoView()])
    photo.save()
    return dict(success=True)


@render_to_json
def login(request):
    if request.user.is_authenticated():
        return {
            'success': True,
            'user': {'username': 'logged'}
        }
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            django.contrib.auth.login(request, user)
            return {
                'success': True,
                'user': {'username': user.username}
            }
        else:
            return {
                'success': False,
                'error': {'message': 'user_disabled'}
            }
    else:
        return {
            'success': False,
            'error': {'message': 'user_notexists'}
        }

@render_to_json
def logout(request):
    if request.user.is_authenticated(): django.contrib.auth.logout(request)
    return{
        'success':True
    }

@render_to_json
def set_status(request):
    profile = request.user.get_profile()
    profile.status = escape(request.POST['status'])
    profile.save()
    return{
        'success':True
    }

@render_to_json
def set_profile(request):

    profile = request.user.get_profile()
    profile.city = escape(request.POST['city'])
    profile.skype = escape(request.POST['skype'])
    profile.icq = escape(request.POST['icq'])
    profile.mobileTel = escape(request.POST['mobileTel'])
    profile.credo = escape(request.POST['credo'])
    profile.force = escape(request.POST['force'])
    profile.favFilms = escape(request.POST['favFilms'])
    profile.favMusic = escape(request.POST['favMusic'])
    gender = escape(request.POST['gender'])

    if gender == '0':
        profile.gender=False
    elif gender == '1':
        profile.gender=True
    elif gender == 'null':
        profile.gender = None

    profile.save()
    return {'success':True}

@render_to_json
def set_avatar(request):
    photo = Photo(photo=request.FILES['photo'],
        photoViews=[AvatarViewPhotoView(), AvatarThumbPhotoView()])
    photo.save()
    profile = request.user.get_profile()
    profile.avatar = photo
    profile.save()
    return dict(success=True)

@view(url=r'^sell/$')
def sellx(request): return render(request,'index.html')

@view(url=r'^sell.html/$')
def sell(request): return render(request,'sell.html')
