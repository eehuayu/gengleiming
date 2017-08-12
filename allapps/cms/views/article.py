from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

from allapps.cms import forms
from allapps.cms import models
from allapps.cms import mixins
from share.log import logger


class ArticleListView(mixins.ListViewWithCategory):
    """
    文章列表
    """
    template_name = "cms/save_success.html"
    model = models.Article


class ArticleCreateView(mixins.CreateViewWithCategory, PermissionRequiredMixin):
    """
    创建文章
    """
    permission_required = ("dormitory.write", )
    template_name = "cms/write.html"
    model = models.Article
    form_class = forms.ArticleForm
    success_url = reverse_lazy("cms:article_list")

    def form_valid(self, form):
        f = form.save(False)
        f.user = self.request.user
        f.save()
        return super(ArticleCreateView, self).form_valid(form)

    def form_invalid(self, form):
        logger.debug(form.cleaned_data)
        logger.debug(form.errors)
        return super(ArticleCreateView, self).form_invalid(form)


class ManageTemplateView(mixins.TemplateViewWithCategory):
    """
    管理界面
    """
    template_name = 'cms/manage.html'


class ArticleDetailView(mixins.DetailViewWithCategory):
    """
    文章内容
    """
    template_name = "cms/article_detail.html"
    model = models.Article
