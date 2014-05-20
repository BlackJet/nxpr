# -*- coding:utf-8 -*-

"""
Работа со story
"""
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models.aggregates import Sum, Count
from django.http import Http404

from django.shortcuts import render_to_response, render
from django.template.context import RequestContext
from ke.core.forms import StoryForm
import logging
from ke.core.models import Attachment, Story, Rate, Comment
from ke.core.utils import render_to_json, view
from ke.core.views import user_view
from ke.photo.classes import StoryViewPhotoView, StoryThumbPhotoView
from ke.photo.models import Photo

logger = logging.getLogger(__name__)
PAGE_SIZE = 20

@view(url=r'^story/$')
def story(request): return user_view.index(request)

@view(url=r'^story_add/$')
def story_add(request): return user_view.index(request)

@view(url=r'^story.html/$')
def story_page(request):
    """
   Вернет посты
    """
    page = int(request.GET.get('page',0))
    clientTotal = int(request.GET.get('total',0))

    total = Story.objects.count()
    if not page: page,clientTotal = 1,total
    lastPageNo = clientTotal//PAGE_SIZE
    tail = clientTotal % PAGE_SIZE
    skip = total - clientTotal # allways 0 for the first
    offset = skip + (page-1)*PAGE_SIZE # allways 0 the first
    limit = offset + PAGE_SIZE
    # last page
    if page > lastPageNo:
        if (page - lastPageNo) == 1 and tail: limit = offset + tail
        else: raise Http404

    stories = Story.objects.all()[offset:limit].annotate(rating=Sum('rate__value'))
    rates = {rate.story.id:rate.value for rate in Rate.objects.filter(story__id__in=[s.id for s in stories],user=request.user)}
    for story in stories:
        story.rateValue = rates.get(story.id,0)


    if request.GET.has_key('page') : return render(request,'template/story_block.html',dict(stories = stories))
    return render(request,'template/story.html',dict(stories = stories,total = total))

@view(url=r'^story/(\d+)/attachments.html/$')
def story_attachments(request,id):
    return render(request,'template/story_attachments.html',dict(story = Story.objects.get(id=id)))

@view(url=r'^template/([a-z0-9_\.]+)/$')
def template(request,template):
    return render(request,'template/%s' % template)

@render_to_json
def add(request):
    # сначала сохраняем стори, потом уже привяки
    form = StoryForm(request.POST)
    if form.is_valid():
        story = form.save(commit=False)
        story.user = request.user
        thumb = request.FILES.get('thumb',None)
        if thumb:
            photo = Photo(photo=thumb, photoViews=[StoryThumbPhotoView()])
            photo.save()
            story.thumb = photo
        story.save()

        attachedPhotoFiles = [(fieldName,file) for fieldName,file in request.FILES.iteritems() if 'photoFile' in fieldName]
        for fieldName, file in attachedPhotoFiles:
            photo = Photo(photo=file, photoViews=[StoryViewPhotoView()])
            photo.save()
            a = Attachment(photo=photo, type=1, item=story)
            a.save()
        return {'success': True}
    return {
        'success': False,
        'errors': [(k, v[0].encode('utf-8')) for k, v in form.errors.items()]
    }

@render_to_json
@login_required
def vote(request,storyId):
    story = Story.objects.get(id=storyId)
    value = int(request.POST['value'])
    if value != -1 and value != 1: return {'success':False}
    query = Rate.objects.filter(user=request.user,story=story)
    if not query:
        userRate = Rate(story=story,user=request.user,value=value)
    else:
        userRate = query[0]
        if userRate.value > 0 and value == 1 or userRate.value < 0 and value == -1: return {'success':False}
        userRate.value += value
    userRate.save()
    return {'success':True}

@view(url=r'^story/(\d+)/add_comment/$')
@render_to_json
@login_required
def story_set_comments(request,id):
    text = request.POST['text'].replace('\n','<br>')
    comment = Comment(text=text,user = request.user,item = Story.objects.get(id=id))
    comment.save()
    rendered = render_to_string('template/story_comment.html',dict(comment=comment),context_instance=RequestContext(request))
    return dict(success=True,data=rendered)


@view(url=r'^story/(\d+)/comments/$')
@render_to_json
def get_story_comment(request,id):
    comments = Story.objects.get(id=id).comments.all()
    data = [{'id':comment.id} for comment in comments]
    dict(success =True,data=data)


@view(url=r'^story/(\d+).html')
def story_html(request,id):

    return render(request,'template/story_view.html',dict(story=Story.objects.get(id=id)))