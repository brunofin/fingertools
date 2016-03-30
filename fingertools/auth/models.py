from django.contrib.auth.models import User
from django.db import models

from fingertools.comment.models import FTComment
from fingertools.img.models import Image
from fingertools.text.models import Texto


class UserProfile(models.Model):
    __DEFAULT_PROFILE_PICTURE_PATH = 'img/profile_pictures/default.jpg'
    
    user = models.ForeignKey(User, unique = True)
    url = models.URLField("Website", blank = True)
    picture = models.ImageField(upload_to = 'img/profile_pictures/%Y%m%d')
    premium = models.BooleanField()
    
    def get_shown_name(self):
        if not self.user.get_full_name():
            return self.user.userrname
        else:
            return self.user.get_full_name()
    
    def get_profile_picture(self):
        if self.picture:
            return self.picture
        else:
            return self.__DEFAULT_PROFILE_PICTURE_PATH
    
    def get_images(self):
        return Image.objects.filter(user=self.user)
    
    def get_images_count(self):
        return self.get_images().count()
    
    def get_texts(self):
        return Texto.objects.filter(user = self.user)
    
    def get_texts_count(self):
        return self.get_texts().count()
    
    def get_posts(self):
        return FTComment.objects.filter(user = self.user)
    
    def get_posts_count(self):
        return FTComment.objects.filter(user = self.user).count()
        