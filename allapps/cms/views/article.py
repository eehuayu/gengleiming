from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy, reverse

from allapps.cms import forms
from allapps.cms import models
from allapps.cms import mixins
from allapps.cms.utils import get_ip
from config import redis_key
from share.log import logger
from share.rds import rds


class ArticleListView(mixins.ListViewWithCategory):
    """
    文章列表
    """
    template_name = "cms/article_list.html"
    model = models.Article

    def get_queryset(self):
        cid = int(self.kwargs['cid'])

        if not cid:
            return super(ArticleListView, self).get_queryset()

        query_set = self.model.objects.filter(category_id=cid)
        return query_set


class ArticleCreateView(mixins.CreateViewWithCategory, PermissionRequiredMixin):
    """
    创建文章
    """
    permission_required = ("dormitory.write", )
    template_name = "cms/article_create.html"
    model = models.Article
    form_class = forms.ArticleForm
    success_url = reverse_lazy("cms:article_list", args=[0])

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

    def get_context_data(self, **kwargs):
        ctx = super(ArticleDetailView, self).get_context_data(**kwargs)

        request_ip = get_ip(self.request)
        rds_key = redis_key.IP_VISIT.format(ip=request_ip)

        ret = rds.get(rds_key)

        # 一个IP一天之内只统计一次浏览数
        if not ret:
            self.object.visit_times += 1
            self.object.save()
            rds.setex(rds_key, 1, redis_key.IP_VISIT_EXPIRE_TIME)
        else:
            ctx['disabled'] = 1

        return ctx
