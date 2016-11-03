from django.conf.urls import url
from django.contrib.auth.views import login_required

from . import views

urlpatterns = [
    url(r'^$', login_required(views.IpRecordListView.as_view()), name="ips"),
]
