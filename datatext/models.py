#from __future__ import unicode_literals
from django.utils.translation import ugettext as _
from django.db import models
from datetime import datetime

class Auteur(models.Model):
    nom_ar = models.CharField(max_length=50)
    prenom_ar = models.CharField(max_length=100,null=True,blank=True)
    nom_trans = models.CharField(max_length=40,null=True,blank=True)
    prenom_trans = models.CharField(max_length=80,null=True,blank=True)
    naiss_date = models.CharField(max_length=10,null=True,blank=True)
    deces_date = models.CharField(max_length=10,null=True,blank=True)
    naiss_hej = models.CharField(max_length=10,null=True,blank=True)
    deces_hej = models.CharField(max_length=10,null=True,blank=True)
    naiss_lieu = models.CharField(max_length=20,null=True,blank=True)
    deces_lieu = models.CharField(max_length=20,null=True,blank=True)
    biographie = models.TextField(null=True,blank=True)
    pub_date = models.DateTimeField(default=datetime.now)
    
    class Meta:
        managed = True
        db_table = 'sara_auteurs'
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')
        
    def __str__(self):              # __unicode__ on Python 2
        return '%s %s' % (self.prenom_ar, self.nom_ar)
        
class Categorie(models.Model):
    intitule_ar = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    pub_date = models.DateTimeField(default=datetime.now)
    
    class Meta:
        managed = True
        db_table = 'sara_textes_categories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        
    def __str__(self):              # __unicode__ on Python 2
        return self.intitule_ar
        
class Texte(models.Model):
    LANGUES = (
            ('ar', 'العربيّة'),
            ('fr', 'français'),
        )
    CATALOGUES = (
            ('AWi', 'AWi'),
            ('AWii', 'AWii'),
            ('النّقشبندي', 'النّقشبندي'),
            ('Adler', 'Adler'),
        )
    lang = models.CharField(max_length=2,default='ar', choices=LANGUES)
    titre_ar = models.CharField(max_length=150)
    titre_trans = models.CharField(max_length=100,null=True,blank=True)
    commentaires = models.TextField(null=True,blank=True)
    id_auteur = models.ForeignKey(Auteur)
    catalogue1 = models.CharField(max_length=10,null=True,blank=True,choices=CATALOGUES)
    ref1 = models.CharField(max_length=10,null=True,blank=True)
    catalogue2 = models.CharField(max_length=10,null=True,blank=True,choices=CATALOGUES)
    ref2 = models.CharField(max_length=10,null=True,blank=True)
    id_categorie = models.ForeignKey(Categorie,null=True,blank=True)
    pub_date = models.DateTimeField(default=datetime.now)
    
    class Meta:
        managed = True
        db_table = 'sara_textes'
        verbose_name = _('Text')
        verbose_name_plural = _('Texts')
        
    def __str__(self):              # __unicode__ on Python 2
        return self.titre_ar
        
class Bibliographie(models.Model):
    id_texte = models.ForeignKey(Texte)
    zotero = models.CharField(max_length=50,null=True,blank=True)
    lang = models.CharField(max_length=10,null=True,blank=True)
    page = models.CharField(max_length=25,null=True,blank=True)
    pub_date = models.DateTimeField(default=datetime.now)
    
    class Meta:
        managed = True
        db_table = 'bibliographie'
        verbose_name = _('Bibliography')
        verbose_name_plural = _('Bibliographies')
        
    def __str__(self):              # __unicode__ on Python 2
        return self.id_texte    
    
class Bibliotheque(models.Model):
    nom = models.CharField(max_length=100)
    nom_origin = models.CharField(max_length=100,blank=True)
    nom_abbrev = models.CharField(max_length=10)
    pays = models.CharField(max_length=40)
    ville = models.CharField(max_length=40)
    pub_date = models.DateTimeField(default=datetime.now)
    
    class Meta:
        managed = True
        db_table = 'sara_bibliotheques'
        verbose_name = _('Library')
        verbose_name_plural = _('Libraries')
        
    def __str__(self):              # __unicode__ on Python 2
        return '%s : %s-%s' % (self.nom, self.pays, self.ville)
        
class Corpus(models.Model):
    id_biblio = models.ForeignKey(Bibliotheque)
    prefix = models.CharField(max_length=25)
    cote = models.IntegerField()
    ancienne_cote = models.CharField(max_length=30)
    pub_date = models.DateTimeField(default=datetime.now)
    
    class Meta:
        managed = True
        db_table = 'sara_corpus'
        verbose_name = _('Corpus')
        verbose_name_plural = _('Corpus')
        
    def __str__(self):              # __unicode__ on Python 2
        return '%s : %s%s' % (self.id_biblio, self.prefix, self.cote)

class Copie(models.Model):
    id_corpus = models.ForeignKey(Corpus)
    numincorpus = models.IntegerField()
    id_texte = models.ForeignKey(Texte)
    folios = models.CharField(max_length=20)
    folio_begin = models.CharField(max_length=10)
    folio_end = models.CharField(max_length=10)
    auteur = models.CharField(max_length=30)
    titre = models.CharField(max_length=70)
    copiste = models.CharField(max_length=60)
    date_hej = models.CharField(max_length=40)
    date = models.CharField(max_length=40)
    lieu = models.CharField(max_length=30)
    commentaires = models.TextField()
    incipit = models.CharField(max_length=200)
    explicit = models.CharField(max_length=400)
    pub_date = models.DateTimeField(default=datetime.now)
    
    class Meta:
        managed = True
        db_table = 'sara_copies_textes'
        verbose_name = _('Copy')
        verbose_name_plural = _('Copies')
        
    def __str__(self):              # __unicode__ on Python 2
        return self.id_texte
        
class Section(models.Model):
    texte = models.ForeignKey(Texte,null=True,blank=False)
    titre = models.CharField(max_length=200,null=True,blank=False)
    contenu = models.TextField(null=True,blank=False)
    pub_date = models.DateTimeField(default=datetime.now)
    
    class Meta:
        managed = True
        db_table = 'sara_sections'
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')
        
    def __str__(self):              # __unicode__ on Python 2
        return '%s : %s' % (self.texte, self.titre)