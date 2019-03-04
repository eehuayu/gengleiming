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
