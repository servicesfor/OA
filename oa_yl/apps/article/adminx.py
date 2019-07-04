from django.contrib import admin

# Register your models here.
import xadmin
from article.models import Article, Arti_title
from xadmin import views

# 文章管理
class ArtProjeAdmin(object):
    list_display = ('title', 'auth', 'subjection','art_class')
    search_fields = ['title', 'auth', 'subjection','art_class']
    list_filter = ['title', 'auth', 'subjection','art_class']
    list_per_page = 20
    site_title = '文章管理'
    model_icon = 'fa fa-book'

xadmin.site.register(Article, ArtProjeAdmin)

class ArtiProjeAdmin(object):
    list_display = ('subtitle',)
    search_fields = ['subtitle']
    list_filter = ['subtitle']

xadmin.site.register(Arti_title, ArtiProjeAdmin)
