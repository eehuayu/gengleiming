from django.views import generic


class HomeView(generic.TemplateView):
    template_name = "gengleiming/home.html"

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)
        if 'HTTP_X_FORWARDED_FOR' in self.request.META:
            client_ip = self.request.META['HTTP_X_FORWARDED_FOR']
            client_ip = client_ip.split(",")[0]
        else:
            client_ip = self.request.META['REMOTE_ADDR']
        print(client_ip)
        return ctx
