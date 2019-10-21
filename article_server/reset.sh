#!/usr/bin/env bash
# 删除创建的容器使用
containername="article_server"
imageversion='0.0.1'
imagename="article_server"
logfilename='container_log'

image="$imagename:$imageversion"
docker container stop $containername
docker container rm $containername
docker image rm $image
rm -rf $logfilename