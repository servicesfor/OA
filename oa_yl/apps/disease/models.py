from django.db import models


class Disease(models.Model):       # 疾病模型
    ill_name = models.CharField(max_length=100,verbose_name='疾病名称')     #疾病名称
    symptom = models.CharField(max_length=255,verbose_name='症状')        #症状
    pathogeny = models.CharField(max_length=255,verbose_name='病因')     #病因
    treatment = models.CharField(max_length=255,verbose_name='治疗')    #治疗
    diagnosis = models.CharField(max_length=255,verbose_name='诊断')       #诊断
    Prevention = models.CharField(max_length=255,verbose_name='预防')       #预防
    life = models.CharField(max_length=255,verbose_name='生活')         #生活

    class Meta:
        db_table = 'yl_diseases'
        verbose_name = '疾病表'
        verbose_name_plural = verbose_name

