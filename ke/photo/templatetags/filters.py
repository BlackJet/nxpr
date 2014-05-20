# -*- coding: utf-8 -*-
from django import template
import ke
register = template.Library()
@register.filter
def photo_filter(photo,className):
    cls = getattr(ke.photo.classes,className)
    return cls().get(photo.photo)

