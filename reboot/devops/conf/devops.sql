CREATE TABLE `user` (
`id` int(10) unsigned NOT NULL AUTO_INCREMENT,
`username` varchar(40) NOT NULL COMMENT '用户名',
`password` varchar(64) NOT NULL COMMENT '密码',
`name` varchar(80) NOT NULL COMMENT '姓名',
`email` varchar(64) NOT NULL COMMENT '公司邮箱',
`mobile` varchar(16) COMMENT '手机号',
`r_id`  varchar(32)   NOT NULL COMMENT '角色id,允许多个r_id,存为字符串类型',      
`is_lock` tinyint(1) unsigned NOT NULL COMMENT '是否锁定 0-未锁定 1-锁定',
`join_date` datetime DEFAULT NULL COMMENT '注册时间',
`last_login` datetime DEFAULT NULL COMMENT '最后登录时间',
PRIMARY KEY (`id`),
UNIQUE 	KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


CREATE TABLE `role` (
`id` int(10) unsigned NOT NULL AUTO_INCREMENT,
`name` int(10)  NOT NULL COMMENT '角色名',
`p_id` int(10)  NOT NULL COMMENT '权限id，允许多个p_id,存为字符串类型',
`info` varchar(50) COMMENT '角色描述信息',
 PRIMARY  KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


CREATE TABLE `power` (
`id` int(10) unsigned NOT NULL AUTO_INCREMENT,
`name` varchar(32) NOT NULL COMMENT '权限英文名',
`name_cn` varchar(40) NOT NULL COMMENT '权限中文名',
`url` varchar(128) NOT NULL COMMENT '权限对应的url',
`comment` varchar(128) NOT NULL COMMENT '备注',
PRIMARY KEY (`id`),
UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


CREATE TABLE `project` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL COMMENT '项目名',
  `path` varchar(80) NOT NULL COMMENT '项目代码仓库路径',
  `principal` int(10) unsigned NOT NULL COMMENT '负责人',
  `create_date` date NOT NULL COMMENT '创建时间',
  `is_lock` tinyint(1) unsigned DEFAULT '0' COMMENT '是否锁定 0-未锁定 1-锁定',
  `comment` varchar(256) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


CREATE TABLE `project_test` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `project_id` int(10) NOT NULL COMMENT '对应project项目ID',
  `host` varchar(64) NOT NULL COMMENT '测试主机',
  `commit` varchar(64) NOT NULL COMMENT '推送版本号',
  `pusher` varchar(128) NOT NULL COMMENT '推送人',
  `push_date` datetime NOT NULL COMMENT '推送时间',
  `comment` varchar(256) COMMENT '备注',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


CREATE TABLE `project_apply` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `project_id` int(10) NOT NULL COMMENT '对应project项目ID',
  `info` varchar(64) NOT NULL COMMENT '发布简介',
  `applicant` varchar(64) NOT NULL COMMENT '申请人',
  `version` varchar(64) DEFAULT NULL COMMENT '发布版本',
  `commit` varchar(64) NOT NULL COMMENT '代码最新版本',
  `apply_date` datetime NOT NULL COMMENT '申请时间',
  `status` int(10) DEFAULT 0 COMMENT '发布状态',
  `detail` text COMMENT '发布详情',
  PRIMARY KEY (`id`),
  UNIQUE KEY `project_id` (`project_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

CREATE TABLE `project_deploy` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `project_id` int(10) NOT NULL COMMENT '对应project的项目ID',
  `info` varchar(64) NOT NULL COMMENT '发布简介',
  `version` varchar(64) DEFAULT NULL COMMENT '发布版本',
  `commit` varchar(64) NOT NULL COMMENT '代码最新版本',
  `applicant` varchar(64) NOT NULL COMMENT '操作人',
  `apply_date` datetime NOT NULL COMMENT '操作时间',
  `status` int(10) DEFAULT 0 COMMENT '发布状态',
  `detail` text COMMENT '发布详情',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
