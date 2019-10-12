#!/usr/bin/env bash
# 需要在 article_server 目录下执行
# 需要预先创建好数据库（需要 docker_init_database 目录下生成的 mysql 容器。他自带生成符合需要的脚本)

imageversion='0.0.1'
imagename="article_server"
image="$imagename:$imageversion"
containername="article_server"
imageport=55002
exportport=55002

echo "【1】下载 Python:3 版本 image"
docker pull python:3
echo "下载完成或无需下载"

echo "【2】生成容器，容器名为：$image"
docker image build -t "$image" .

echo "【3】查看镜像是否生成成功"
docker images

echo "【4】生成容器"
docker container run --name "$containername" -p "$exportport:$imageport" -d "$image"

echo "【5】查看容器是否生成成功"
docker container ps -a
