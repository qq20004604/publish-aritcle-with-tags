#!/usr/bin/env bash
docker container stop mysql-article-tags
docker container rm mysql-article-tags
rm -rf mysqldata