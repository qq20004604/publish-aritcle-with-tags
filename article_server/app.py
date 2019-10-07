#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from concurrent import futures
import time
import grpc
import sys

# 必须先设置一下环境路径
sys.path.append("proto_container/proto")

import article_pb2, article_pb2_grpc
from article_server_controller import ArticleController

PORT = 55002
MAX_WORKERS = 10


# 实现 proto 文件中定义的 ArticleService，注意继承的 class，需要是有同名函数的那个
class ArticleService(article_pb2_grpc.ArticleServiceServicer):
    # 新增文章
    def AddArticle(self, request, context):
        print('---- client AddArticle:\narticle: %s' % request.article)
        # 先拿到数据
        article_content = request.article
        # 创建实例
        ac = ArticleController()
        # 调用示例方法，将文章插入
        result = ac.insert(content=article_content)
        print(result['data'])
        # 返回信息给 client 端
        return article_pb2.AddArticleReply(**result)

    # 查找文章
    def SelectArticle(self, request, context):
        print('---- client SelectArticle:\nid: %s' % request.id)
        # 创建实例
        ac = ArticleController()
        # 调用示例方法，查找符合的数据
        result = ac.select(id=request.id)
        print('---- client SelectArticle result: ----\nresult: %s' % result)
        # 返回信息给 client 端
        return article_pb2.SelectArticleReply(**result)

    # 更新文章
    def UpdateArticle(self, request, context):
        print('---- client UpdateArticle:\nid: %s\n article: %s' % (request.id, request.article))
        # 先拿到数据
        article_content = request.article
        id = request.id
        # 创建实例
        ac = ArticleController()
        # 调用示例方法，将文章插入
        result = ac.update(id=id, content=article_content)
        # 返回信息给 client 端
        return article_pb2.UpdateArticleReply(**result)


class ArticleServer(object):
    def __init__(self):
        pass

    def run(self):
        # 启动 rpc 服务，设置连接池，最大为10个用户
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=MAX_WORKERS))
        # 设置 Server，并启用响应函数
        article_pb2_grpc.add_ArticleServiceServicer_to_server(ArticleService(), server)
        # 监听本机的 55002 端口
        server.add_insecure_port('[::]:%s' % PORT)
        # 启动服务
        server.start()
        print('server start!')
        # 这个是为了维持 Server 一直在启动。从这里可以推断，上面应该是起了一个新的线程或者进程。
        try:
            while True:
                time.sleep(60 * 60 * 24)  # one day in seconds
        except KeyboardInterrupt:
            # 如果用户手动中断（比如 ctrl + c？）
            print('server exit!')
            server.stop(0)


# 测试和示例代码
if __name__ == '__main__':
    s = ArticleServer()
    s.run()
