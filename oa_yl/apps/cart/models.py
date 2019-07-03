from django.db import models

from django.db import models

from medicine.models import Medicine
from user.models import User


class Cart(models.Model):   # 购物车模型
    c_user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户')
    c_med = models.ForeignKey(Medicine,on_delete=models.CASCADE,verbose_name='药品')
    c_med_num = models.IntegerField(verbose_name='下单数量')
    c_is_select = models.BooleanField(default=False,verbose_name='选中状态')

    class Meta:
        db_table = 'carts'
        verbose_name = '订单表'
        verbose_name_plural = verbose_name
