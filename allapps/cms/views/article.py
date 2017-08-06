from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from allapps.cms import forms
from allapps.cms import models
from share.log import logger


class ArticleListView(generic.ListView):
    """文章列表"""
    template_name = "cms/save_success.html"
    model = models.Article

#     def get_queryset(self):
#         return super(ArticleListView, self).get_queryset().order_by("-create_time")
#
#     def get_context_data(self, **kwargs):
#         ctx = super(ArticleListView, self).get_context_data(**kwargs)
#         if self.request.GET.get("index"):
#             pass
#         else:
#             ctx["articles"] = self.object_list[:10] if len(self.object_list) > 10 else self.object_list
#         return ctx


class ArticleCreateView(generic.CreateView, PermissionRequiredMixin):
    """创建文章"""
    permission_required = ("dormitory.write", )
    template_name = "cms/write.html"
    model = models.Article
    form_class = forms.ArticleForm
    success_url = reverse_lazy("cms:article_list")

    def get_context_data(self, **kwargs):
        ctx = super(ArticleCreateView, self).get_context_data(**kwargs)
        ctx['categories'] = models.Category.objects.all()
        return ctx

    def form_valid(self, form):
        f = form.save(False)
        f.user = self.request.user
        # 外键要重新save --mark
        # f.category = form.category
        f.save()
        return super(ArticleCreateView, self).form_valid(form)

    def form_invalid(self, form):
        logger.debug(form.cleaned_data)
        logger.debug(form.errors)
        return super(ArticleCreateView, self).form_invalid(form)


class ManageTemplateView(generic.TemplateView):
    template_name = 'cms/manage.html'


class CategoryCreateView(generic.CreateView):
    """创建分类"""
    success_url = "success.html"
    model = models.Category
    form_class = forms.CategoryForm

    def form_invalid(self, form):
        logger.debug(form.errors)
        print(form.errors)


# class ReadDetailView(generic.DetailView):
#     template_name = "cms/detail.html"
#     model = Article
