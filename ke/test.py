# -*- coding: utf-8 -*-
class Preview:
    bee = 1
    def get(self,photo):
        return photo + 'buzz'

def photo_filter(photo,className):
    cls = globals()[className]
    return cls().get(photo)

print photo_filter('sss','Preview')