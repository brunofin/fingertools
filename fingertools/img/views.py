# -*- coding: utf-8 -*-

import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.comments.models import Comment
from django.shortcuts import render, get_object_or_404, redirect

from fingertools.TagUtils import findOrCreateMultipleTags
from fingertools.base.models import Referer
from fingertools.comment.forms import FTCommentForm
from fingertools.comment.models import FTComment
from forms import FormImage
from models import Image


def index(request):
	if request.method == 'POST':
		form = FormImage(request.POST, request.FILES)
		if form.is_valid():
					
			img = form.save(commit=False)
			
			img.uploader_ip = request.META.get('HTTP_X_FORWARDED_FOR', '') or request.META.get('REMOTE_ADDR')
			now = datetime.datetime.now()
			img.date = now.strftime("%Y-%m-%d")
			img.time = now.strftime("%H:%M")
			img.views = 0
			if request.user.is_authenticated():
				img.user = request.user
			else:
				img.user = None
			
			img.save()
			
			tags = findOrCreateMultipleTags(form.data['tags'])
			for tag in tags:
				img.tags.add(tag)
			
			return show_detail(request, img.id)
		else:
			errors = form.errors
			form = FormImage()
			lastUploads = Image.objects.all().order_by('-id')[:6]
			return render(request, "img/index.html", {'errors': errors, 'form': form, 'lastUploads': lastUploads})
			
	else: # página acessada via link (GET)
		# Exibe o formulário em branco
		form = FormImage()
		lastUploads = Image.objects.all().order_by('-id')[:6]
		return render(request, "img/index.html", {'form': form, 'lastUploads': lastUploads})

@login_required		
def show_my_images(request):
	imgs = Image.objects.filter(user=request.user)
	return render(request, "img/my_images.html", {'imgs': imgs})
	
@login_required
def remove_image(request, img_id):
	img = Image.objects.get(id=img_id)
	return render(request, "img/confirm_delete.html", {'img':img})
	
@login_required
def remove_image_y(request, img_id):
	img = get_object_or_404(Image, pk=img_id)
	if img.user == request.user: # low security check
		img.delete()
	return redirect('/v/my_images')
		
def show_direct(request, img_id):
	img = get_object_or_404(Image, pk=img_id)
	img.views += 1
	img.save()
	
	try:
		referer = Referer()
		referer.referer_url = request.META['HTTP_REFERER']
		referer.object = img
		referer.save()
	except KeyError:
		pass
	
	return render(request, "img/show_direct.html", {"img": img})
	
def show_detail(request, img_id):
	img = get_object_or_404(Image, pk=img_id)
	img.views += 1
	img.save()
	
	try:
		referer = Referer()
		referer.referer_url = request.META['HTTP_REFERER']
		referer.object = img
		referer.save()
	except KeyError:
		pass
	
	return render(request, "img/show_detail.html", {'img': img})
