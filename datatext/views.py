from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render

from datatext import models as m

def textes(request):
    # List the texts from the database.
    textes = m.Texte.objects.all()
    template = loader.get_template('datatext/textes.html')
    context = Context({
        'page':'textes',
        'textes': textes,
        })
    return HttpResponse(template.render(context))

def categories(request):
    # List the categories from the database.
    categories = m.Categorie.objects.all()
    template = loader.get_template('datatext/categories.html')
    context = Context({
        'page':'categories',
        'categories': categories,
        })
    return HttpResponse(template.render(context))

def texte(request, texte_id):
    # Convert the data from database directly to hml.
    texte = m.Texte.objects.filter(id=texte_id)
    copies = m.Copie.objects.filter(id_texte=texte_id)
    sections = m.Section.objects.filter(id_texte=texte_id)
    template = loader.get_template('datatext/texte.html')
    context = Context({
        'page':'texte',
        'texte': texte,
        'copies': copies,
        'sections': sections,
        })
    return HttpResponse(template.render(context))
    
def textei(request, texte_id):
    # Convert the data from database to xml.
    
    texte = m.Texte.objects.filter(id=texte_id)
    copies = m.Copie.objects.filter(id_texte=texte_id)
    sections = m.Section.objects.filter(texte_id=texte_id)
    template = loader.get_template('datatext/textei.xml')
    context = Context({
        'page':'texte',
        'texte': texte,
        'copies': copies,
        'sections': sections,
        })
    return HttpResponse(template.render(context), content_type="application/xhtml+xml")

def _textei(request, texte_id):
    # Convert the data from database to xml, show it on a navigator.
    
    texte = m.Texte.objects.filter(id=texte_id)
    copies = m.Copie.objects.filter(id_texte=texte_id)
    sections = m.Section.objects.filter(texte_id=texte_id)
    template = loader.get_template('datatext/textei.xml')
    context = Context({
        'page':'texte',
        'texte': texte,
        'copies': copies,
        'sections': sections,
        })
    return template.render(context)

def texteihtml(request, texte_id):
    # Convert the data from database to xml.

    from lxml import etree
  
    xml = _textei(request,texte_id)
    root = etree.fromstring(xml)
    titre = root[0][0][0][0][0].text
    persName = root[0][0][0][1][0]
    body = root[1][1][0]

    template = loader.get_template('datatext/texte2.html')
    context = Context({
        'page':'texte',
        'titre': titre,
        'auteur': persName,
        'body': body,
        })
    return HttpResponse(template.render(context))