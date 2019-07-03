from django.contrib import admin

import xadmin
from doctor.models import Doctor,DoctorQuality


class Basesetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


# 疾病管理
class DocProjeAdmin(object):
    list_display = ('doc_name', 'doc_title','department', 'hospital','doc_exp')
    search_fields = ['doc_name', 'doc_title','department', 'hospital','doc_exp']
    list_filter = ['doc_name', 'doc_title','department', 'hospital','doc_exp']
    list_per_page = 20
    site_title = '医生管理'


xadmin.site.register(Doctor, DocProjeAdmin)


class QuaProjeAdmin(object):
    list_display = ('d_name', 'd_level','m_answer', 'm_recipel','avg_response','is_recommend')
    search_fields = ['d_name', 'd_level','m_answer', 'm_recipel','avg_response','is_recommend']
    list_filter = ['d_name', 'd_level','m_answer', 'm_recipel','avg_response','is_recommend']
    list_per_page = 20
    site_title = '医生属性管理'


xadmin.site.register(DoctorQuality, QuaProjeAdmin)