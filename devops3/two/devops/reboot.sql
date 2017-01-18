-- MySQL dump 10.13  Distrib 5.1.73, for redhat-linux-gnu (x86_64)
--
-- Host: localhost    Database: reboot
-- ------------------------------------------------------
-- Server version	5.1.73

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `power`
--

DROP TABLE IF EXISTS `power`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `power` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL COMMENT '权限英文名',
  `name_cn` varchar(40) NOT NULL COMMENT '权限中文名',
  `url` varchar(128) NOT NULL COMMENT '权限对应的url',
  `comment` varchar(128) NOT NULL COMMENT '备注',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `power`
--

LOCK TABLES `power` WRITE;
/*!40000 ALTER TABLE `power` DISABLE KEYS */;
INSERT INTO `power` VALUES (4,'git','git仓库','/project/project','测试'),(3,'cdn','cdn刷新接口','/api','cdn刷新测试'),(6,'zabbix','监控','/zabbix','监控管理平台11'),(8,'testing','测试发布','/project/testing','代码测试发布'),(9,'apply','申请发布','/project/apply','申请发布'),(10,'deploy','发布列表','/project/deploy','发布列表'),(13,'applylist','申请列表','/project/applylist','查看并处理申请发布的项目'),(16,'devops','运维开发','sdafs','fasdf');
/*!40000 ALTER TABLE `power` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `project` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL COMMENT '项目名',
  `path` varchar(128) NOT NULL COMMENT '项目代码仓库路径',
  `principal` varchar(32) NOT NULL COMMENT '负责人',
  `p_user` varchar(32) DEFAULT NULL COMMENT '有权限的用户',
  `p_group` varchar(32) DEFAULT NULL COMMENT '有权限的组',
  `create_date` date NOT NULL COMMENT '创建时间',
  `is_lock` tinyint(1) unsigned DEFAULT '0' COMMENT '是否锁定 0-未锁定 1-锁定',
  `comment` varchar(256) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
INSERT INTO `project` VALUES (1,'test','test','2','3','1,6,7','2016-04-18',0,'testdsds'),(3,'devops','test111','3','21','9,10','2016-04-19',0,'testssdads'),(4,'gitolite-admin','gitolite-admin','1','1','1,6,7','2016-04-23',0,'管理仓库'),(5,'reboot','reboot','3','2,7','1,6','2016-04-24',0,'test'),(6,'test1','test','1','2','7','2016-07-17',0,'nihaosdsdssdsd'),(7,'devops2','http:///dsdsd','2','1,2,3','1,6,7','2016-07-17',0,'just+a+testsdad'),(17,'fdsafa','fasdfas','3','2,3','6','2016-07-31',0,'fsadfas'),(18,'sdad','dadsad','2','2','7','2016-07-31',0,'sad'),(19,'sdadsdsds','dadsad','1,15','2','1,7','2016-07-31',0,'sad'),(20,'adadsadas','sa','1,15,21','2,21','7','2016-07-31',0,'sad'),(21,'aaa','aa','2','1,3','7,9','2016-08-06',0,'aa'),(22,'sadfasf','fadsfa','1','2','7','2016-09-11',0,'fsadfa'),(23,'1111','1111','2','3','1','2016-11-19',0,'11'),(24,'fdasfsafs','fasdfasf','2','2','7','2016-11-20',0,'fdsafsaf'),(25,'2323','323232','2','24','10','2016-11-20',0,'32323');
/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project_apply`
--

DROP TABLE IF EXISTS `project_apply`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `project_apply` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `project_id` int(10) NOT NULL COMMENT '对应project项目ID',
  `info` varchar(64) NOT NULL COMMENT '发布简介',
  `applicant` varchar(64) NOT NULL COMMENT '申请人',
  `version` varchar(64) DEFAULT NULL COMMENT '发布版本',
  `commit` varchar(64) NOT NULL COMMENT '代码最新版本',
  `apply_date` datetime NOT NULL COMMENT '申请时间',
  `status` int(10) DEFAULT '0' COMMENT '发布状态',
  `detail` text COMMENT '发布详情',
  PRIMARY KEY (`id`),
  UNIQUE KEY `project_id` (`project_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_apply`
--

LOCK TABLES `project_apply` WRITE;
/*!40000 ALTER TABLE `project_apply` DISABLE KEYS */;
INSERT INTO `project_apply` VALUES (1,1,'速度是多少','admin','aa','11111','2016-06-26 09:38:00',3,'实打实'),(2,3,'nihao','admin','vsdsds','11111','2016-07-31 18:00:00',1,'nihao'),(3,5,'DD','admin','111','11111','2016-04-24 16:36:00',3,'DD'),(4,4,'等等','admin',NULL,'11111','2016-05-22 10:13:00',3,'等等'),(5,7,'aa','admin','version0.11','11111','2016-08-06 09:22:00',1,'aa'),(7,21,'dsafs','bbbbb','dsafsaf','11111','2016-11-20 10:07:00',4,'fdsafsaf'),(6,20,'adsas','admin','dasd','11111','2016-07-31 17:55:00',3,'asd'),(8,17,'111','kk',NULL,'11111','2016-08-13 20:25:00',3,'111'),(9,23,'','admin','dfsafaf','11111','2016-11-20 11:44:00',1,'');
/*!40000 ALTER TABLE `project_apply` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project_deploy`
--

DROP TABLE IF EXISTS `project_deploy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `project_deploy` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `project_id` int(10) NOT NULL COMMENT '对应project的项目ID',
  `info` varchar(64) NOT NULL COMMENT '发布简介',
  `version` varchar(64) DEFAULT NULL COMMENT '发布版本',
  `commit` varchar(64) NOT NULL COMMENT '代码最新版本',
  `applicant` varchar(64) NOT NULL COMMENT '操作人',
  `apply_date` datetime NOT NULL COMMENT '操作时间',
  `status` int(10) DEFAULT '0' COMMENT '发布状态',
  `detail` text COMMENT '发布详情',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=125 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_deploy`
--

LOCK TABLES `project_deploy` WRITE;
/*!40000 ALTER TABLE `project_deploy` DISABLE KEYS */;
INSERT INTO `project_deploy` VALUES (1,1,'nih',NULL,'11111','admin','2016-04-21 21:05:00',1,'dsdsd'),(2,3,'nihao+',NULL,'11111','admin','2016-04-21 21:16:00',1,'nihao'),(3,3,'nihao+','','11111','admin','2016-04-21 21:16:00',4,'nihao'),(28,3,'111','v0.1','11111','admin','2016-04-22 11:46:00',3,'111'),(7,1,'nih','11111','11111','admin','2016-04-21 21:05:00',2,'dsdsd'),(8,1,'nih','11111','11111','admin','2016-04-21 21:05:00',3,'dsdsd'),(9,3,'你好',NULL,'11111','admin','2016-04-22 00:09:00',1,'测试'),(27,3,'111','v0.1','11111','admin','2016-04-22 11:46:00',2,'111'),(13,3,'你好','v0.q1','11111','admin','2016-04-22 00:09:00',2,'测试'),(14,3,'你好','v0.q1','11111','admin','2016-04-22 00:09:00',3,'测试'),(15,3,'你好','v0.q1','11111','admin','2016-04-22 00:09:00',3,'测试'),(16,3,'你好','v0.q1','11111','admin','2016-04-22 00:09:00',3,'测试'),(17,3,'你好','v0.q1','11111','admin','2016-04-22 00:09:00',3,'测试'),(18,3,'你好','v0.q1','11111','admin','2016-04-22 00:09:00',3,'测试'),(19,3,'你好','v0.q1','11111','admin','2016-04-22 00:09:00',4,'测试'),(20,1,'sdsds',NULL,'11111','admin','2016-04-22 00:17:00',1,'dsds'),(21,1,'sdsds','vsd','11111','admin','2016-04-22 00:17:00',2,'dsds'),(22,1,'sdsds','vsd','11111','admin','2016-04-22 00:17:00',3,'dsds'),(23,3,'dssd',NULL,'11111','admin','2016-04-22 00:20:00',1,'sds'),(24,3,'dssd','sdsd','11111','admin','2016-04-22 00:20:00',2,'sds'),(25,3,'dssd','sdsd','11111','admin','2016-04-22 00:20:00',3,'sds'),(26,3,'111',NULL,'11111','admin','2016-04-22 11:46:00',1,'111'),(29,1,'nihao+',NULL,'11111','rock','2016-04-23 12:25:00',1,'nihao'),(30,1,'nihao+','v1.0','11111','rock','2016-04-23 12:25:00',2,'nihao'),(31,1,'nihao+','v1.0','11111','rock','2016-04-23 12:25:00',4,'nihao'),(32,1,'nihao+','v1.0','11111','rock','2016-04-23 12:25:00',4,'nihao'),(33,1,'nihao+','v1.0','11111','rock','2016-04-23 12:25:00',4,'nihao'),(34,1,'test',NULL,'11111','rock','2016-04-23 12:26:00',1,'test'),(35,1,'test','12','11111','rock','2016-04-23 12:26:00',2,'test'),(36,1,'test','12','11111','rock','2016-04-23 12:26:00',4,'test'),(37,1,'nihaodd',NULL,'11111','rock','2016-04-23 13:24:00',1,'nih'),(38,1,'nihaodd','12','11111','rock','2016-04-23 13:24:00',3,'nih'),(39,1,'sss',NULL,'11111','rock','2016-04-23 13:24:00',1,'ss'),(40,1,'sss','sss','11111','rock','2016-04-23 13:24:00',2,'ss'),(41,1,'sss','sss','11111','rock','2016-04-23 13:24:00',4,'ss'),(42,1,'dssd',NULL,'11111','rock','2016-04-23 13:29:00',1,'sds'),(43,1,'dssd','v0.q1','11111','rock','2016-04-23 13:29:00',2,'sds'),(44,1,'dssd','v0.q1','11111','rock','2016-04-23 13:29:00',4,'sds'),(45,3,'test',NULL,'11111','admin','2016-04-24 15:01:00',1,'aaaa'),(46,3,'test','v0.1','11111','admin','2016-04-24 15:01:00',3,'aaaa'),(47,3,'test',NULL,'11111','admin','2016-04-24 15:06:00',1,'test'),(48,3,'test','version0.1','11111','admin','2016-04-24 15:06:00',2,'test'),(49,3,'test','version0.1','11111','admin','2016-04-24 15:06:00',4,'test'),(50,3,'ddd',NULL,'11111','admin','2016-04-24 15:48:00',1,'dddd'),(51,1,'nihao',NULL,'11111','admin','2016-04-24 16:03:00',1,'nihao'),(52,3,'ddd','version0.1','11111','admin','2016-04-24 15:48:00',3,'dddd'),(53,5,'nihao',NULL,'11111','admin','2016-04-24 16:05:00',1,'test'),(54,5,'nihao','','11111','admin','2016-04-24 16:05:00',3,'test'),(55,1,'nihao','aa','11111','admin','2016-04-24 16:03:00',2,'nihao'),(56,3,'fgfff',NULL,'11111','admin','2016-04-24 16:33:00',1,'ghgg'),(57,3,'fgfff','vvv','11111','admin','2016-04-24 16:33:00',2,'ghgg'),(58,1,'nihao','aa','11111','admin','2016-04-24 16:03:00',3,'nihao'),(59,5,'DD',NULL,'11111','admin','2016-04-24 16:36:00',1,'DD'),(60,3,'fgfff','vvv','11111','admin','2016-04-24 16:33:00',4,'ghgg'),(61,3,'特务+v',NULL,'11111','admin','2016-05-22 10:13:00',1,'特特'),(62,4,'等等',NULL,'11111','admin','2016-05-22 10:13:00',1,'等等'),(63,3,'特务+v','111','11111','admin','2016-05-22 10:13:00',2,'特特'),(64,3,'特务+v','111','11111','admin','2016-05-22 10:13:00',4,'特特'),(65,3,'qqq',NULL,'11111','admin','2016-06-25 23:16:00',1,'qqq'),(66,3,'qqq','sss','11111','admin','2016-06-25 23:16:00',2,'qqq'),(67,1,'速度是多少',NULL,'11111','admin','2016-06-26 09:38:00',1,'实打实'),(68,5,'DD','111','11111','admin','2016-04-24 16:36:00',2,'DD'),(69,3,'qqq','sss','11111','admin','2016-06-25 23:16:00',3,'qqq'),(70,7,'测试',NULL,'11111','admin','2016-07-17 14:01:00',1,'测试'),(71,3,'你好',NULL,'11111','admin','2016-07-17 14:03:00',1,'你好'),(72,3,'你好','sss','11111','admin','2016-07-17 14:03:00',3,'你好'),(73,7,'测试','version0.11','11111','admin','2016-07-17 14:01:00',2,'测试'),(74,7,'测试','version0.11','11111','admin','2016-07-17 14:01:00',4,'测试'),(75,3,'nihao+',NULL,'11111','admin','2016-07-28 23:15:00',1,'nihao'),(76,3,'nihao+','vsdad','11111','admin','2016-07-28 23:15:00',2,'nihao'),(77,3,'nihao+','vsdad','11111','admin','2016-07-28 23:15:00',4,'nihao'),(78,4,'等等','','11111','admin','2016-05-22 10:13:00',3,'等等'),(79,3,'sdafa',NULL,'11111','admin','2016-07-28 23:18:00',1,'dafasf'),(80,3,'sdafa','sdsd','11111','admin','2016-07-28 23:18:00',2,'dafasf'),(81,3,'sdafa','sdsd','11111','admin','2016-07-28 23:18:00',4,'dafasf'),(82,1,'速度是多少','aa','11111','admin','2016-06-26 09:38:00',3,'实打实'),(83,3,'sadfa',NULL,'11111','admin','2016-07-31 09:26:00',1,'fdsaf'),(84,3,'sadfa','vsdsds','11111','admin','2016-07-31 09:26:00',2,'fdsaf'),(85,5,'DD','111','11111','admin','2016-04-24 16:36:00',3,'DD'),(86,3,'sadfa','vsdsds','11111','admin','2016-07-31 09:26:00',4,'fdsaf'),(87,20,'just+a+test',NULL,'11111','admin','2016-07-31 17:36:00',1,'sdsds'),(88,20,'just+a+test','version0.1','11111','admin','2016-07-31 17:36:00',2,'sdsds'),(89,20,'just+a+test','version0.1','11111','admin','2016-07-31 17:36:00',3,'sdsds'),(90,20,'fasdfasfd',NULL,'11111','admin','2016-07-31 17:43:00',1,'asdfasf'),(91,20,'fasdfasfd','sadfa','11111','admin','2016-07-31 17:43:00',2,'asdfasf'),(92,20,'fasdfasfd','sadfa','11111','admin','2016-07-31 17:43:00',4,'asdfasf'),(93,20,'adsas',NULL,'11111','admin','2016-07-31 17:55:00',1,'asd'),(94,20,'adsas','dasd','11111','admin','2016-07-31 17:55:00',2,'asd'),(95,3,'nihao',NULL,'11111','admin','2016-07-31 18:00:00',1,'nihao'),(96,7,'aa',NULL,'11111','admin','2016-08-06 09:22:00',1,'aa'),(97,21,'s11111',NULL,'11111','admin','2016-08-06 09:54:00',1,'111'),(98,21,'s11111','v1.10','11111','admin','2016-08-06 09:54:00',2,'111'),(99,21,'s11111','v1.10','11111','admin','2016-08-06 09:54:00',4,'111'),(100,21,'sds',NULL,'11111','kk','2016-08-13 20:18:00',1,'sdsd'),(101,17,'111',NULL,'11111','kk','2016-08-13 20:25:00',1,'111'),(102,21,'sds','vvdd','11111','kk','2016-08-13 20:18:00',2,'sdsd'),(103,21,'sds','vvdd','11111','kk','2016-08-13 20:18:00',2,'sdsd'),(104,21,'sds','vvdd','11111','kk','2016-08-13 20:18:00',4,'sdsd'),(105,21,'',NULL,'11111','admin','2016-08-18 10:50:00',1,''),(106,21,'','vvdd','11111','admin','2016-08-18 10:50:00',3,''),(107,21,'这是一个测试',NULL,'11111','admin','2016-08-18 10:52:00',1,'这是一个测试'),(108,21,'这是一个测试','v0.3','11111','admin','2016-08-18 10:52:00',2,'这是一个测试'),(109,21,'这是一个测试','v0.3','11111','admin','2016-08-18 10:52:00',4,'这是一个测试'),(110,21,'test',NULL,'11111','admin','2016-09-10 10:13:00',1,'test'),(111,21,'test','ss','11111','admin','2016-09-10 10:13:00',2,'test'),(112,21,'test','ss','11111','admin','2016-09-10 10:13:00',4,'test'),(113,21,'fsadfsaf',NULL,'11111','admin','2016-09-11 11:53:00',1,'fasdfsa'),(114,21,'fsadfsaf','version0.1sdfs','11111','admin','2016-09-11 11:53:00',2,'fasdfsa'),(115,21,'fsadfsaf','version0.1sdfs','11111','admin','2016-09-11 11:53:00',4,'fasdfsa'),(116,20,'adsas','dasd','11111','admin','2016-07-31 17:55:00',3,'asd'),(117,17,'111','','11111','kk','2016-08-13 20:25:00',3,'111'),(118,21,'dsafs',NULL,'11111','bbbbb','2016-11-20 10:07:00',1,'fdsafsaf'),(119,21,'dsafs','dsafsaf','11111','bbbbb','2016-11-20 10:07:00',2,'fdsafsaf'),(120,21,'dsafs','dsafsaf','11111','bbbbb','2016-11-20 10:07:00',4,'fdsafsaf'),(121,23,'dfasdf',NULL,'11111','admin','2016-11-20 10:16:00',1,'fasdfsaf'),(122,23,'dfasdf','dfsafaf','11111','admin','2016-11-20 10:16:00',2,'fasdfsaf'),(123,23,'dfasdf','dfsafaf','11111','admin','2016-11-20 10:16:00',3,'fasdfsaf'),(124,23,'',NULL,'11111','admin','2016-11-20 11:44:00',1,'');
/*!40000 ALTER TABLE `project_deploy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project_test`
--

DROP TABLE IF EXISTS `project_test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `project_test` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `project_id` int(10) NOT NULL COMMENT '对应project项目ID',
  `host` varchar(64) NOT NULL COMMENT '测试主机',
  `commit` varchar(64) NOT NULL COMMENT '推送版本号',
  `pusher` varchar(128) NOT NULL COMMENT '推送人',
  `push_date` datetime NOT NULL COMMENT '推送时间',
  `comment` varchar(256) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_test`
--

LOCK TABLES `project_test` WRITE;
/*!40000 ALTER TABLE `project_test` DISABLE KEYS */;
/*!40000 ALTER TABLE `project_test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL COMMENT 'è§’è‰²å',
  `name_cn` varchar(40) NOT NULL COMMENT 'è§’è‰²ä¸­æ–‡å',
  `p_id` varchar(20) NOT NULL COMMENT 'æƒé™idï¼Œå…è®¸å¤šä¸ªp_id,å­˜ä¸ºå­—ç¬¦ä¸²ç±»åž‹',
  `info` varchar(50) DEFAULT NULL COMMENT 'è§’è‰²æè¿°ä¿¡æ¯',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (1,'sa','运维组','4,3,6,7,8,9,10,13','超级管理员'),(17,'test','从测试','4','测试'),(7,'php','开发组','4,6,8,9,10','PHP开发'),(9,'ios','苹果开发组','4,8,24','苹果开发组'),(10,'devops','运维研发','4,3,6,13,16','运维研发组');
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(40) NOT NULL COMMENT '用户名',
  `password` varchar(64) NOT NULL COMMENT '密码',
  `name` varchar(80) NOT NULL COMMENT '姓名',
  `email` varchar(64) NOT NULL COMMENT '公司邮箱',
  `mobile` varchar(16) DEFAULT NULL COMMENT '手机号',
  `r_id` varchar(32) NOT NULL COMMENT '角色id,允许多个r_id,存为字符串类型',
  `is_lock` tinyint(1) unsigned NOT NULL COMMENT '是否锁定 0-未锁定 1-锁定',
  `join_date` datetime DEFAULT NULL COMMENT '注册时间',
  `last_login` datetime DEFAULT NULL COMMENT '最后登录时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'admin','e10adc3949ba59abbe56e057f20f883e','admin','787696331@qq.com','183105199111','1,7,10',0,NULL,'2016-12-01 21:47:26'),(2,'wd','e10adc3949ba59abbe56e057f20f883e','卧底','787696331@123.com','121212121s','1,12',0,'2016-04-11 23:24:04','2016-08-13 10:11:44'),(3,'pc','e10adc3949ba59abbe56e057f20f883e','你好啊','787696331@qq.com','18310519911','16,7',0,'2016-04-11 23:26:51','2016-12-01 19:24:46'),(7,'kk','e10adc3949ba59abbe56e057f20f883e','kk','7896331@qq.com','182104199222','1,6,7',0,'2016-04-13 14:53:33','2016-08-13 20:53:13'),(6,'panda','e10adc3949ba59abbe56e057f20f883e','panda','787696331@qq.com','121212121','1,7,10',0,'2016-04-12 23:23:50','2016-04-22 17:04:27'),(15,'rock','e10adc3949ba59abbe56e057f20f883e','峻峰','777@111111.com','18210510011','1,6,7,10',0,'2016-04-17 10:10:49','2016-04-23 12:21:59'),(22,'qicheng','e10adc3949ba59abbe56e057f20f883e','qicheng','787696331@qq.com','121212121','10',0,'2016-10-22 17:01:02',NULL),(28,'aaaaa','96e79218965eb72c92a549dd5a330112','你好','1111@reboot.com','18310419933','1,17,7,10',0,'2016-12-01 21:12:18',NULL),(24,'bbbbb','e10adc3949ba59abbe56e057f20f883e','你好吗','111@reboot.com','18310419933','7,9',0,'2016-11-20 10:04:01','2016-11-27 16:43:08');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-12-01 21:57:11
