from django.conf.urls import url

from .views import coding

urlpatterns = [
    url(r"^$", coding.CodingListView.as_view(), name="index"),
    url(r"coding/write/$", coding.CodeCreateView.as_view(), name="coding-write"),
    url(r"category/create/$", coding.CategoryCreateView.as_view(), name="category-create"),
]
