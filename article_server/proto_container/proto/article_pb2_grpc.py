# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import article_pb2 as article__pb2


class ArticleServiceStub(object):
  """函数
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.AddArticle = channel.unary_unary(
        '/ArticleService/AddArticle',
        request_serializer=article__pb2.AddArticleRequest.SerializeToString,
        response_deserializer=article__pb2.AddArticleReply.FromString,
        )
    self.SelectArticle = channel.unary_unary(
        '/ArticleService/SelectArticle',
        request_serializer=article__pb2.SelectArticleRequest.SerializeToString,
        response_deserializer=article__pb2.SelectArticleReply.FromString,
        )
    self.UpdateArticle = channel.unary_unary(
        '/ArticleService/UpdateArticle',
        request_serializer=article__pb2.UpdateArticleRequest.SerializeToString,
        response_deserializer=article__pb2.UpdateArticleReply.FromString,
        )


class ArticleServiceServicer(object):
  """函数
  """

  def AddArticle(self, request, context):
    """新增文章
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SelectArticle(self, request, context):
    """查询文章
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateArticle(self, request, context):
    """更新文章
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ArticleServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'AddArticle': grpc.unary_unary_rpc_method_handler(
          servicer.AddArticle,
          request_deserializer=article__pb2.AddArticleRequest.FromString,
          response_serializer=article__pb2.AddArticleReply.SerializeToString,
      ),
      'SelectArticle': grpc.unary_unary_rpc_method_handler(
          servicer.SelectArticle,
          request_deserializer=article__pb2.SelectArticleRequest.FromString,
          response_serializer=article__pb2.SelectArticleReply.SerializeToString,
      ),
      'UpdateArticle': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateArticle,
          request_deserializer=article__pb2.UpdateArticleRequest.FromString,
          response_serializer=article__pb2.UpdateArticleReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ArticleService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
