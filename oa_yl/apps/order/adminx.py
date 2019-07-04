import xadmin
from order.models import Order, Order_Detail, Receive


class Basesetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


# 药品管理
class RecProjeAdmin(object):
    list_display = ('r_name','r_user', 'r_phone','r_addr','r_default')
    search_fields = ['r_name','r_user', 'r_phone','r_addr','r_default']
    list_filter = ['r_name','r_user', 'r_phone','r_addr','r_default']
    list_per_page = 20
    site_title = '订单管理'


xadmin.site.register(Receive, RecProjeAdmin)


class OrdProjeAdmin(object):
    list_display = ('o_price', 'o_status', 'o_id', 'o_user', 'o_time','o_receive')
    search_fields = ['o_price', 'o_status', 'o_id', 'o_user', 'o_time','o_receive']
    list_filter = ['o_price', 'o_status', 'o_id', 'o_user', 'o_time','o_receive']
    list_per_page = 20
    site_title = '订单详情管理'


xadmin.site.register(Order, OrdProjeAdmin)

class OrdDetProjeAdmin(object):
    list_display = ('o_order', 'o_goods', 'o_med_num', 'o_med_price')
    search_fields = ['o_order', 'o_goods', 'o_med_num', 'o_med_price']
    list_filter = ['o_order', 'o_goods', 'o_med_num', 'o_med_price']
    list_per_page = 20
    site_title = '订单详情管理'


xadmin.site.register(Order_Detail, OrdDetProjeAdmin)