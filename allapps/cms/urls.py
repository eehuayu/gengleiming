from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import article

urlpatterns = [
    url(r"article_list/$", article.ArticleListView.as_view(), name="article_list"),
    url(r"write/$", login_required(article.ArticleCreateView.as_view()), name="write"),
    # url(r"category/create/$", article.CategoryCreateView.as_view(), name="category-create"),
    # url(r"read/(?P<pk>[\d]+)/$", article.ReadDetailView.as_view(), name="read"),
]
