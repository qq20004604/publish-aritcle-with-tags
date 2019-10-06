#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import time
import grpc

# 必须先设置一下环境路径
sys.path.append("../proto")

import article_pb2, article_pb2_grpc

HOST = 'localhost'
PORT = 55002


# 生成成功的返回信息
def success_return(data=None):
    return {
        'code': 200,
        'msg': 'success',
        'data': data
    }


# 生成失败的返回信息
def error_return(msg):
    return {
        'code': 0,
        'msg': msg
    }


def error_log(msg):
    with open('./rpc_err.log', 'a')as f:
        f.write('%s||%s||%s\n' % (
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            sys._getframe(1).f_code.co_name,  # 执行errlog这个函数的函数名字，即上一级函数
            msg
        ))


# RPC专用类（客户端）
class GRPCClient(object):
    def __init__(self):
        server = '%s:%s' % (HOST, PORT)
        # 连接 rpc 服务器
        channel = grpc.insecure_channel(server)
        # 调用 rpc 服务，GreeterStub 这个类名是固定生成的，参照 helloworld_pb2_grpc.py
        self.stub = article_pb2_grpc.ArticleServiceStub(channel)

    # 新增文章
    def add_article(self, article):
        is_error = False
        error_msg = ''
        try:
            # s 是一个基于 dict 的实例
            s = article_pb2.AddArticleRequest(article=article)
            # 调用 SayHello 向 Server 发送信息
            # 这个函数是在 __init__ 时被定义的，定义时，添加了3个参数，分别定义了唯一标识、指定压缩格式（str to 二进制）、解压缩格式。
            # 所以这里调用时，会被自动压缩成对应的参数，然后发送到 server 去。
            # 如果只看转成二进制字符串这一步，相当于
            # import grpc._common as common
            # common.serialize(s, helloworld_pb2.HelloRequest.SerializeToString)
            # 然后你也可以拿去，用自己的通信方式去发送数据
            response = self.stub.AddArticle(s)
        except BaseException as e:
            # 这个错误信息可能是服务器连接失败
            is_error = True
            error_msg = e
            error_log(e.details())
            return error_return('send error')
        finally:
            # 组织返回信息
            if is_error:
                return error_return(error_msg)
            else:
                if response.code is 200:
                    return success_return({
                        'id': response.data.id
                    })
                else:
                    return error_return(response.msg)

    # 查找文章
    def select_article(self, id):
        is_error = False
        error_msg = ''
        try:
            # s 是一个基于 dict 的实例
            s = article_pb2.SelectArticleRequest(id=id)
            response = self.stub.SelectArticle(s)
        except BaseException as e:
            # 这个错误信息可能是服务器连接失败
            is_error = True
            error_msg = e
            error_log(e.details())
            return error_return('send error')
        finally:
            # 组织返回信息
            if is_error:
                return error_return(error_msg)
            else:
                if response.code is 200:
                    return success_return({
                        'id': response.data.id,
                        'article': response.dat.article
                    })
                else:
                    return error_return(response.msg)

    # 更新文章
    def update_article(self, id, article):
        is_error = False
        error_msg = ''
        try:
            # s 是一个基于 dict 的实例
            s = article_pb2.UpdateArticleRequest(id=id, article=article)
            response = self.stub.UpdateArticle(s)
        except BaseException as e:
            # 这个错误信息可能是服务器连接失败
            is_error = True
            error_msg = e
            error_log(e.details())
            return error_return('send error')
        finally:
            # 组织返回信息
            if is_error:
                return error_return(error_msg)
            else:
                if response.code is 200:
                    return success_return({
                        'id': response.data.id
                    })
                else:
                    return error_return(response.msg)


# 测试和示例代码
if __name__ == '__main__':
    client = GRPCClient()
    result_add = client.add_article("abcdefg")
    print(result_add)

    # res2 = client.send_people('张三', 20)
    # if res2['code'] is 200:
    #     print(res2['msg'])
    #     print(res2['data'].isRight)
    # else:
    #     print('error')
