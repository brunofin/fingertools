# -*- coding: utf-8 -*-

import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from fingertools.TagUtils import findOrCreateMultipleTags
from fingertools.base.models import Referer
from fingertools.text.forms import FormTexto
from fingertools.text.models import Texto


def upload(request):
	if request.method == 'POST':
		form = FormTexto(request.POST)
		if form.is_valid():
			txt = form.save(commit=False)
			txt.uploader_ip = request.META.get('HTTP_X_FORWARDED_FOR', '') or request.META.get('REMOTE_ADDR')
			now = datetime.datetime.now()
			txt.date = now.strftime("%Y-%m-%d")
			txt.time = now.strftime("%H:%M")
			txt.views = 0
			if request.user.is_authenticated():
				txt.user = request.user
			else:
				txt.user = None
			txt.save()
			
			tags = findOrCreateMultipleTags(form.data['tags'])
			for tag in tags:
				txt.tags.add(tag)
				
			return show_detail(request, txt.id)
		else:
			errors = form.errors
			form = FormTexto()
			return render(request, "txt/upload.html", {'errors': errors, 'form': form})
			
			
	else: # página acessada via link (GET)
		# Exibe o formulário em branco
		form = FormTexto()
	
		textos = Texto.objects.all().order_by('-id')[:10]
		return render(request, "txt/upload.html", {'form': form, 'textos': textos})

def show_detail(request, txt_id):
	txt = get_object_or_404(Texto, pk=txt_id)
	txt.views += 1
	txt.save()
	
	try:
		referer = Referer()
		referer.referer_url = request.META['HTTP_REFERER']
		referer.object = txt
		referer.save()
	except KeyError:
		pass
	
	return render(request, "txt/show_detail.html", {'txt': txt})
	
@login_required		
def show_my_codes(request):
	txts = Texto.objects.filter(user=request.user)
	return render(request, "txt/my_codes.html", {'txts': txts})
	
@login_required
def remove_code(request, txt_id):
	txt = Texto.objects.get(id=txt_id)
	return render(request, "txt/confirm_delete.html", {'txt':txt})
	
@login_required
def remove_code_y(request, txt_id):
	txt = get_object_or_404(Texto, pk=txt_id)
	if txt.user == request.user: # low security check
		txt.delete()
	return redirect('/v/my_codes')
