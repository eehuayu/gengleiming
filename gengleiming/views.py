from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from allapps.cms import models
from allapps.cms import mixins


class HomeView(mixins.ListViewWithCategory):
    template_name = "gengleiming/home.html"
    model = models.Article


class SuccessView(mixins.TemplateViewWithCategory):
    template_name = "gengleiming/success.html"


class FailView(mixins.TemplateViewWithCategory):
    template_name = "gengleiming/fail.html"


@csrf_exempt
def unicode_test(request):
    if request.method != "GET":
        return HttpResponse("method is not post, method is " + request.method)

    data = request.GET.get("data")

    if not data:
        return HttpResponse("data is None.")

    return HttpResponse(data)
