from django.http import JsonResponse
from django.views import generic
from pymysql import IntegrityError

from allapps.cms import models
from share.error_code import ERROR_DESC, DUPLICATE_FOR_UNIQUE, ENTRY_NONE, UNKNOWN_ERROR
from share.log import logger


class CategoryListView(generic.ListView):
    template_name = "cms/category_list.html"
    model = models.Category


class CategoryCreateView(generic.CreateView):
    def post(self, request, *args, **kwargs):
        name = self.request.POST.get("name")

        if not name:
            return JsonResponse(dict(
                ret=ENTRY_NONE,
                error_msg=ERROR_DESC[ENTRY_NONE],
            ))

        try:
            models.Category.objects.create(name=name)
            return JsonResponse(dict(
                ret=0
            ))
        except IntegrityError:
            return JsonResponse(dict(
                ret=DUPLICATE_FOR_UNIQUE,
                error_msg=ERROR_DESC[DUPLICATE_FOR_UNIQUE]
            ))
        except Exception as e:
            logger.error(e)
            return JsonResponse(dict(
                ret=UNKNOWN_ERROR,
                error_msg=ERROR_DESC[UNKNOWN_ERROR]

            ))


