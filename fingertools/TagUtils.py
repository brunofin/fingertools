from fingertools.base.models import Tag
from django.core.exceptions import ObjectDoesNotExist

def findOrCreateTag(tagname):
    tag = None
    try:
        tag = Tag.objects.get(tag=tagname)
        return tag
    except ObjectDoesNotExist:
        tag = Tag()
        tag.tag = tagname
        tag.save()
        return tag
    
def findOrCreateMultipleTags(taglist=''):
    tags = []
    taglistStr = taglist.split(';')
    for tag in taglistStr:
        tag = tag.strip()
        tags.append(findOrCreateTag(tag))
    return tags