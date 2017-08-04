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
    form_class = forms.CmsForm
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


# class CategoryCreateView(generic.View):
#     """创建分类"""
#     def post(self, request):
#         name = request.POST.get("name").strip()
#         description = request.POST.get("description")
#         if not name:
#             return JsonResponse({"message": "类别不能为空"})
#         try:
#             Category.objects.get(name=name)
#             return JsonResponse({"message": name + "类别已存在"})
#         except Category.DoesNotExist:
#             category = Category.objects.create(name=name, description=description)
#             return JsonResponse({"id": category.id, "name": category.name, "message": "添加成功"})
#
#
# class ReadDetailView(generic.DetailView):
#     template_name = "cms/detail.html"
#     model = Article
