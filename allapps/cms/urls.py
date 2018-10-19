from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from allapps.cms.views import category
from allapps.cms.views import article

app_name = "cms"

urlpatterns = [
    url("article/list/(?P<cid>[\d]+)/$", article.ArticleListView.as_view(), name="article_list"),
    url("article/create/$", login_required(article.ArticleCreateView.as_view()), name="article_create"),
    url("manage/$", login_required(article.ManageTemplateView.as_view()), name="manage"),
    url("category/list/$", login_required(category.CategoryListView.as_view()), name="category_list"),
    url("category/create/$", login_required(category.CategoryCreateView.as_view()), name="category_create"),
    url("article/(?P<pk>[\d]+)/$", article.ArticleDetailView.as_view(), name="article_detail"),
    url("article/upvote/$", article.ArticleUpvoteView.as_view(), name="article_upvote"),
]
