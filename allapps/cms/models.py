from django.db import models

# Create your models here.


class Base(models.Model):
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    class Meta:
        abstract = True


class Category(Base):
    name = models.CharField(verbose_name="名称", max_length=255, unique=True)

    class Meta:
        verbose_name = verbose_name_plural = "类别"


class KeyWord(Base):
    word = models.CharField(verbose_name="名称", max_length=64, unique=True)

    class Meta:
        verbose_name = verbose_name_plural = "关键字"


class Content(Base):
    from django.contrib.auth.models import User
    user = models.ForeignKey(User, verbose_name="用户", on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)  # 删除外键之前要先删除级联的书籍，否则报错
    key_word = models.ManyToManyField(KeyWord)
    title = models.CharField(verbose_name="标题", max_length=255)
    content = models.TextField(verbose_name="内容")
    visit_count = models.PositiveIntegerField(verbose_name="访问量", default=0)
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    class Meta:
        verbose_name = verbose_name_plural = "内容"
