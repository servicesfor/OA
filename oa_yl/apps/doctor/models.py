from django.db import models

from hospital.models import Department, Hospital
from user.models import User


class Doctor(models.Model):         # 医生模型
    doc_name = models.CharField(max_length=50,verbose_name='医生姓名')          # 名字
    department = models.ForeignKey(Department,on_delete=models.CASCADE,null=False,verbose_name='医生科室')           # 科室
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE,verbose_name='所属医院')     # 关联医院
    doc_title = models.CharField(max_length=50,null=False,verbose_name='职称')         # 职称
    doc_img = models.CharField(max_length=255,null=False,verbose_name='照片')          # 头像
    doc_exp = models.CharField(max_length=15,null=False,verbose_name='从业时间')                     # 从业时间
    doc_goods = models.CharField(max_length=255,null=False,verbose_name='擅长方向')         # 擅长方向
    doc_resume = models.TextField(verbose_name='医生履历')

    class Meta:
        db_table = 'doctors'
        verbose_name = '医生表'
        verbose_name_plural = verbose_name


class DoctorQuality(models.Model):      # 医生相关属性模型
    d_name = models.ForeignKey(Doctor,on_delete=models.CASCADE,verbose_name='医生')         # 关联医生
    d_level = models.IntegerField(default=5,verbose_name='评分')        # 医生评分星级
    m_answer = models.CharField(max_length=20,verbose_name='月回答次数')    # 月回答次数
    m_recipel = models.IntegerField(verbose_name='月处方数量')   # 月处方数量
    avg_response = models.IntegerField(verbose_name='平均回复时间')    # 平均回复时间
    is_recommend = models.BooleanField(default=False,verbose_name='是否力荐')        # 是否力荐
    text_price = models.CharField(max_length=20,verbose_name='图文问诊价格')    # 图文问诊价格
    tel_price = models.CharField(max_length=50,verbose_name='电话问诊价格')     # 电话问诊价格
    discount = models.CharField(max_length=50,null=True,verbose_name='是否折扣')    # 问诊折扣
    dis_num = models.IntegerField(null=True,verbose_name='折扣剩余名额')
    new_excl = models.BooleanField(verbose_name='是否新人专享')

    class Meta:
        db_table = 'doctor_quality'
        verbose_name = '医生属性表'
        verbose_name_plural = verbose_name


class Doc_comm(models.Model):   # 用户对医生评价表
    doc_comm = models.ForeignKey(Doctor,on_delete=models.CASCADE, verbose_name='医生名称')
    nick_name = models.CharField(max_length=20, default='匿名用户', verbose_name='用户名')  # 昵称关联用户昵称
    score = models.IntegerField(default=5, verbose_name='评分')  # 评论星数
    comm_con = models.CharField(max_length=200, default='默认好评', verbose_name='评论内容')
    comm_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')

    class Meta:
        db_table = 'doc_comm'
        verbose_name = '医生评价表'
        verbose_name_plural = verbose_name


class Doc_adv(models.Model):   # 用户对医生问诊表   相当于我的问诊表
    doc_adv = models.ForeignKey(Doctor,on_delete=models.CASCADE, verbose_name='医生名称')
    u_name = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户名')  # 昵称关联用户昵称
    score = models.IntegerField(default=5, verbose_name='评分')  # 评论星数
    doc_con = models.CharField(max_length=200, default='默认好评', verbose_name='评论内容')
    doc_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')

    class Meta:
        db_table = 'doc_adv'
        verbose_name = '我的问诊表'
        verbose_name_plural = verbose_name


class Focus_doc(models.Model):  # 用户关注医生表
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 关联用户,关注医生
    doc = models.ForeignKey(Doctor, on_delete=models.CASCADE)  # 关联文章,被关注者

    class Meta:
        db_table = 'focus_doc'