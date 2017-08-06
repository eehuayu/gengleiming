from django import forms

from allapps.cms.models import Article, Category


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ("title", "content", "category", "keywords",)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("name", )
