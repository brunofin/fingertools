from django.conf.urls import * #patterns, include, url
from django.http import HttpResponsePermanentRedirect

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',    
    (r'^$', 'img.views.index'),
    (r'^my_images/$', 'img.views.show_my_images'),
    (r'^v/(?P<img_id>\d+)/d$', 'img.views.show_detail'),
    (r'^v/(?P<img_id>\d+)/remove/yes$', 'img.views.remove_image_y'),
    (r'^v/(?P<img_id>\d+)/remove$', 'img.views.remove_image'),
    (r'^v/(?P<img_id>\d+)/$', 'img.views.show_direct'),
    (r'^code/$', 'text.views.upload'),
    (r'^my_codes/$', 'text.views.show_my_codes'),
    (r'^v/(?P<txt_id>\d+)/t$', 'text.views.show_detail'),
    (r'^v/(?P<txt_id>\d+)/t/remove/yes$', 'text.views.remove_code_y'),
    (r'^v/(?P<txt_id>\d+)/t/remove$', 'text.views.remove_code'),
    (r'^changePassword/$', 'auth.views.changePassword'),
    (r'^uploads/$', 'auth.views.uploads'),
    (r'^get_my_images$', 'auth.views.get_my_images'),
    (r'^get_my_texts$', 'auth.views.get_my_texts'),
    (r'^change_password/$', 'auth.views.password_change', {'template_name': 'usr/changePasswordTemplate.html', 'post_change_redirect': '/my_profile'}),
    (r'^signup/$', 'auth.views.register'),
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'usr/login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url': '/login/'}),
    (r'^tos$', 'auth.views.tos'),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^v/$', lambda request: HttpResponsePermanentRedirect('/')),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^profile/(?P<user_id>\d+)', 'auth.views.profile'),
    (r'^my_profile$', 'auth.views.my_profile'),
    (r'tag/(?P<tag_name>.*)', 'base.views.listByTag'),
    #(r'^comments/(?P<obj_id>\d+)', 'comment.views.get_comment'),
    #(r'^play$', 'play.views.index'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
