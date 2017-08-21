import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
rds = redis.Redis(connection_pool=pool)
