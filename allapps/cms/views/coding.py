from django.views import generic

from allapps.cms.models import Content


class IndexView(generic.TemplateView):
    template_name = "cms/coding/index.html"


class CodeCreateView(generic.CreateView):
    template_name = "cms/coding/write.html"
    model = Content
    fields = ['title', 'content', 'key_word', 'category']
