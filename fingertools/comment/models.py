from django.contrib.comments.models import Comment
from django.db import models

class FTComment(Comment):
    upvotes = models.PositiveSmallIntegerField()
    downvotes = models.PositiveSmallIntegerField()
