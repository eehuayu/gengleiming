from config.redis_key import IP_UPVOTE, IP_UPVOTE_EXPIRE_TIME, IP_VISIT, IP_VISIT_EXPIRE_TIME
from share.rds import rds


class CacheHelper:
    rds = rds
    redis_key = ""
    ex_time = 0

    def get(self):
        return self.rds.get(self.redis_key)

    def set_ex(self):
        self.rds.setex(self.redis_key, self.ex_time)


class UpvoteHelper(CacheHelper):

    def __init__(self, ip):
        self.redis_key = IP_UPVOTE.format(ip=ip)
        self.ex_time = IP_UPVOTE_EXPIRE_TIME


class VisitHelper(CacheHelper):

    def __init__(self, ip):
        self.redis_key = IP_VISIT.format(ip=ip)
        self.ex_time = IP_VISIT_EXPIRE_TIME
