#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .forms import UserForm
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
def login(request):
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

    username = data.get('username', '')
    password = data.get('password', '')
    print(username, password)
    tool = Md5Tool()
    md5pw = tool.get_md5(password)
    print(md5pw)
    # 连接数据库
    with MySQLTool(host=mysql_config['host'],
                   user=mysql_config['user'],
                   password=mysql_config['pw'],
                   database=mysql_config['database']) as mtool:
        # 执行sql并获得返回结果
        result = mtool.run_sql([
            ['select * from developer_info where name = %s', [username]]
        ])
        # 打印结果e
        print(result)
        # 判定密码是否相等
        if len(result) > 0:
            if md5pw == result[0][2]:
                # 再判定该用户状态是否正常
                if result[0][4] != 0:
                    return get_res_json(code=0, msg="该用户禁止登陆")

                sm = SessionManage(request.session)
                sm.set_login(result[0])
                # 更新登陆时间
                mtool.update_row(
                    'UPDATE developer_info SET lastlogin_time = %s WHERE name = %s',
                    [
                        nowtime,
                        username
                    ]
                )
                return get_res_json(
                    data={
                        'redirecturl': '/home' if not IS_ON_WEBPACK_DEVELOPMENT else '/home.html',
                        'msg': '登陆成功'
                    })
            else:
                return get_res_json(code=0, msg="密码错误")
        else:
            return get_res_json(code=0, msg="不存在该用户")


# 登出
@my_csrf_decorator()
def logout(request):
    sm = SessionManage(request.session)
    try:
        sm.logout()
        return get_res_json(
            data={'redirecturl': '/' if not IS_ON_WEBPACK_DEVELOPMENT else '/login.html', 'msg': '登出成功'})
    except BaseException as e:
        print(e)
        return get_res_json(code=0, msg="登出失败")
