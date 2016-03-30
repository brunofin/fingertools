# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

from fingertools.auth.forms import FormUser
from fingertools.auth.models import UserProfile
from fingertools.auth.profile import create_user_profile
from fingertools.img.models import Image
from fingertools.text.models import Texto


def tos(request):
	return render(request, 'tos.html')

def register(request):
	if request.method == 'POST':
		form = FormUser(request.POST)
		if form.is_valid():
			usr = form.save(commit=False)
			usr.is_staff = False
			usr.is_active = True
			usr.is_superuser = False
			#usr.set_password(form.data['password'])
			usr.save()
			return render(request, "usr/successful.html", {'usr': usr})
		else:
			return render(request, "usr/register.html", {'form': form})
			
	else:
		form = FormUser()
		return render(request, "usr/register.html", {'form': form})

@login_required
def uploads(request):
	return render(request, 'usr/uploads.html')

@login_required
def get_my_images(request):
	imagens = Image.objects.filter(user = request.user)
	
	return render(request, 'usr/my_images.html', {'imagens': imagens})

@login_required
def get_my_texts(request):
	textos = Texto.objects.filter(user = request.user)
	
	return render(request, 'usr/my_texts.html', {'textos': textos})
	
		
@login_required
def changePassword(request):
	form = PasswordChangeForm(request.user)
	
	return render(request, "usr/changePassword.html", {'form': form})

def profile(request, user_id):
	user = User.objects.get(id = user_id)
	try:
		profile = UserProfile.objects.get(user = user)
	except:
		profile = create_user_profile(user)
	
	return render(request, 'usr/profile.html', {'profile': profile})

def my_profile(request):
	return profile(request, request.user.id)

@sensitive_post_parameters()
@csrf_protect
@login_required
def password_change(request,
                    template_name='registration/password_change_form.html',
                    post_change_redirect=None,
                    password_change_form=PasswordChangeForm,
                    current_app=None, extra_context=None):
	if post_change_redirect is None:
		post_change_redirect = reverse('django.contrib.auth.views.password_change_done')
	if request.method == "POST":
		form = password_change_form(user=request.user, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(post_change_redirect)
	else:
		form = password_change_form(user=request.user)
	try:
		profile = UserProfile.objects.get(user = request.user)
	except:
		profile = create_user_profile(request.user)
	context = {
			'form': form,
			'profile': profile
	}
	if extra_context is not None:
		context.update(extra_context)
	
	
	return TemplateResponse(request, template_name, context,
                            current_app=current_app)
