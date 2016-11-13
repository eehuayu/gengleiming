from django.urls import reverse_lazy
from django.views import generic

from allapps.cms.forms import CmsForm
from allapps.cms.models import Content, Category, KeyWord


class IndexView(generic.TemplateView):
    template_name = "cms/coding/index.html"


class CodeCreateView(generic.CreateView):
    template_name = "cms/coding/write.html"
    model = Content
    form_class = CmsForm
    success_url = reverse_lazy("cms:index")

    def get_context_data(self, **kwargs):
        ctx = super(CodeCreateView, self).get_context_data(**kwargs)
        ctx['categories'] = Category.objects.all()
        ctx['keywords'] = KeyWord.objects.all()
        return ctx

    def form_valid(self, form):
        f = form.save(False)
        print(111)
        keyword_list = self.request.POST.get("keyword_add").split(",")
        keywords = []
        for name in keyword_list:
            keyword = KeyWord.objects.get_or_create(word=name)[0]
            keywords.append(keyword)
        f.save()
        f.keyword = keywords
        return super(CodeCreateView, self).form_valid(form)
    
    def form_invalid(self, form):
        print(222)
        print(form.errors)
        return super(CodeCreateView, self).form_invalid(form)
