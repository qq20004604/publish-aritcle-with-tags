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

