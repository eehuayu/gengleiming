from allapps.cms.models import Category
from share.log import logger


def with_category(parent):
    print(222)
    def inner(cls):
        def wrapper(*args):
            # 这里不能用parent().get_context_data()，会报错
            ctx = cls().get_context_data()

            def get_context_date(self):
                ctx['category_list'] = Category.objects.all()
                return ctx

            # 重写父类的属性，把子类初始化之前的get_context_data属性重写后再覆盖掉父类的
            if not parent.hasattr("get_context_data"):
                logger.error("class: %s, has no attribute get_context_data")
                raise Exception("class has no attribute get_context_data")

            parent.get_context_data = get_context_date

            print(dir(cls))

        return cls

    return inner
