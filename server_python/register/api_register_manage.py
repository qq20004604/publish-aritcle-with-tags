#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .forms import UserForm
import time
import json
from decorator_csrf_setting import my_csrf_decorator
from md5_lingling import Md5Tool
from mysql_lingling import MySQLTool
from config.mysql_options import mysql_config
from response_data import get_res_json
from session_manage import SessionManage
from config.development_config import IS_ON_WEBPACK_DEVELOPMENT
from get_time import get_date_time


# 登录验证
@my_csrf_decorator()
def register(request):
    # 获取当前时间
    nowtime = get_date_time()
    print(nowtime)

    if request.method != 'POST':
        return get_res_json(code=0, msg="请通过POST请求来进行登陆")

    data = json.loads(request.body)
    uf = UserForm(data)
    # 验证不通过，返回错误信息
    if not uf.is_valid():
        msg = uf.get_form_error_msg()
        return get_res_json(code=0, msg=msg)

    username = data.get('username')
    password = data.get('password')
    email = data.get('email', '')
    print(username, password, email)

    tool = Md5Tool()
    md5pw = tool.get_md5(password)

    print(md5pw)

    # 连接数据库
    with MySQLTool(host=mysql_config['host'],
                   user=mysql_config['user'],
                   password=mysql_config['pw'],
                   database=mysql_config['database']) as mtool:
        # 查看有没有同名的用户
        result = mtool.run_sql([
            ['select (name) from developer_info where name = %s', [username]]
        ])
        # 打印结果e
        print(result)
        # 判定密码是否相等
        if len(result) > 0:
            return get_res_json(code=0, msg="该用户名已注册，请更换用户名")

        # 插入
        row_id = mtool.insert_row(
            'INSERT developer_info'
            '(id, name, pw, permission, status, create_time, lastlogin_time, email) VALUES'
            '(%s, %s,   %s, 3,          0,      %s,          %s,             %s)',
            [
                None,
                username,
                md5pw,
                nowtime,
                nowtime,
                email
            ]
        )

        if row_id is False:
            return get_res_json(code=0, msg='注册失败')

        sm = SessionManage(request.session)
        sm.set_login([row_id, username, '', 3, 0, nowtime, nowtime, email])

        return get_res_json(code=200, data={
            'msg': '用户注册成功，正在跳转中...',
            'redirecturl': '/home' if not IS_ON_WEBPACK_DEVELOPMENT else '/home.html',
        })
