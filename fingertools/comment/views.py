# Create your views here.
from fingertools.comment.models import Comment
from django.shortcuts import render_to_response
from fingertools.base.models import FTObject

def get_comment(request, obj_id):
    commentsAux = Comment.objects.all()
    comments = []
    
    for comment in commentsAux:
        if comment.object.id == obj_id:
            comments.append(comment)
    
    return render_to_response('comment/comment.html', {'comments': comments})