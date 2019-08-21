#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

# 初始化数据库（这里是使用 sqlite3 存储非业务数据）
init_sql = 'python manage.py migrate'
info = os.popen(init_sql).readlines()
print(info)

# 测试和示例代码
if __name__ == '__main__':
    pass
