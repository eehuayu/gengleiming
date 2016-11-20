from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.views import generic

from allapps.cms.forms import CmsForm
from allapps.cms.models import Content, Category, KeyWord


class CodingListView(generic.ListView):
    template_name = "cms/coding/index.html"
    model = Content

    def get_context_data(self, **kwargs):
        ctx = super(CodingListView, self).get_context_data(**kwargs)
        if self.request.GET.get("index"):
            pass
        else:
            ctx["contents"] = self.object_list[:10] if len(self.object_list) > 10 else self.object_list
        return ctx


class CodeCreateView(generic.CreateView, PermissionRequiredMixin):
    permission_required = ("dormitory.write", )
    template_name = "cms/coding/write.html"
    model = Content
    form_class = CmsForm
    success_url = reverse_lazy("cms:index")

    def get_context_data(self, **kwargs):
        ctx = super(CodeCreateView, self).get_context_data(**kwargs)
        ctx['categories'] = Category.objects.all()
        ctx['keywords'] = list(KeyWord.objects.exclude(word='').exclude(word=None).values_list("word", flat=True))
        return ctx

    def form_valid(self, form):
        f = form.save(False)
        keyword_list = self.request.POST.get("keyword_add").replace("，", ",").replace(" ", "").split(",")
        keywords = []
        for name in keyword_list:
            keyword = KeyWord.objects.get_or_create(word=name)[0]
            keywords.append(keyword)
        f.user = self.request.user
        f.save()
        f.keyword = keywords
        return super(CodeCreateView, self).form_valid(form)


class CategoryCreateView(generic.View):
    def post(self, request):
        name = request.POST.get("name").strip()
        description = request.POST.get("description")
        if not name:
            return HttpResponse("类别不能为空。")
        try:
            Category.objects.get(name=name)
            return HttpResponse(name + "类别已存在。")
        except Category.DoesNotExist:
            Category.objects.create(name=name, description=description)
            return HttpResponse("增加成功。")
        return HttpResponse("未知错误")
