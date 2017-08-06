from django.urls import reverse_lazy
from django.views import generic

from allapps.cms import models
from allapps.cms.forms import CategoryForm


class CategoryListView(generic.ListView):
    template_name = "cms/category_list.html"
    model = models.Category


class CategoryCreateView(generic.CreateView):
    template_name = "cms/category_list.html"
    model = models.Category
    success_url = reverse_lazy("success")
    form_class = CategoryForm
