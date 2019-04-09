```
docker run --name mysql -v /data/release/gengleiming_config/mysql/my.cnf:/etc/mysql/my.cnf -v /data/mysql/store:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 -p 3306:3306 -d mysql:5.7
docker run --name redis -v /data/docker/redis/redis.conf:/usr/local/etc/redis/redis.conf -v /data/docker/redis/log/:/var/log/redis/ -p 6379:6379 -d redis:5.0.4
docker run --name nginx --net host  -v /data/code/backend/deploy/dev/nginx/inner/:/etc/nginx/conf.d -v /data/release/:/data/release/ -v /data/code:/data/code 192.168.100.22:5000/nginx 

```
