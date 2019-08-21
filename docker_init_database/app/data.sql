-- 创建数据库
CREATE DATABASE `article_system` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
-- 创建用户表
CREATE TABLE `user` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL DEFAULT '' COMMENT '用户名',
  `pw` varchar(32) NOT NULL DEFAULT '' COMMENT '密码，以sha1存储，加盐',
  `permission` tinyint(1) NOT NULL DEFAULT '0' COMMENT '权限，0未验证用户，1普通用户，2被封禁用户，10管理员',
  `status` tinyint(1) NOT NULL DEFAULT '0' COMMENT '账号状态，0启用，1禁用',
  `create_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `lastlogin_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '最近一次登录时间',
  `email` varchar(100) DEFAULT NULL COMMENT '注册邮箱',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `用户名` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPACT COMMENT='用户表';
-- 创建标签表
CREATE TABLE `tag` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `tag` varchar(20) NOT NULL DEFAULT '' COMMENT '标签文字，长度不超过20',
  `status` tinyint(3) DEFAULT '0' COMMENT '0启用1禁用，默认0',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='标签数据库';
-- 创建资料列表
CREATE TABLE `list` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `id_of_tags` varchar(255) DEFAULT NULL COMMENT '标签列表，标签以id形式存储，以英文逗号分隔',
  `content_id` int(11) DEFAULT '0' COMMENT '内容的id，内容存放在article_content这个表里',
  `create_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL COMMENT '最后更新时间（默认为空，为未编辑过）',
  `author` int(11) NOT NULL DEFAULT '0' COMMENT '发布人id',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='资料表，资料的正文都存这里';
-- 创建资料正文表
CREATE TABLE `article_content` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(2000) DEFAULT NULL COMMENT '内容',
  `status` tinyint(3) DEFAULT NULL COMMENT '0启用(默认)1禁用，即该资料是否可查阅',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='资料的正文';
