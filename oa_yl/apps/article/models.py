from django.db import models

from user.models import User


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='文章标题')  # 标题
    auth = models.CharField(max_length=20, verbose_name='文章作者')  # 作者
    auth_img = models.CharField(max_length=200,verbose_name='作者头像')
    subjection = models.CharField(max_length=100, verbose_name='作者所属平台')  # 作者所属于平台
    title_img = models.CharField(max_length=200,null=True,verbose_name='文章图片')
    content = models.TextField(verbose_name='内容')  # 内容
    art_class = models.CharField(max_length=50,null=True,verbose_name='文章分类')

    class Meta:
        db_table = 'articles'
        verbose_name = '科普文章'
        verbose_name_plural = verbose_name


class Collect_art(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 关联用户,收藏文章
    arc = models.ForeignKey(Article, on_delete=models.CASCADE)  # 关联文章,被关注者

    class Meta:
        db_table = 'collect_art'


class Arti_title(models.Model):
    subtitle = models.CharField(max_length=100,verbose_name='常见疾病类别')

    class Meta:
        db_table = 'art_title'
        verbose_name = '科普分类'
        verbose_name_plural = verbose_name


class Article_image(models.Model):
    image = models.CharField(max_length=200,verbose_name='科普文章图片')
    subtitle_id = models.ForeignKey(Arti_title,verbose_name='常见疾病')
    art_cont = models.ForeignKey(Article,null=True,verbose_name="文章内容")

    class Meta:
        db_table = 'article_image'
        verbose_name = '科普常见疾病'
        verbose_name_plural = verbose_name
