from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from allapps.cms import config


class Base(models.Model):
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    class Meta:
        abstract = True


class Category(Base):
    name = models.CharField(verbose_name="名称", max_length=100, unique=True)
    description = models.TextField(verbose_name="描述", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "类别"


class Article(Base):
    user = models.ForeignKey(User, verbose_name="用户", related_name="user")
    title = models.CharField(verbose_name="标题", max_length=255)
    content = models.TextField(verbose_name="内容")
    category = models.ForeignKey(Category, verbose_name="类别", on_delete=models.PROTECT, related_name="contents")   # 删除外键之前要先删除级联，否则报错
    keywords = models.CharField(verbose_name="关键字", max_length=255)
    visit_times = models.PositiveIntegerField(verbose_name="访问量", default=0)
    like_times = models.PositiveIntegerField(verbose_name="喜欢数", default=0)
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    @property
    def time_desc(self):
        from .helper import get_time_desc
        return get_time_desc(self.create_time)

    @property
    def comment_count(self):
        """
        评论数
        :return:
        """
        article = Article.objects.get(id=self.id)
        article_comment_count = article.comments.count()
        return article_comment_count

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = "文章"
        permissions = (("write", "写文章"), )
        ordering = ("-create_time", )


class Comment(Base):
    article = models.ForeignKey(Article, verbose_name="文章", null=True, blank=True, related_name="comments")
    content = models.TextField(verbose_name="内容")
    type = models.PositiveSmallIntegerField(verbose_name="留言的类型", choices=config.COMMENT_TYPE)

    def __str__(self):
        return dict(config.COMMENT_TYPE)[self.type] + ":" + self.article.title

    class Meta:
        verbose_name = verbose_name_plural = "留言"
