import datetime
from django.utils.timezone import utc


def get_time_desc(date_time):
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    seconds = (now - date_time).seconds
    days = (now - date_time).days
    months = now.month - date_time.month
    years = now.year - date_time.year
    if days < 1:
        if 0 < seconds < 60:
            return "刚刚"
        if 60 <= seconds < 3600:
            return "{0}分钟之前".format(seconds // 60)
        if 3600 <= seconds < 3600 * 24:
            return "{0}小时以前".format(seconds // 3600)
    elif 1 <= days < 31:
        return "{0}天以前".format(days)
    elif now.month - date_time.month < 12:
        return "{0}个月以前".format(months)
    else:
        return "{0}年以前".format(years)
