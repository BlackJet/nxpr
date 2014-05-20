# -*- coding:utf-8 -*-
from ke.core.utils import view
from ke.core.views import user_view, story_view
from ke.core.utils import render_to_json, view
@view(url=r'^api/profile/add/$')
@render_to_json
def add_profile(request): return user_view.add(request)

@view(url=r'^api/login/$')
def login(request): return user_view.login(request)

@view(url=r'^api/logout/$')
def logout(request): return user_view.logout(request)

@view(url=r'^api/profile/upload_photo/$')
def upload_photo(request): return user_view.upload_photo(request)

@view(url=r'^api/profile/status/$')
def set_profile_status(request): return user_view.set_status(request)

@view(url=r'^api/profile/$')
def set_profile(request): return user_view.set_profile(request)

@view(url=r'^api/profile/set_avatar/$')
def set_profile_avatar(request): return user_view.set_avatar(request)

@view(url=r'^api/story/add/$')
def add_story(request): return story_view.add(request)

@view(url=r'^api/story/(\d+)/vote/$')
def vote_story(request,id): return story_view.vote(request,id)


