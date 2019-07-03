from django.contrib import admin
import xadmin
from hospital.models import Hospital,Department,Province,City


# 医院管理
class HosProjeAdmin(object):
    list_display = ('hosp_name', 'hosp_addr','hosp_tel', 'medical_insurance','hosp_level')
    search_fields = ['hosp_name', 'hosp_addr','hosp_tel', 'medical_insurance','hosp_level']
    list_filter = ['hosp_name', 'hosp_addr','hosp_tel', 'medical_insurance','hosp_level']
    list_per_page = 20
    site_title = '医院管理'
    model_icon = 'fa fa-briefcase'

xadmin.site.register(Hospital, HosProjeAdmin)


class DepProjeAdmin(object):
    list_display = ('name',)
    search_fields = ['name']
    list_filter = ['name']
    list_per_page = 20


xadmin.site.register(Department, DepProjeAdmin)


class ProProjeAdmin(object):
    list_display = ('pro_name',)
    search_fields = ['pro_name']
    list_filter = ['pro_name']
    list_per_page = 20
    site_title = '省份管理'


xadmin.site.register(Province, ProProjeAdmin)


class CityProjeAdmin(object):
    list_display = ('city_name', 'pro_name')
    search_fields = ['city_name', 'pro_name']
    list_filter = ['city_name', 'pro_name']
    list_per_page = 20
    site_title = '城市管理'


xadmin.site.register(City, CityProjeAdmin)
