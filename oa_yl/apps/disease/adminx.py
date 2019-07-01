from django.contrib import admin

import xadmin
from disease.models import Disease
from xadmin import views


class Basesetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True

class GlobalSetting(object):
    site_title = u'TN'
    site_footer = u'TN'
    menu_style = 'accordion'  # 实现折叠功能
    list_per_page = 20

xadmin.site.register(views.CommAdminView, GlobalSetting)


# 疾病管理
class DisProjeAdmin(object):
    list_display = ('ill_name', 'symptom', 'pathogeny','treatment','Prevention')
    search_fields = ['ill_name', 'symptom', 'pathogeny','treatment','Prevention']
    list_filter = ['ill_name', 'symptom', 'pathogeny','treatment','Prevention']
    list_per_page = 20


xadmin.site.register(Disease, DisProjeAdmin)
