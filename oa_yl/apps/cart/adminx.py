from django.contrib import admin

# Register your models here.
import xadmin
from cart.models import Cart



class Basesetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


# 文章管理
class CartProjeAdmin(object):
    list_display = ('c_user', 'c_med', 'c_med_num','c_is_select')
    search_fields = ['c_user', 'c_med', 'c_med_num','c_is_select']
    list_filter = ['c_user', 'c_med', 'c_med_num','c_is_select']
    list_per_page = 20


xadmin.site.register(Cart, CartProjeAdmin)