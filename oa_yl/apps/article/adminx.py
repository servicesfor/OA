from django.contrib import admin

# Register your models here.
import xadmin
from article.models import Article
from xadmin import views


class Basesetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


# 文章管理
class ArtProjeAdmin(object):
    list_display = ('title', 'auth', 'subjection')
    search_fields = ['title', 'auth', 'subjection']
    list_filter = ['title', 'auth', 'subjection']
    list_per_page = 20


xadmin.site.register(Article, ArtProjeAdmin)


