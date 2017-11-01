from django.http import HttpResponse

from allapps.cms import models
from allapps.cms import mixins


class HomeView(mixins.ListViewWithCategory):
    template_name = "gengleiming/home.html"
    model = models.Article


class SuccessView(mixins.TemplateViewWithCategory):
    template_name = "gengleiming/success.html"


class FailView(mixins.TemplateViewWithCategory):
    template_name = "gengleiming/fail.html"


def unicode_test(request):
    if request.method != "post":
        return HttpResponse("method is not post.")

    data = request.POST.get("data")

    if not data:
        return HttpResponse("data is None.")

    print(type(data))
    print(data)

    return HttpResponse(data)
