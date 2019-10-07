#!/usr/bin/env bash
# 如果需要使用其他镜像，记得自行修改脚本
# 修改映射到本机的端口也一样
# 需要在 docker_init_database 目录下执行

appfilename="app"
mysqldatafilename="mysqldata"
imagename="docker-demo-02-mysql:0.0.1"
containername="mysql-article-tags"

# 建立持久化文件夹
if [[ ! -d ${mysqldatafilename} ]]; then
  mkdir "$mysqldatafilename"
fi

echo "【1】下载 mysql:5.6 版本 image"
docker pull mysql:5.6
echo "下载完成或无需下载"

echo "【2】先用原本镜像生成容器，初始化不需要密码（后续添加），并进行持久化配置"
echo "$PWD/$mysqldatafilename"
docker run --name "$containername" -v "$PWD/$mysqldatafilename":/var/lib/mysql -p 3306:3306 -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -d mysql:5.6 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
docker run --name "$containername" -v "$PWD/$mysqldatafilename":/var/lib/mysql -p 55001:3306 -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -d mysql:5.6 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci

# 如果自己手动执行的话，下面这行脚本可以在创建容器时即添加账号密码
# docker run --name mysql-demo -d -v "$PWD/$mysqldatafilename":/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=1234567890 mysql:5.6

# 然后把 app 文件拷贝到容器里面
echo "【3】然后把 app 文件拷贝到容器里面"
docker cp "$PWD/$appfilename" "$containername":/

# mac 下需要手动启动，linux 下通常不需要
echo "【4】启动容器"
docker container start mysql-article-tags

echo "【5】执行容器内的初始化脚本"
docker exec "$containername" sh "/$appfilename/init.sh"

echo "【6】查看当前容器状态，Mac 下需要手动输入命令 docker container ps -a 查看当前容器状态，原因是容器可能会自动 exit"
echo " 启动容器的方法是输入： docker container start mysql-article-tags"
docker container ps -a
