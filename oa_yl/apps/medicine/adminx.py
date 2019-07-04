import xadmin
from medicine.models import Medicine,Med_Details,Mid_comment


class Basesetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


# 药品管理
class MedProjeAdmin(object):
    list_display = ('med_name','med_img', 'price','med_stock', 'approval_number','packing_size','med_formulation')
    search_fields = ['med_name','med_img', 'price','med_stock', 'approval_number','packing_size','med_formulation']
    list_filter = ['med_name','med_img', 'price','med_stock', 'approval_number','packing_size','med_formulation']
    list_per_page = 20
    site_title = '药品管理'


xadmin.site.register(Medicine, MedProjeAdmin)


class DetProjeAdmin(object):
    list_display = ('med_name', 'composition','shape', 'indications','pdc_date','validity_period','manufacturer','attentions','taboo','reaction','storage')
    search_fields = ['med_name', 'composition','shape', 'indications','pdc_date','validity_period','manufacturer','attentions','taboo','reaction','storage']
    list_filter = ['med_name', 'composition','shape', 'indications','pdc_date','validity_period','manufacturer','attentions','taboo','reaction','storage']
    list_per_page = 20
    site_title = '药品详情管理'


xadmin.site.register(Med_Details, DetProjeAdmin)


class ComProjeAdmin(object):
    list_display = ('med_comm', 'nick_name','score', 'comm_con','comm_time')
    search_fields = ['med_comm', 'nick_name','score', 'comm_con','comm_time']
    list_filter = ['med_comm', 'nick_name','score', 'comm_con','comm_time']
    list_per_page = 20



xadmin.site.register(Mid_comment, ComProjeAdmin)