from django.contrib import admin

# Register your models here.
import xadmin
from article.models import Article
from xadmin import views

# 文章管理
class ArtProjeAdmin(object):
    list_display = ('title', 'auth', 'subjection','art_class')
    search_fields = ['title', 'auth', 'subjection','art_class']
    list_filter = ['title', 'auth', 'subjection','art_class']
    date_hierarchy = 'go_time'
    list_per_page = 20
    site_title = '文章管理'
    model_icon = 'fa fa-book'

xadmin.site.register(Article, ArtProjeAdmin)


