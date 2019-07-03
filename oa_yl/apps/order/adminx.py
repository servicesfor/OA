import xadmin
from order.models import Order, Order_Detail


class Basesetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


# 药品管理
class OrdProjeAdmin(object):
    list_display = ('o_user','o_price', 'o_status','o_id','o_time')
    search_fields = ['o_user','o_price', 'o_status','o_id','o_time']
    list_filter = ['o_user','o_price', 'o_status','o_id','o_time']


xadmin.site.register(Order, OrdProjeAdmin)


class OrdDetProjeAdmin(object):
    list_display = ('o_order', 'o_consignee', 'o_addr', 'o_phone', 'o_goods')
    search_fields = ['o_order', 'o_consignee', 'o_addr', 'o_phone', 'o_goods']
    list_filter = ['o_order', 'o_consignee', 'o_addr', 'o_phone', 'o_goods']


xadmin.site.register(Order_Detail, OrdDetProjeAdmin)