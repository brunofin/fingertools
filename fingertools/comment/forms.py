# -*- coding: utf-8 -*-

from captcha.fields import ReCaptchaField
import datetime
from django.conf import settings
from django.contrib.comments.forms import CommentForm
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import force_unicode

from fingertools.comment.models import FTComment


class FTCommentForm(CommentForm):
    captcha = ReCaptchaField(required=True)
    
    def get_comment_model(self):
        return FTComment
    
    def get_comment_create_data(self):
        # Use the data of the superclass, and remove extra fields
        return dict(
            content_type = ContentType.objects.get_for_model(self.target_object),
            object_pk    = force_unicode(self.target_object._get_pk_val()),
            comment      = self.cleaned_data["comment"],
            submit_date  = datetime.datetime.now(),
            site_id      = settings.SITE_ID,
            is_public    = True,
            is_removed   = False,
            upvotes      = 0,
            downvotes    = 0,
        )
    
FTCommentForm.base_fields.pop('url')
FTCommentForm.base_fields.pop('email')
FTCommentForm.base_fields.pop('name')