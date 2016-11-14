from django import forms

from allapps.cms.models import Content


class CmsForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ("title", "content", "category")
