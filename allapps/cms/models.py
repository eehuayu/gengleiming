from django.db import models

# Create your models here.


class Base(models.Model):
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    class Meta:
        abstract = True


class Category(Base):
    name = models.CharField(verbose_name="名称", max_length=255, unique=True)
    description = models.TextField(verbose_name="描述", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "类别"


class KeyWord(Base):
    word = models.CharField(verbose_name="名称", max_length=64, unique=True)

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = verbose_name_plural = "关键字"


class Article(Base):
    from django.contrib.auth.models import User
    user = models.ForeignKey(User, verbose_name="用户", related_name="contents")
    category = models.ForeignKey(Category, verbose_name="类别", on_delete=models.PROTECT, related_name="contents")  # 删除外键之前要先删除级联，否则报错
    keyword = models.ManyToManyField(KeyWord, verbose_name="关键字")
    title = models.CharField(verbose_name="标题", max_length=255)
    content = models.TextField(verbose_name="内容")
    visit_count = models.PositiveIntegerField(verbose_name="访问量", default=0)
    like = models.PositiveIntegerField(verbose_name="喜欢数", default=0)
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    def __str__(self):
        return self.title

    @property
    def time_desc(self):
        from .helper import get_time_desc
        return get_time_desc(self.create_time)

    class Meta:
        verbose_name = verbose_name_plural = "文章"
        permissions = (("write", "写文章"), )


class Comment(Base):
    article = models.ForeignKey(Article, verbose_name="文章", null=True, blank=True, related_name="comments")
    reply = models.PositiveIntegerField(verbose_name="回复评论id", help_text="这里是回复的评论的ID", default=None)
    content = models.TextField(verbose_name="内容")
    like = models.PositiveIntegerField(verbose_name="点赞数", default=0)
    is_article = models.BooleanField(verbose_name="是否文章留言", help_text="是文章下面的留言，或者是留言板的留言")

    def __str__(self):
        return "文章评论:" + self.article.title if self.article else "回复评论:" + str(self.reply)

    class Meta:
        verbose_name = verbose_name_plural = "留言"
