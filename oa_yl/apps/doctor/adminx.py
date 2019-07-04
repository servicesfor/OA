import xadmin
from doctor.models import Doctor, DoctorQuality, Doc_adv


class Basesetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


# 疾病管理
class DocProjeAdmin(object):
    list_display = ('doc_name', 'department','hospital','doc_title','department', 'hospital','doc_exp','doc_goods')
    search_fields = ['doc_name', 'department','hospital','doc_title','department', 'hospital','doc_exp','doc_goods']
    list_filter = ['doc_name', 'department','hospital','doc_title','department', 'hospital','doc_exp','doc_goods']
    list_per_page = 20
    site_title = '医生管理'


xadmin.site.register(Doctor, DocProjeAdmin)


class QuaProjeAdmin(object):
    list_display = ('d_name', 'd_level','m_answer', 'm_recipel','avg_response','is_recommend','text_price','tel_price','discount','dis_num','new_excl')
    search_fields = ['d_name', 'd_level','m_answer', 'm_recipel','avg_response','is_recommend','text_price','tel_price','discount','dis_num','new_excl']
    list_filter = ['d_name', 'd_level','m_answer', 'm_recipel','avg_response','is_recommend','text_price','tel_price','discount','dis_num','new_excl']
    list_per_page = 20
    site_title = '医生属性管理'


xadmin.site.register(DoctorQuality, QuaProjeAdmin)

#
class AdvProjeAdmin(object):
    list_display = ('doc_adv', 'u_name','score', 'doc_con','doc_time')
    search_fields = ['doc_adv', 'u_name','score', 'doc_con','doc_time']
    list_filter = ['doc_adv', 'u_name','score', 'doc_con','doc_time']
    list_per_page = 20
    site_title = '问诊管理'


xadmin.site.register(Doc_adv, AdvProjeAdmin)

