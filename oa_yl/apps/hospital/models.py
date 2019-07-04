from django.db import models

class Hospital(models.Model):    #医院模型
    hosp_name = models.CharField(max_length=100,verbose_name='医院名称')  #医院名称
    hosp_addr = models.CharField(max_length=100,verbose_name='医院地址')  #医院地址
    hosp_tel = models.CharField(max_length=30,verbose_name='医院电话')                 #医院电话
    medical_insurance = models.CharField(max_length=20,default="医保定点",verbose_name='医保')       #是否医保
    hosp_level = models.CharField(max_length=20,verbose_name='医院级别')    #医院级别
    hosp_img = models.CharField(max_length=255,verbose_name='医院图片')    #医院图片

    class Meta:
        db_table = 'hospitals'
        verbose_name = '医院表'
        verbose_name_plural = verbose_name


class Department(models.Model):  # 科室模型
    name = models.CharField(max_length=50,verbose_name='科室名称')  # 科室名称

    class Meta:
        db_table = 'departments'
        verbose_name = '科室表'
        verbose_name_plural = verbose_name


class Province(models.Model):      # 医院所属省份模型
    pro_name = models.CharField(max_length=15,unique=True,verbose_name='省份')

    class Meta:
        db_table = 'provinces'
        verbose_name = '省份表'
        verbose_name_plural = verbose_name


class City(models.Model):           # 医院所属城市模型
    city_name = models.CharField(max_length=15,verbose_name='城市')
    pro_name = models.ForeignKey(Province,on_delete=models.CASCADE,verbose_name='城市所在省份')

    class Meta:
        db_table = 'cities'
        verbose_name = '城市表'
        verbose_name_plural = verbose_name
