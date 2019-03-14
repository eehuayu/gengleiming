docker run --name mysql -v /data/docker/mysql/conf.d:/etc/mysql/conf.d -v /data/docker/mysql/store:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 -p 3306:3306 -d mysql:5.7
