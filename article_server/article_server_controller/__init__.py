#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mysql_lingling import MySQLTool
from config.mysql_options import mysql_config


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


class ArticleController:
    def __init__(self):
        pass

    # 生成 mysql controller 实例
    def _init_mysql(self):
        return MySQLTool(host=mysql_config['host'],
                         user=mysql_config['user'],
                         password=mysql_config['pw'],
                         port=mysql_config['port'],
                         database=mysql_config['database'])

    # 查
    def select(self, id):
        # 连接数据库
        with self._init_mysql() as mtool:
            # 执行sql并获得返回结果
            result = mtool.run_sql([
                ['SELECT * from article_content where id = %s', [id]]
            ])
            # result 成功的情况下，可能是一个空的 list，或者是一个有一个元素的 list（原因是限定了 id）
            # 失败的话，返回 False
            # print(result)

            # 失败，返回提示信息
            if result is False:
                # 理论上不会触发这个，除非表本身有错误
                return error_return('Select error!')
            else:
                # 没有查到结果，返回提示信息
                if len(result) <= 0:
                    return error_return("None result")
                else:
                    # 成功查到，返回内容
                    return success_return({
                        'id': result[0][0],
                        'article': result[0][1]
                    })

    # 增
    def insert(self, content, status=0):
        verify_result = self.verify_content(content)
        if len(verify_result) > 0:
            return error_return(verify_result)

        # 连接数据库
        with self._init_mysql() as mtool:
            result = mtool.insert_row(
                'INSERT article_content(content, status) values (%s, %s)',
                (content, status)
            )
            if result is False:
                return error_return('insert error!')
            else:
                return success_return({
                    'id': result
                })

    # 改
    def update(self, id, content):
        verify_result = self.verify_content(content)
        if len(verify_result) > 0:
            return error_return(verify_result)

        # 连接数据库
        with self._init_mysql() as mtool:
            result = mtool.update_row(
                'UPDATE article_content SET content = %s where id = %s',
                (content, id)
            )
            if result is False:
                return error_return('insert error!')
            else:
                # 如果返回 0，说明没有触发更新。两种情况：1、该行存在，但不需要更新；2、该行不存在
                if result == 0:
                    search_isexist = mtool.run_sql([
                        ['SELECT * FROM article_content WHERE id = %s', [id]]
                    ])
                    # 如果查询错误（应该不会），或者查询结果为 0，说明该行不存在
                    if search_isexist is False or len(search_isexist) <= 0:
                        return error_return("The article which id = [%s] doesn't exist!" % id)
                    else:
                        # 说明存在但不需要更新，直接返回即可（认为更新成功）
                        return success_return({
                            'id': search_isexist[0][0]
                        })
                else:
                    # 其他情况下，result 是触发更新的行数，一般是 1（因为只更新了一行）
                    return success_return()

    # 验证 content
    def verify_content(self, content):
        # content 上限不超过 2000，下限不能为空
        if len(content) > 2000:
            return "Too many words, the length must be less then 2000"
        elif len(content) <= 0:
            return "Content can't be empty!"
        else:
            return ''


if __name__ == '__main__':
    ac = ArticleController()
    print(ac.insert(content='abcdefg'))
    ac.select(id=1)
    print(ac.update(id=1, content='eeeee'))
