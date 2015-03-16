__author__ = 'tom'

from django.contrib import admin
from core.models import Post, Project

admin.site.register(Post)
admin.site.register(Project)