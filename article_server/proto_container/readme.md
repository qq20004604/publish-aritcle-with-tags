# 使用说明

## 0、安装的依赖什么的

使用 GRPC

完整版参考：https://juejin.im/post/5b19590b6fb9a01e4b062391

简单版参考：https://github.com/qq20004604/Python-RPC-demo

## 1、定义 proto 文件

假如新增的 proto 文件名为 article.proto

在 proto 文件夹下新建他，然后按照语法编写，语法参照：

https://colobu.com/2017/03/16/Protobuf3-language-guide/

## 2、编译

在 article_server/proto_container/proto 目录下执行（需要 python3，实际第一个指令可能是 python3 也可能是 python，主要看你环境配置怎么写的，到底哪个指向 python3）

```
python3 -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I. article.proto
```

然后直接使用的话，可能会报路径错误问题。因此需要设置 path，方法如下：

```
import sys

sys.path.append([proto 生成的 py 文件，他们在当前应用中的文件夹的路径])
# 例如 sys.path.append("proto_container/proto")
```

## 3、使用方法

参照 https://github.com/qq20004604/Python-RPC-demo 吧