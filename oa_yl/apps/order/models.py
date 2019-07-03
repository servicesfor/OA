from django.db import models

from medicine.models import Medicine
from user.models import User

class Order(models.Model):
    o_price = models.FloatField(default=0, verbose_name='订单总价')
    o_status = models.IntegerField(default=0, verbose_name='订单状态')
    o_id = models.CharField(max_length=30,unique=True,verbose_name='订单号')
    o_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    o_time = models.DateTimeField(auto_now=True, null=True, verbose_name='下单时间')

    class Meta:
        db_table = "orders"
        verbose_name = '订单表'
        verbose_name_plural = verbose_name


class Order_Detail(models.Model):

    o_order = models.ForeignKey(Order,on_delete=models.CASCADE,to_field='o_id',verbose_name='订单号')
    o_consignee = models.CharField(max_length=20,verbose_name='收货人')
    o_addr = models.CharField(max_length=200,verbose_name='收货地址')
    o_phone = models.CharField(max_length=15,verbose_name='收货人手机号')
    o_goods = models.ForeignKey(Medicine,on_delete=models.CASCADE,verbose_name='订单药品')


    class Meta:
        db_table = 'order_detail'
        verbose_name = '订单详情表'
        verbose_name_plural = verbose_name


