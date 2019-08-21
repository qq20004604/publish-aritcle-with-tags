#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from form import Form, forms


class UserForm(Form):
    username = forms.CharField(label='username',
                               min_length=8,
                               max_length=40,
                               error_messages={
                                   'required': '你没有填写账号',
                                   'max_length': '账号长度需要在8~40位之间',
                                   'min_length': '账号长度需要在8~40位之间'
                               }
                               )
    password = forms.CharField(label='password',
                               min_length=8,
                               max_length=40,
                               error_messages={
                                   'required': '你没有填写密码',
                                   'max_length': '密码长度需要在8~40位之间',
                                   'min_length': '密码长度需要在8~40位之间'
                               }
                               )
    email = forms.CharField(label='email',
                            initial='',
                            max_length=100,
                            required=False,
                            error_messages={
                                'max_length': '邮箱长度不应大于255'
                            })
