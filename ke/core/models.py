from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver
from ke.photo.models import Photo


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    bd = models.DateField(null = True)
    status = models.TextField(null=True)
    city = models.TextField(null = True, blank = True)
    gender = models.NullBooleanField(null = True)
    icq = models.TextField(null = True, blank = True)
    skype = models.TextField(null = True, blank = True)
    mobileTel = models.TextField(null = True, blank = True)

    credo = models.TextField(null = True, blank = True)
    force = models.TextField(null = True, blank = True)

    favFilms = models.TextField(null = True, blank = True)
    favMusic = models.TextField(null = True, blank = True)

    avatar = models.ForeignKey(to=Photo,null=True,blank=True)

    class Meta:
        app_label = 'core'
#User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

@receiver(post_save, sender=User)
def create_userprofile(sender, instance, created, **kwargs):
    if created: 
        profile, new = UserProfile.objects.get_or_create(user=instance)

class Attachment(models.Model):
    TYPE_CHOICES = (
        (1,"photo"),
        (2,"photolink"),
        (3,"videolink"),
    )

    photo = models.ForeignKey(to=Photo,null=True,blank=True)
    type = models.PositiveIntegerField(choices=TYPE_CHOICES)
    url = models.TextField()

    title = models.TextField()

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    # Story or Comment
    item = generic.GenericForeignKey()



class Comment(models.Model):
    user = models.ForeignKey(User)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    # Story  or Sale or Question or Supply
    item = generic.GenericForeignKey()


class Story(models.Model):
    user = models.ForeignKey(User)
    title = models.TextField(max_length=140)
    description = models.TextField(max_length=280,blank=True,null=True)
    text = models.TextField(blank=True,null=True)
    thumb = models.ForeignKey(Photo,null=True)
    date = models.DateTimeField(auto_now_add=True)
    attachments = generic.GenericRelation(Attachment)
    comments = generic.GenericRelation(Comment)

#    rates = generic.GenericRelation(Rate)
    class Meta:
        ordering = ['-date']

class Rate(models.Model):
    user = models.ForeignKey(User)
    value = models.IntegerField()
    story = models.ForeignKey(Story)

class CommentRate(models.Model):
    user = models.ForeignKey(User)
    value = models.IntegerField()
    comment = models.ForeignKey(Comment)



