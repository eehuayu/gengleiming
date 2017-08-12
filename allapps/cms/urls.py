from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from allapps.cms.views import category
from allapps.cms.views import article

urlpatterns = [
    url(r"article/list/(?P<cid>[\d]+)/$", article.ArticleListView.as_view(), name="article_list"),
    url(r"article/create/$", login_required(article.ArticleCreateView.as_view()), name="article_create"),
    url(r"manage/$", login_required(article.ManageTemplateView.as_view()), name="manage"),
    url(r"category/list/$", login_required(category.CategoryListView.as_view()), name="category_list"),
    url(r"category/create/$", login_required(category.CategoryCreateView.as_view()), name="category_create"),
    url(r"article/(?P<pk>[\d]+)/$", article.ArticleDetailView.as_view(), name="article_detail"),
]
