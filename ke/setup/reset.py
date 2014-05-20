# -*- coding:utf-8 -*-

# config settings
import sys
import os
print "Configuring"

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir,os.path.pardir))
sys.path.append(PROJECT_ROOT)
os.environ['DJANGO_SETTINGS_MODULE'] = 'ke.settings'

print "Done Configuring"


from ke.photo.models import Photo
from django.core.files import File
from ke.photo.classes import StoryViewPhotoView
from django.core.files.storage import default_storage
from django.core.management import call_command
from django.contrib.auth.models import User
from django.db import connection
cursor = connection.cursor()

print "Database recreate"

cursor.execute("DROP DATABASE IF EXISTS %s;" % connection.settings_dict['NAME'])
cursor.execute("CREATE DATABASE %s CHARACTER SET utf8 COLLATE utf8_general_ci;" % connection.settings_dict['NAME'])
from django import db
db.close_connection()

print "Done Database recreate"


# remove tables = truncate + syncdb
print "Sync"
call_command('syncdb',interactive=False)
print "Done Sync"

print "create superuser"
admin = User(username='aynadin',email="brox2319@gmail.com",first_name="Айнадин" , last_name="Камалов")
admin.set_password('user123')
admin.is_superuser = True
admin.is_staff = True
admin.save()
print "done create superuser"

#remove photos
print "Removing photos"

for file in default_storage.listdir('photo')[1]:
    default_storage.delete('photo/%s' % file )

print "Done Removing photos"

# add photos
print "Adding photos"

SETUP_PATH = os.path.join(PROJECT_ROOT,'ke','setup')
for filename in os.listdir(os.path.join(SETUP_PATH,'photo')):
    filePath = os.path.join(os.path.join(SETUP_PATH,'photo'),filename)
    p = Photo(photo=File(open(filePath)), photoViews=[StoryViewPhotoView()])
    p.save()

print "Done Adding photos"

#add fixtures
print "load fixtures"

call_command('loaddata',os.path.join(SETUP_PATH,'fixtures.json'), interactive=True)

print "Done load fixtures"


print "Finished!"