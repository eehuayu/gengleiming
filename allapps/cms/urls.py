from django.conf.urls import url

from .views import coding


urlpatterns = [
    url(r"^$", coding.IndexView.as_view(), name="index"),
    url(r"coding/write/$", coding.CodeCreateView.as_view(), name="coding-write"),
]
