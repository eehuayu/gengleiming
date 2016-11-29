from django import forms

from allapps.cms.models import Article


class CmsForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ("title", "content", "category")
