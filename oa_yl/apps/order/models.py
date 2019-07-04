from django.db import models

from medicine.models import Medicine
from user.models import User

class Receive(models.Model):        # 收货信息模型
    r_name = models.CharField(max_length=20,verbose_name='收货人')
    r_user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户')
    r_phone = models.CharField(max_length=15,verbose_name='收货人电话')
    r_addr = models.CharField(max_length=200,verbose_name="收货地址")
    r_default = models.BooleanField(default=False,verbose_name='默认收货地址')
    class Meta:
        db_table = 'yl_receive'
        verbose_name = '收货信息'
        verbose_name_plural = verbose_name



class Order(models.Model):      # 订单模型
    o_price = models.FloatField(default=0, verbose_name='订单总价')
    o_status = models.IntegerField(default=0, verbose_name='订单状态')
    o_id = models.CharField(max_length=30,unique=True,verbose_name='订单号')
    o_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    o_time = models.DateTimeField(auto_now=True, null=True, verbose_name='下单时间')
    o_receive = models.ForeignKey(Receive,null=True,on_delete=models.CASCADE,verbose_name='收货人信息')

    class Meta:
        db_table = "orders"
        verbose_name = '订单表'
        verbose_name_plural = verbose_name


class Order_Detail(models.Model):       # 订单详情模型
    o_order = models.ForeignKey(Order,on_delete=models.CASCADE,to_field='o_id',verbose_name='订单号')
    o_goods = models.ForeignKey(Medicine,on_delete=models.CASCADE,verbose_name='订单药品')
    o_med_num = models.IntegerField(null=True,verbose_name='药品数量')
    o_med_price = models.FloatField(null=True,verbose_name='单个药品总价')


    class Meta:
        db_table = 'order_detail'
        verbose_name = '订单详情表'
        verbose_name_plural = verbose_name



