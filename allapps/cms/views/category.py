from django.http import JsonResponse
from django.views import generic
from pymysql import IntegrityError

from allapps.cms import models
from share import error_code
from share.log import logger


class CategoryListView(generic.ListView):
    template_name = "cms/category_list.html"
    model = models.Category


class CategoryCreateView(generic.CreateView):
    def post(self, request, *args, **kwargs):
        name = self.request.POST.get("name")

        if not name:
            return JsonResponse(dict(
                ret=error_code.ENTRY_NONE,
                error_msg=error_code.ENTRY_NONE_DESC,
            ))

        try:
            models.Category.objects.create(name=name)
            return JsonResponse(dict(
                ret=0
            ))
        except IntegrityError:
            return JsonResponse(dict(
                ret=error_code.DUPLICATE_FOR_UNIQUE,
                error_msg=error_code.DUPLICATE_FOR_UNIQUE_DESC,
            ))
        except Exception as e:
            logger.error(e)
            return JsonResponse(dict(
                ret=error_code.UNKNOWN_ERROR,
                error_msg=error_code.UNKNOWN_ERROR_DESC,
           ))


