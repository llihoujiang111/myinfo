from django.db import models
from db.base_model import BaseModel

from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class Article_my(BaseModel):
    article_name = models.CharField(max_length=30, verbose_name='文章名字')
    article_author = models.CharField(max_length=20, verbose_name='作者')
    article_count = RichTextUploadingField(verbose_name='文章内容')
    article_img = models.ImageField(upload_to='article', default='myimg/starlu.png', verbose_name='文章图片')
    article_title = RichTextUploadingField(max_length=100, verbose_name='文章简介')

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.article_name


class Article_pl(BaseModel):
    pl_name = models.CharField(max_length=30, verbose_name='评论昵称')
    pl_eml = models.EmailField(verbose_name='评论邮箱')
    pl_web = models.CharField(max_length=50, verbose_name='评论网站')
    pl_count = models.TextField(verbose_name='评论内容')

    class Meta:
        verbose_name = "回复信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.pl_name
