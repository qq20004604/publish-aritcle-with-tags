use mysql;
select host, user from user;
-- 任意地点的root账号可以用一个非常复杂的密码登录（瞎打的），用于禁止无密码登录
GRANT ALL ON *.* to root@'%' identified by 'abcd1235ojpibetbenoinwef' with grant option;
-- 允许root用户以密码 123456 来登录（仅限本地）
GRANT ALL ON *.* to root@'localhost' identified by '123456' with grant option;
-- mysql新设置用户或权限后需要刷新系统权限否则可能会出现拒绝访问：
FLUSH PRIVILEGES;