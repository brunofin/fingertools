# Create your views here.
from django.shortcuts import render
from django.db import connection

from fingertools.base.models import Tag, FTObject
from fingertools.img.models import Image
from fingertools.text.models import Texto


def listByTag(request, tag_name):
    tagobj = Tag.objects.filter(tag = tag_name)
    mostTagged = getMostTaggedTags()
    
    if len(tagobj) == 0:
        return render(request, 'tags/list.html', {'query': tag_name, 'mostTagged': mostTagged})
    
    objects = Image.objects.all()
    listimg = []
    for ftobject in objects:
        for tagin in ftobject.tags.all():
            if tagin.tag == tagobj[0].tag:
                listimg.append(ftobject)
    
    objects = Texto.objects.all()
    listtxt = []
    for ftobject in objects:
        for tagin in ftobject.tags.all():
            if tagin.tag == tagobj[0].tag:
                listtxt.append(ftobject)
    
    
    
    return render(request, 'tags/list.html', {'query': tag_name, 'images': listimg, 'texts': listtxt, 'mostTagged': mostTagged})

def getMostTaggedTags():
    cursor = connection.cursor()
    cursor.execute('SELECT tag_id, COUNT(tag_id) AS NumberOfTimes FROM base_ftobject_tags GROUP BY tag_id ORDER BY tag_id ASC')
    rows = cursor.fetchall()[:10]
    tagMap = []
    
    for row in rows:
        tagMap.append((Tag.objects.get(id=row[0]), row[1]))
    
    return tagMap
    
    