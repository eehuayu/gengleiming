from django.db import models


class IpRecord(models.Model):
    ip = models.CharField(verbose_name="ip地址", max_length=64)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    class Meta:
        verbose_name = "访问者IP历史记录"
