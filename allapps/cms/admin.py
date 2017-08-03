from django.contrib import admin

# Register your models here.
from allapps.cms import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "create_time")


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("user", "category", "title", "content", "visit_times", "update_time")


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Article, ArticleAdmin)
