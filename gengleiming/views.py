from django.views import generic

from allapps.cms import models


class HomeView(generic.TemplateView):
    template_name = "gengleiming/home.html"

    def get_article_list(self):
        return models.Article.objects.all()

    def get_category_list(self):
        return models.Category.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)

        ctx['article_list'] = self.get_article_list()
        ctx['category_list'] = self.get_category_list()
        # if 'HTTP_X_FORWARDED_FOR' in self.request.META:
        #     client_ip = self.request.META['HTTP_X_FORWARDED_FOR']
        #     client_ip = client_ip.split(",")[0]
        # else:
        #     client_ip = self.request.META['REMOTE_ADDR']
        # if not client_ip:
        #     client_ip = '异常'
        # if IpRecord.objects.count() < 10000:
        #     IpRecord.objects.create(ip=client_ip)

        return ctx


class SuccessView(generic.TemplateView):
    template_name = "gengleiming/success.html"


class FailView(generic.TemplateView):
    template_name = "gengleiming/fail.html"
