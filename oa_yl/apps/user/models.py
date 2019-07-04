from django.db import models
from django.contrib.auth.hashers import make_password


class User(models.Model):
    login_auth_str = models.CharField(max_length=200,null=True,verbose_name='口令')
    create_time = models.DateTimeField(auto_now_add=True,null=True,verbose_name='注册时间')
    update_time = models.DateTimeField(auto_now=True,null=True,verbose_name='更新时间')
    note = models.CharField(max_length=50,
                            blank=True,
                            null=True,verbose_name='备注')      # 备注
    nick_name = models.CharField(max_length=16,verbose_name='昵称')  # 用户昵称
    phone = models.CharField(max_length=15,unique=True,verbose_name='注册手机号')  # 用户手机号
    sex = models.CharField(max_length=2,null=True,verbose_name='性别')  # 性别
    photo = models.CharField(max_length=700,null=True,verbose_name='头像')    #用户头像
    activated = models.IntegerField(null=True,verbose_name='激活状态')  # 用户激活状态

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if all((len(self.login_auth_str) < 70,
                not self.login_auth_str.startswith('pbkdf2_sha256$36000$'))):
            self.login_auth_str = make_password(self.login_auth_str)
        super().save()

    class Meta:
        db_table = 'yl_user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name


class Patient(models.Model):    # 患者模型
    p_user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='用户名称')  # 关联当前登录用户
    p_name = models.CharField(max_length=20,verbose_name='患者姓名')        #患者姓名
    p_ID_number = models.CharField(max_length=18,verbose_name='身份证号')   #患者身份证号
    p_sex = models.CharField(max_length=2,default='男',verbose_name='性别')      #患者性别
    date_birth = models.DateTimeField(verbose_name='出生年月')     #出生年月
    p_weight = models.CharField(max_length=10,verbose_name='体重')      #体重
    is_allergy = models.BooleanField(default=False,verbose_name='过敏史')     #过敏史
    medical_history = models.CharField(max_length=100,blank=True,null=True,verbose_name='过敏病史')  #过往病史
    is_normal_liver = models.BooleanField(default=True,verbose_name='肝功') #   肝功能是否正常
    is_normal_kidney = models.BooleanField(default=True,verbose_name='肾功')  # 肾功能是否正常
    is_pregnancy_preparation = models.BooleanField(default=False,verbose_name='是否备孕')   #是否备孕

    class Meta:
        db_table = 'patient'
        verbose_name = '患者表'
        verbose_name_plural = verbose_name



