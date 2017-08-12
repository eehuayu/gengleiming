from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from allapps.cms.views import category
from .views import article

urlpatterns = [
    url(r"article_list/$", article.ArticleListView.as_view(), name="article_list"),
    url(r"write/$", login_required(article.ArticleCreateView.as_view()), name="write"),
    url(r"manage/$", login_required(article.ManageTemplateView.as_view()), name="manage"),
    url(r"category/list/$", login_required(category.CategoryListView.as_view()), name="category_list"),
    url(r"category/create/$", login_required(category.CategoryCreateView.as_view()), name="category_create"),
    url(r"read/(?P<pk>[\d]+)/$", article.ArticleDetailView.as_view(), name="article_detail"),
]
