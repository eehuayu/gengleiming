from django.conf.urls import url

from .views import article

urlpatterns = [
    url(r"^$", article.ArticleListView.as_view(), name="index"),
    url(r"write/$", article.ArticleCreateView.as_view(), name="write"),
    url(r"category/create/$", article.CategoryCreateView.as_view(), name="category-create"),
    url(r"read/(?P<pk>[\d]+)/$", article.ReadDetailView.as_view(), name="read"),
]
