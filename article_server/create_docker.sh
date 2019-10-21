#!/usr/bin/env bash
# 需要在 article_server 目录下执行
# 需要预先创建好数据库（需要 docker_init_database 目录下生成的 mysql 容器。他自带生成符合需要的脚本)

imageversion='0.0.1'
imagename="article_server"
image="$imagename:$imageversion"
containername="article_server"
imageport=55002
exportport=55002
dockernetwork="base-mysql-database-network"
logfilename='container_log'

# 建立持久化文件夹
if [ ! -d $logfilename ]; then
  mkdir "$logfilename"
fi

echo "【1】下载 Python:3 版本 image"
docker pull python:3
echo "下载完成或无需下载"

echo "【2】生成容器，容器名为：$image"
docker image build -t "$image" .

echo "【3】查看镜像是否生成成功"
docker images

echo "【4】生成容器，并和mysql容器link到一起"
docker container run --name "$containername" -v "$pwd/$logfilename":/usr/src/app/log --net="$dockernetwork" -p "$exportport:$imageport" -d "$image"
#docker container run --name "$containername" --link=mysql-article-tags:db -p "$exportport:$imageport" -d "$image"
# 这个是加入docker网络，是另外一种方式，更方便
# docker container run --name article_server --net=base-mysql-database-network -p 55002:55002 -d article_server:0.0.1

echo "【5】查看容器是否生成成功"
docker container ps -a
