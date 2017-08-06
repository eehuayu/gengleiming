from django.views import generic

from allapps.record.models import IpRecord


class HomeView(generic.TemplateView):
    template_name = "gengleiming/home.html"

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)
        # if 'HTTP_X_FORWARDED_FOR' in self.request.META:
        #     client_ip = self.request.META['HTTP_X_FORWARDED_FOR']
        #     client_ip = client_ip.split(",")[0]
        # else:
        #     client_ip = self.request.META['REMOTE_ADDR']
        # if not client_ip:
        #     client_ip = '异常'
        # if IpRecord.objects.count() < 10000:
        #     IpRecord.objects.create(ip=client_ip)
        ctx['home'] = True
        return ctx


class SuccessView(generic.TemplateView):
    template_name = "gengleiming/success.html"


class FailView(generic.TemplateView):
    template_name = "gengleiming/fail.html"
