from django.contrib import admin

# Register your models here.
from allapps.cms import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "create_time")


class KeyWordAdmin(admin.ModelAdmin):
    list_display = ("word", "create_time")


class ContentAdmin(admin.ModelAdmin):
    filter_horizontal = ("keyword", )
    list_display = ("user", "category", "title", "content", "visit_count", "update_time")

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.KeyWord, KeyWordAdmin)
admin.site.register(models.Content, ContentAdmin)
