# -*- coding: utf-8 -*-

from django import template
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render_to_response
from django.utils.safestring import mark_safe

from fingertools.auth.models import UserProfile


register = template.Library()

MAX_ENTRIES = 10

class PostObject(object):
    pageurl = ''
    pagetitle = ''
    comment = ''
    submit_date = ''

@register.filter
def render_user_posts(user_id):
    user = User.objects.get(id = user_id)
    user_profile = UserProfile.objects.get(user = user)
    posts = user_profile.get_posts().order_by('submit_date')[:MAX_ENTRIES]
    data = []
    
    for post in posts:
        ct = ContentType.objects.get_for_id(post.content_type.id)
        ftobj = ct.get_object_for_this_type(pk=post.object_pk)
        
        obj = PostObject()
        obj.pageurl = ftobj.url()
        obj.pagetitle = ftobj.titulo
        obj.comment = post.comment
        obj.submit_date = post.submit_date
        
        data.append(obj)
    
    html = str(render_to_response('usr/profile/posts.html', {'data': data}))
    return mark_safe(html[40:])

@register.filter
def render_user_images(user_id):
    user = User.objects.get(id = user_id)
    user_profile = UserProfile.objects.get(user = user)
    images = user_profile.get_images().order_by('date')[:MAX_ENTRIES]
    
    html = str(render_to_response('usr/profile/images.html', {'images': images}))
    return mark_safe(html[40:])

@register.filter
def render_user_redirects(user_id):
    return ''

@register.filter
def render_user_texts(user_id):
    return ''
        
        