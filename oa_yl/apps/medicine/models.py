from django.db import models

from user.models import User


class Medicine(models.Model):
    med_name = models.CharField(max_length=200,unique=True,verbose_name='药品名')     # 药名
    med_img = models.CharField(max_length=255,verbose_name='药品图片')  # 图片
    price = models.CharField(max_length=50,verbose_name='药品价格')             # 价格
    med_stock = models.IntegerField(verbose_name='药品库存')   # 库存
    approval_number = models.CharField(max_length=50,verbose_name='批准文号')    # 批准文号
    packing_size = models.CharField(max_length=100,verbose_name='包装规格')         # 包装规格
    med_formulation = models.CharField(max_length=50,verbose_name='剂型')      # 剂型

    class Meta:
        db_table = 'medicine'
        verbose_name = '药品表'
        verbose_name_plural = verbose_name


class Med_Details(models.Model):    #药品详情
    med_name = models.ForeignKey(Medicine,on_delete=models.CASCADE,verbose_name='药品名称')    #关联药品模型
    composition = models.CharField(max_length=500,verbose_name='药品成分')  # 成分
    shape = models.CharField(max_length=500,verbose_name='药品形状')  # 性状
    indications = models.TextField(verbose_name='适应症')  # 适应症
    pdc_date = models.CharField(max_length=50,verbose_name='生产日期')  # 生产日期
    validity_period = models.CharField(max_length=20,verbose_name='有效期')  # 有效期
    manufacturer = models.TextField(verbose_name='制造商')  # 制造商
    med_interact = models.TextField(verbose_name='药品相互作用')  # 药物相互作用
    attentions = models.TextField(verbose_name='注意事项')  # 注意事项
    taboo = models.TextField(verbose_name='禁忌')  # 禁忌
    reaction = models.TextField(verbose_name='不良反应')  # 不良反应
    pharm_toxicity = models.TextField(verbose_name='药理毒理')   # 药理毒理
    storage = models.CharField(max_length=255,verbose_name='贮藏')  # 贮藏

    class Meta:
        db_table = 'med_details'
        verbose_name = '药品详情表'
        verbose_name_plural = verbose_name


class Mid_comment(models.Model):        # 用户评论药品

    med_comm = models.ForeignKey(Medicine,to_field='med_name',on_delete=models.CASCADE,verbose_name='药品名称')
    nick_name = models.CharField(max_length=20,default='匿名用户',verbose_name='用户名')  #昵称关联用户昵称
    score = models.IntegerField(default=5,verbose_name='评分')    #评论星数
    comm_con = models.CharField(max_length=200,default='默认好评',verbose_name='评论内容')
    comm_time = models.DateTimeField(auto_now_add=True,verbose_name='评论时间')

    class Meta:
        db_table = 'mid_comm'
        verbose_name = '药品评论表'
        verbose_name_plural = verbose_name