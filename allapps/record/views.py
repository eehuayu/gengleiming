from django.views import generic

from .models import IpRecord

class IpRecordListView(generic.ListView):
    model = IpRecord
    template_name = "record/index.html"
