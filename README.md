# publish-aritcle-with-tags

## 使用说明

### 1、配置 database

先确保自己有安装docker，本地的mysql需要通过docker来安装，以确保不存在环境问题 + 自动化配置环境。

docker的使用说明见：https://github.com/qq20004604/docker-learning

然后运行以下命令，自动化安装 MySQL

```
sh docker_init_database/create-image-mysql.sh
```

安装好了后，默认登陆方法是：（需要你本机有安装mysql，或者使用第三方管理工具登入）

```
mysql -h 127.0.0.1 -P 3306 -u root -pabcd1235ojpibetbenoinwef
```

假如无法登陆，执行以下代码检查容器是否已启动（Mac下大部分情况下会自动退出，Linux通常不会）

```
docker container ps -a
```

如果 ``STATUS`` 列显示：``Exited (1) 44 seconds ago ``，说明容器停止运行了，启动它即可。

```
docker container start mysql-article-tags
```

<b>其他：</b>

如果安装失败，或者遇见问题，可以运行以下命令重置

```
sh docker_init_database/reset.sh
```

### 2、版本更新说明

> 0.0.1 (done)

1. 内容继承于另外一个框架，东西略，后续会补充；
2. 封装了专门的 article_server 服务，使用 RPC 来获取数据；
3. 入口 ``article_server/app.py``；
4. client 端测试 ``article_server/proto_container/client/__init__.py``
5. 使用 Google Protocol Buffer
6. proto 文件：``article_server/proto_container/proto/article.proto``
7. 根据 proto 文件生成对应的文件的脚本：``article_server/proto_container/proto/init_proto.sh``
8. RPC 接口：``article_server/readme.md``
9. RPC 使用说明：``article_server/proto_container/proto``

> 0.0.2 （plan)

1. 将 article_server 封装为 docker 容器来对外提供服务