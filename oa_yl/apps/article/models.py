from django.db import models

from user.models import User


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='文章标题')  # 标题
    auth = models.CharField(max_length=20, verbose_name='文章作者')  # 作者
    subjection = models.CharField(max_length=100, verbose_name='作者所属平台')  # 作者所属于平台
    content = models.TextField(verbose_name='内容')  # 内容

    class Meta:
        db_table = 'articles'
        verbose_name = '科普文章'
        verbose_name_plural = verbose_name


class Collect_art(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 关联用户,收藏文章
    arc = models.ForeignKey(Article, on_delete=models.CASCADE)  # 关联文章,被关注者

    class Meta:
        db_table = 'collect_art'