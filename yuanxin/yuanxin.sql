-- MySQL dump 10.13  Distrib 5.1.73, for redhat-linux-gnu (x86_64)
--
-- Host: localhost    Database: yuanxin
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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (10,'php'),(9,'sa');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (17,10,28),(18,10,26),(19,10,29),(16,10,31),(15,9,16),(13,9,18),(14,9,17);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=49 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(23,'Can add content type',4,'add_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add profile',6,'add_userprofile'),(17,'Can change profile',6,'change_userprofile'),(18,'Can delete profile',6,'delete_userprofile'),(24,'Can change content type',4,'change_contenttype'),(25,'Can delete content type',4,'delete_contenttype'),(26,'Can add workorder',7,'add_workorder'),(27,'Can deal workorder',7,'deal_workorder'),(28,'Can see workorder',7,'view_workorder'),(29,'Can apply deploy',8,'apply_deploy'),(30,'Can deal deploy',8,'deal_deploy'),(31,'Can see deploy',8,'history_deploy'),(32,'Can change work_order',7,'change_workorder'),(33,'Can delete work_order',7,'delete_workorder'),(34,'Can add deploy',8,'add_deploy'),(35,'Can change deploy',8,'change_deploy'),(36,'Can delete deploy',8,'delete_deploy'),(37,'Can add idc',9,'add_idc'),(38,'Can change idc',9,'change_idc'),(39,'Can delete idc',9,'delete_idc'),(40,'Can add status',10,'add_status'),(41,'Can change status',10,'change_status'),(42,'Can delete status',10,'delete_status'),(43,'Can add product',11,'add_product'),(44,'Can change product',11,'change_product'),(45,'Can delete product',11,'delete_product'),(46,'Can add server',12,'add_server'),(47,'Can change server',12,'change_server'),(48,'Can delete server',12,'delete_server');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `code_release_deploy`
--

DROP TABLE IF EXISTS `code_release_deploy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `code_release_deploy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  `project_version` varchar(40) NOT NULL,
  `version_desc` varchar(100) NOT NULL,
  `applicant_id` int(11) NOT NULL,
  `update_detail` longtext NOT NULL,
  `is_version_back` tinyint(1) NOT NULL,
  `status` int(11) NOT NULL,
  `apply_time` datetime NOT NULL,
  `deploy_time` datetime NOT NULL,
  `assigned_to_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `code_release_deploy_02c1725c` (`assigned_to_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `code_release_deploy`
--

LOCK TABLES `code_release_deploy` WRITE;
/*!40000 ALTER TABLE `code_release_deploy` DISABLE KEYS */;
INSERT INTO `code_release_deploy` VALUES (2,'devops','V0.2','第二个版本',1,'aa',0,2,'2017-05-31 19:32:29','2017-05-31 19:35:06',1),(3,'devops','V0.1','第一个项目',1,'aa',0,2,'2017-05-31 19:36:35','2017-06-01 10:53:03',1),(4,'devops','V0.2','第二个版本',1,'aa',0,3,'2017-06-01 10:53:32','2017-06-01 10:53:32',1),(10,'devops','V0.2','第二个版本',11,'aa',0,0,'2017-06-05 18:40:21','2017-06-05 18:40:21',1),(7,'devops','V0.2','第二个版本',1,'aa',0,3,'2017-06-01 14:17:12','2017-06-01 14:17:12',1),(8,'devops','V0.1','第一个项目',1,'aa',0,3,'2017-06-01 14:18:11','2017-06-01 14:18:11',1),(9,'devops','V0.2','第二个版本',1,'dddd',0,2,'2017-06-01 14:45:42','2017-06-05 18:19:29',1);
/*!40000 ALTER TABLE `code_release_deploy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dashboard_userprofile`
--

DROP TABLE IF EXISTS `dashboard_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dashboard_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  `name` varchar(30) NOT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `wechat` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dashboard_userprofile`
--

LOCK TABLES `dashboard_userprofile` WRITE;
/*!40000 ALTER TABLE `dashboard_userprofile` DISABLE KEYS */;
INSERT INTO `dashboard_userprofile` VALUES (1,'pbkdf2_sha256$20000$vcIuPQKKyNbQ$XkcKr9Ryi2PHBsZ1n77hqUSDXDvcZbNaTXtZ1rhuhV4=','2017-06-09 10:20:13',1,'admin','','','admin@163.com',1,1,'2017-05-25 07:55:19','admin','18310519941',NULL),(11,'pbkdf2_sha256$20000$t3WJt8a0cMO0$Amy2NQkD2+BL8JZBxLZfci4ng2UvtiHCNHjK4mIq7Bk=','2017-06-06 14:40:16',0,'liuziping','','','787696331@qq.com',0,1,'2017-06-04 22:16:39','zp','18210519911',NULL),(12,'pbkdf2_sha256$20000$CAZksxTABctb$zIUiXds6LUSiRuHQpG5JeisEyqu0FwMwqZefyE3plX8=','2017-06-06 15:49:14',0,'panda','','','787696331@qq.com',0,1,'2017-06-06 14:57:11','panda','18310519941',NULL);
/*!40000 ALTER TABLE `dashboard_userprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dashboard_userprofile_groups`
--

DROP TABLE IF EXISTS `dashboard_userprofile_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dashboard_userprofile_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `userprofile_id` (`userprofile_id`,`group_id`),
  KEY `dashboard_userprofile_groups_9c2a73e9` (`userprofile_id`),
  KEY `dashboard_userprofile_groups_0e939a4f` (`group_id`)
) ENGINE=MyISAM AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dashboard_userprofile_groups`
--

LOCK TABLES `dashboard_userprofile_groups` WRITE;
/*!40000 ALTER TABLE `dashboard_userprofile_groups` DISABLE KEYS */;
INSERT INTO `dashboard_userprofile_groups` VALUES (22,11,9),(20,1,9),(23,12,10);
/*!40000 ALTER TABLE `dashboard_userprofile_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dashboard_userprofile_user_permissions`
--

DROP TABLE IF EXISTS `dashboard_userprofile_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dashboard_userprofile_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `userprofile_id` (`userprofile_id`,`permission_id`),
  KEY `dashboard_userprofile_user_permissions_9c2a73e9` (`userprofile_id`),
  KEY `dashboard_userprofile_user_permissions_8373b171` (`permission_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dashboard_userprofile_user_permissions`
--

LOCK TABLES `dashboard_userprofile_user_permissions` WRITE;
/*!40000 ALTER TABLE `dashboard_userprofile_user_permissions` DISABLE KEYS */;
INSERT INTO `dashboard_userprofile_user_permissions` VALUES (3,1,7);
/*!40000 ALTER TABLE `dashboard_userprofile_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','permission'),(3,'auth','group'),(4,'contenttypes','contenttype'),(5,'sessions','session'),(6,'dashboard','userprofile'),(7,'work_order','workorder'),(8,'code_release','deploy'),(9,'server','idc'),(10,'server','status'),(11,'server','product'),(12,'server','server');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2017-05-25 03:36:17'),(2,'admin','0001_initial','2017-05-25 03:36:17'),(3,'contenttypes','0002_remove_content_type_name','2017-05-25 03:36:17'),(4,'auth','0001_initial','2017-05-25 03:36:17'),(5,'auth','0002_alter_permission_name_max_length','2017-05-25 03:36:17'),(6,'auth','0003_alter_user_email_max_length','2017-05-25 03:36:17'),(7,'auth','0004_alter_user_username_opts','2017-05-25 03:36:17'),(8,'auth','0005_alter_user_last_login_null','2017-05-25 03:36:17'),(9,'auth','0006_require_contenttypes_0002','2017-05-25 03:36:17'),(10,'sessions','0001_initial','2017-05-25 03:36:17'),(11,'dashboard','0001_initial','2017-05-25 04:02:10'),(12,'work_order','0001_initial','2017-05-27 03:35:42'),(13,'work_order','0002_auto_20170527_1136','2017-05-27 03:36:41'),(14,'code_release','0001_initial','2017-05-30 23:04:17'),(15,'server','0001_initial','2017-06-07 18:20:29');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('lgtwd0utf9d9t4qerf1vje2ok2vp2bnp','YjQwMTAxY2E4YzUxOWQ5NWM5MjVlOWEwMTM2YWFmOGQ0NzRiZWQ3MDp7Il9hdXRoX3VzZXJfaGFzaCI6IjU1N2NmMDY3NDg2YTRhMTdiMGI0ODA2NThlYzU1NDAyZmQyMzQwZmQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-06-21 17:10:18'),('l9pc5wgmqkz3g78115ngr0jnrpwdmlan','NjYxYmU4ODc1NWY4MmMxZGYyMDNmNWUxOWUzMjAxMzYxZDNjYzJmMjp7Il9hdXRoX3VzZXJfaGFzaCI6IjVhYjA4MzQ1YzNkODRmMDQ4NjM5MzhjMDAzOTgzMTZiMDg0YjlhZWUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-06-12 15:56:29'),('2on2613c5ky9ukgwaf6r5bf5pgal0m2t','YjQwMTAxY2E4YzUxOWQ5NWM5MjVlOWEwMTM2YWFmOGQ0NzRiZWQ3MDp7Il9hdXRoX3VzZXJfaGFzaCI6IjU1N2NmMDY3NDg2YTRhMTdiMGI0ODA2NThlYzU1NDAyZmQyMzQwZmQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-06-19 22:42:26'),('zz8or52081ylbsxqy934zmsa08aweq9r','YjQwMTAxY2E4YzUxOWQ5NWM5MjVlOWEwMTM2YWFmOGQ0NzRiZWQ3MDp7Il9hdXRoX3VzZXJfaGFzaCI6IjU1N2NmMDY3NDg2YTRhMTdiMGI0ODA2NThlYzU1NDAyZmQyMzQwZmQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-06-22 09:14:51'),('snx24bv0vo7om23v4sntpt6xturw186e','YjQwMTAxY2E4YzUxOWQ5NWM5MjVlOWEwMTM2YWFmOGQ0NzRiZWQ3MDp7Il9hdXRoX3VzZXJfaGFzaCI6IjU1N2NmMDY3NDg2YTRhMTdiMGI0ODA2NThlYzU1NDAyZmQyMzQwZmQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-06-23 10:17:24'),('f06a1l5y74gjfnyjtuo2bxzq85i70eb2','YjQwMTAxY2E4YzUxOWQ5NWM5MjVlOWEwMTM2YWFmOGQ0NzRiZWQ3MDp7Il9hdXRoX3VzZXJfaGFzaCI6IjU1N2NmMDY3NDg2YTRhMTdiMGI0ODA2NThlYzU1NDAyZmQyMzQwZmQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-06-23 10:20:13');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `idc`
--

DROP TABLE IF EXISTS `idc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `idc` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  `idc_name` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `user` varchar(32) NOT NULL,
  `user_phone` varchar(20) NOT NULL,
  `user_email` varchar(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `idc_name` (`idc_name`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `idc`
--

LOCK TABLES `idc` WRITE;
/*!40000 ALTER TABLE `idc` DISABLE KEYS */;
INSERT INTO `idc` VALUES (1,'zhaowei','zw','aaaa','panda','18210519941','11@qq.com'),(2,'sanyuanqia','syq','sys','aa','18210519941','11@qq.com'),(3,'aaabbbb','aaa','aaaa','aaaa','18210519941','11@qq.com'),(4,'adsdaf','saaa','aaaaa','aaddsds','18210519941','ss@11.com');
/*!40000 ALTER TABLE `idc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `pid` int(11) NOT NULL,
  `module_letter` varchar(10) NOT NULL,
  `op_interface` varchar(255) NOT NULL,
  `dev_interface` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `product_0db3209e` (`pid`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'mall',0,'mall','liuziping,panda','liuziping'),(2,'qiche',0,'qc','admin','admin'),(3,'fangchan',0,'fc','admin','admin'),(4,'api',1,'api','liuziping','admin'),(5,'api',2,'api','liuziping','liuziping'),(6,'web',3,'web','liuziping','liuziping'),(7,'web',1,'web','liuziping','liuziping'),(8,'mysql',1,'db','liuziping,panda','liuziping,panda'),(9,'aaaa',0,'aa','liuziping,panda','liuziping'),(10,'wb',9,'we','admin','admin');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `server`
--

DROP TABLE IF EXISTS `server`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `server` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `supplier` int(11) DEFAULT NULL,
  `manufacturers` varchar(50) DEFAULT NULL,
  `manufacture_date` date DEFAULT NULL,
  `server_type` varchar(20) DEFAULT NULL,
  `sn` varchar(60) DEFAULT NULL,
  `os` varchar(50) DEFAULT NULL,
  `hostname` varchar(50) DEFAULT NULL,
  `inner_ip` varchar(32) DEFAULT NULL,
  `mac_address` varchar(50) DEFAULT NULL,
  `ip_info` varchar(255) DEFAULT NULL,
  `server_cpu` varchar(250) DEFAULT NULL,
  `server_disk` varchar(100) DEFAULT NULL,
  `server_mem` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `remark` longtext,
  `service_id` int(11) DEFAULT NULL,
  `check_update_time` datetime DEFAULT NULL,
  `vm_status` int(11) DEFAULT NULL,
  `uuid` varchar(100) DEFAULT NULL,
  `idc_id` int(11) DEFAULT NULL,
  `server_purpose_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `inner_ip` (`inner_ip`),
  KEY `server_afbe94cd` (`sn`),
  KEY `server_0897acf4` (`hostname`),
  KEY `server_9acb4454` (`status`),
  KEY `server_b0dc1e29` (`service_id`),
  KEY `server_25e25237` (`vm_status`),
  KEY `server_ef7c876f` (`uuid`),
  KEY `server_0869e37a` (`idc_id`),
  KEY `server_a3b69d2a` (`server_purpose_id`)
) ENGINE=MyISAM AUTO_INCREMENT=200 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `server`
--

LOCK TABLES `server` WRITE;
/*!40000 ALTER TABLE `server` DISABLE KEYS */;
INSERT INTO `server` VALUES (1,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-web-01','10.20.1.1','68:6:b1:db:81:a8',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB','online',NULL,1,NULL,1,'ba32f054-4bfd-11e7-9953-00163e0066b5',NULL,8),(2,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-web-02','10.20.1.3','f0:c8:59:65:2d:95',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB','online',NULL,3,NULL,1,'ba453b92-4bfd-11e7-9953-00163e0066b5',NULL,6),(3,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-web-03','10.20.1.5','8:1d:83:19:e8:41',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba465f04-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(4,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-web-04','10.20.1.7','78:3:8f:af:7f:4',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba475bfc-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(5,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-web-05','10.20.1.9','27:11:ef:cd:a1:1a',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba485d90-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(6,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-web-06','10.20.1.11','83:66:f5:ec:e1:2',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba495e16-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(7,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-web-07','10.20.1.13','5e:50:f9:9:d5:55',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba4a5ba4-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(8,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-web-08','10.20.1.15','11:2:f8:a4:86:c7',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,2,NULL,1,'ba4b5996-4bfd-11e7-9953-00163e0066b5',NULL,5),(9,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-web-09','10.20.1.17','f8:88:55:76:71:69',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba4c5922-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(10,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-wap-01','10.20.1.19','54:ea:47:b9:e8:c0',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba4d5700-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(11,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-wap-02','10.20.1.21','a1:72:fc:17:3b:f',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba4e8c6a-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(12,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-wap-03','10.20.1.23','f5:df:1f:18:7a:d2',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba4f90ec-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(13,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-wap-04','10.20.1.25','ca:57:b4:51:e8:22',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba50ac8e-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(14,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-wap-05','10.20.1.27','65:17:76:ac:9:47',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba51bd40-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(15,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-wap-06','10.20.1.29','1b:95:ee:84:7a:bf',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba52bc22-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(16,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-wap-07','10.20.1.31','b7:b0:86:0:46:f6',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba53bfaa-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(17,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-wap-08','10.20.1.33','a7:a1:a:93:27:81',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba54c210-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(18,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-wap-09','10.20.1.35','a1:98:91:f9:73:d5',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB','online',NULL,NULL,NULL,1,'ba55caa2-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(19,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-app-01','10.20.1.37','3c:61:3d:c:1c:af',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba56d866-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(20,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-app-02','10.20.1.39','5c:49:95:f0:4b:59',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba57ef30-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(21,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-app-03','10.20.1.41','69:94:fe:f1:5:1d',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba58f092-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(22,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-app-04','10.20.1.43','a7:fb:75:d9:5a:4a',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba59f172-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(23,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-app-05','10.20.1.45','8f:89:97:78:fe:c2',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba5af144-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(24,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-app-06','10.20.1.47','cd:8f:f4:5b:3a:b6',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba5bfb66-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(25,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-app-07','10.20.1.49','80:7e:78:32:c3:97',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba5d0830-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(26,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-app-08','10.20.1.51','d7:6c:be:88:37:4b',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba5e065e-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(27,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-app-09','10.20.1.53','b7:56:f0:95:99:4c',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba5f07b6-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(28,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-api-01','10.20.1.55','b0:b:5:a3:f:b',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba60033c-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(29,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-api-02','10.20.1.57','de:7e:17:2c:a9:63',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba6100a2-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(30,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-api-03','10.20.1.59','78:b4:8c:6b:84:1f',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba61fc1e-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(31,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-api-04','10.20.1.61','77:c4:ff:19:4f:ec',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba62fcd6-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(32,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-api-05','10.20.1.63','8a:a6:e6:f3:a0:8',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba63f58c-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(33,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-api-06','10.20.1.65','e0:0:6f:7a:8a:97',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba64f414-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(34,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-api-07','10.20.1.67','d0:58:28:c8:83:da',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba65f102-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(35,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-api-08','10.20.1.69','d4:54:8:16:ae:ea',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba66f6f6-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(36,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-fang-api-09','10.20.1.71','9c:b2:3:5d:88:a9',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba6834f8-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(37,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-web-01','10.20.1.73','f:af:98:88:c8:70',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba693e84-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(38,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-web-02','10.20.1.75','a7:e3:5a:94:87:dc',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba6a378a-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(39,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-web-03','10.20.1.77','2c:ab:2f:19:c9:50',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba6b38a6-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(40,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-web-04','10.20.1.79','74:10:dc:75:c2:70',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba6dd228-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(41,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-web-05','10.20.1.81','f6:6f:f8:1e:14:b3',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba6ed3bc-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(42,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-web-06','10.20.1.83','99:e2:45:e4:e9:53',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba6fd3a2-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(43,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-web-07','10.20.1.85','5d:c6:d6:98:8d:4b',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba70e968-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(44,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-web-08','10.20.1.87','a5:47:d7:84:5e:e',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba736f9e-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(45,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-web-09','10.20.1.89','24:7c:c4:5f:84:fd',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba746a34-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(46,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-wap-01','10.20.1.91','0:11:c5:c4:f7:44',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba756fba-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(47,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-wap-02','10.20.1.93','81:80:ee:25:4b:69',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba766a14-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(48,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-wap-03','10.20.1.95','5e:2d:fa:e9:ef:13',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba77670c-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(49,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-wap-04','10.20.1.97','30:6d:b9:fc:8b:8d',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba786b7a-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(50,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-wap-05','10.20.1.99','47:bf:90:a:5c:ac',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba79652a-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(51,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-wap-06','10.20.1.101','6a:ab:a1:37:4e:d2',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba7a6092-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(52,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-wap-07','10.20.1.103','34:fe:58:56:e5:aa',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba7b653c-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(53,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-wap-08','10.20.1.105','65:1b:ff:35:be:fb',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba7c5c44-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(54,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-wap-09','10.20.1.107','be:a8:71:9d:60:89',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba7d5a72-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(55,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-app-01','10.20.1.109','b9:22:8:7f:d1:3f',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba7e5242-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(56,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-app-02','10.20.1.111','e2:49:b2:9e:58:ff',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba7f84f0-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(57,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-app-03','10.20.1.113','c8:f8:4e:49:48:de',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba8098c2-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(58,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-app-04','10.20.1.115','35:c:44:c3:77:e0',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba8196fa-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(59,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-app-05','10.20.1.117','55:90:d2:18:50:e4',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba828d30-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(60,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-app-06','10.20.1.119','18:18:68:9f:14:5e',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba838992-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(61,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-app-07','10.20.1.121','43:fd:ae:7e:44:7a',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba84918e-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(62,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-app-08','10.20.1.123','89:50:e0:0:46:43',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba858936-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(63,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-app-09','10.20.1.125','5a:53:5a:2d:8b:8c',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba868868-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(64,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-api-01','10.20.1.127','f7:a0:1e:e7:c6:28',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba878d1c-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(65,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-api-02','10.20.1.129','87:f5:53:14:f5:a',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba888e1a-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(66,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-api-03','10.20.1.131','d:1f:d1:d0:bc:c4',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba899134-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(67,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-api-04','10.20.1.133','2b:38:a7:73:4c:e2',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba8a8cb0-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(68,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-api-05','10.20.1.135','d8:4a:3f:64:be:7f',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba8b8f34-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(69,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-api-06','10.20.1.137','b7:29:bc:d9:25:12',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba8cc700-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(70,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-api-07','10.20.1.139','cd:91:30:1d:ab:a9',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba8dcb46-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(71,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-api-08','10.20.1.141','b4:6a:9c:8:da:88',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba8ecbea-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(72,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-zp-api-09','10.20.1.143','9e:a4:f1:f8:b8:2b',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba8fd404-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(73,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-web-01','10.20.1.145','b3:10:3a:e6:25:95',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba91aaea-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(74,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-web-02','10.20.1.147','44:13:8c:1e:78:18',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba92cdb2-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(75,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-web-03','10.20.1.149','81:9b:2d:16:f6:9c',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba93caf0-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(76,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-web-04','10.20.1.151','24:9b:d2:70:57:26',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba94cb1c-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(77,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-web-05','10.20.1.153','61:6d:9d:c3:ba:e0',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba95c878-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(78,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-web-06','10.20.1.155','c2:8f:7:80:29:d7',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba96c52a-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(79,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-web-07','10.20.1.157','e4:5e:92:6b:1c:50',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba97ceb6-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(80,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-web-08','10.20.1.159','ac:ec:d8:4e:29:97',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba98ca96-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(81,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-web-09','10.20.1.161','ce:79:ea:11:c6:42',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba99dada-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(82,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-wap-01','10.20.1.163','60:82:40:f4:e2:97',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba9ae66e-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(83,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-wap-02','10.20.1.165','a0:43:f6:13:64:a7',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba9be924-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(84,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-wap-03','10.20.1.167','85:e4:29:df:95:ba',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba9cfc6a-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(85,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-wap-04','10.20.1.169','3d:f0:7c:93:49:9b',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba9e3404-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(86,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-wap-05','10.20.1.171','94:12:3d:f:9d:1',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'ba9f4236-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(87,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-wap-06','10.20.1.173','24:1d:57:24:79:b5',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baa0410e-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(88,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-wap-07','10.20.1.175','de:33:d2:53:4c:39',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baa13d8e-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(89,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-wap-08','10.20.1.177','53:7d:7:c7:dd:5a',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baa23e28-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(90,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-wap-09','10.20.1.179','57:57:b3:63:90:d',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baa34282-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(91,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-app-01','10.20.1.181','5c:55:2a:53:25:e1',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baa4452e-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(92,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-app-02','10.20.1.183','9c:f1:6d:f3:1c:f',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baa55450-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(93,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-app-03','10.20.1.185','f5:9e:d6:cc:56:45',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baa64c2a-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(94,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-app-04','10.20.1.187','a7:91:8e:f4:3c:17',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baa7486e-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(95,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-app-05','10.20.1.189','71:45:c2:40:29:eb',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baa88bc0-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(96,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-app-06','10.20.1.191','f6:b1:e1:d0:5f:3e',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baa99f6a-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(97,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-app-07','10.20.1.193','1f:82:99:1e:2a:bc',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baaad0c4-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(98,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-app-08','10.20.1.195','8b:d4:91:0:c1:fc',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baabd3ac-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(99,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-app-09','10.20.1.197','6a:1c:53:2d:8a:14',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baacd5ae-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(100,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-api-01','10.20.1.199','ed:1d:be:c9:3a:59',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baade08e-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(101,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-api-02','10.20.1.201','e3:e5:b0:f2:46:d5',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baaed9c6-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(102,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-api-03','10.20.1.203','f8:73:b7:34:31:31',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baafd57e-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(103,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-api-04','10.20.1.205','c1:c1:1b:8f:10:d2',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bab0e2ac-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(104,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-api-05','10.20.1.207','84:26:b6:99:d0:11',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bab1d8c4-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(105,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-api-06','10.20.1.209','0:fb:5b:fb:e0:2f',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bab2d332-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(106,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-api-07','10.20.1.211','cc:b8:1a:5f:56:81',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bab3cbe8-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(107,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-api-08','10.20.1.213','9a:bd:de:b0:82:34',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bab4c426-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(108,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-sec-api-09','10.20.1.215','6e:f6:88:86:66:dd',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bab5bc46-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(109,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-web-01','10.20.1.217','f6:a9:be:45:92:41',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bab6c334-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(110,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-web-02','10.20.1.219','89:51:53:95:16:cb',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bab7caf4-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(111,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-web-03','10.20.1.221','98:1c:62:81:24:d0',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bab8cb34-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(112,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-web-04','10.20.1.223','2a:75:c3:f7:f:4d',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bab9cd90-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(113,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-web-05','10.20.1.225','2a:96:6b:fe:74:51',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'babae5e0-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(114,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-web-06','10.20.1.227','12:45:9f:44:18:82',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'babc11f4-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(115,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-web-07','10.20.1.229','74:ae:ce:60:0:e5',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'babd1676-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(116,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-web-08','10.20.1.231','7a:8e:fa:e9:aa:e8',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'babe1d96-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(117,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-web-09','10.20.1.233','56:73:1b:1a:6a:58',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'babf22ea-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(118,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-wap-01','10.20.1.235','bf:b5:30:47:53:67',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bac02686-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(119,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-wap-02','10.20.1.237','59:6f:d9:fe:e3:8b',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bac1412e-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(120,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-wap-03','10.20.1.239','b7:5c:25:3c:d2:b3',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bac24b50-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(121,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-wap-04','10.20.1.241','e:f:a2:7e:28:c0',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bac35478-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(122,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-wap-05','10.20.1.243','ec:85:c5:fe:3f:84',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB','online',NULL,NULL,NULL,1,'bac4560c-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(123,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-wap-06','10.20.1.245','61:3:77:66:ad:5a',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,1,NULL,1,'bac5516a-4bfd-11e7-9953-00163e0066b5',NULL,4),(124,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-wap-07','10.20.1.247','1:ba:16:d5:64:7e',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bac64ad4-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(125,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-wap-08','10.20.1.249','ce:43:5e:49:e4:15',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bac74d26-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(126,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-wap-09','10.20.1.251','67:8c:c5:67:c0:63',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bac86198-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(127,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-app-01','10.20.1.253','10:5e:ba:a9:17:43',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bac960a2-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(128,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-app-02','10.20.4.1','b1:ed:7d:be:0:8a',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baca5822-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(129,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-app-03','10.20.4.3','cf:9c:ef:90:5b:58',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bacb52e0-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(130,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-app-04','10.20.4.5','75:8d:83:9c:15:43',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bacc49a2-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(131,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-app-05','10.20.4.7','e9:f3:1d:af:db:68',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bacd50f4-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(132,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-app-06','10.20.4.9','4b:8:52:bd:5c:14',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bace49e6-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(133,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-app-07','10.20.4.11','c6:d3:c:13:36:c5',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bacf4dfa-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(134,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-app-08','10.20.4.13','51:97:1f:66:df:b4',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bad045ca-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(135,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-app-09','10.20.4.15','b2:b:71:1a:69:32',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bad13e94-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(136,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-api-01','10.20.4.17','f3:b2:c3:6d:d:40',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bad23498-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(137,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-api-02','10.20.4.19','54:8:c4:61:d0:a3',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bad33848-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(138,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-api-03','10.20.4.21','74:ad:d2:fb:47:9',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bad42e38-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(139,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-api-04','10.20.4.23','ab:86:35:35:60:2c',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bad524aa-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(140,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-api-05','10.20.4.25','4f:e:be:74:80:7e',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bad61b58-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(141,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-api-06','10.20.4.27','27:5:df:23:4f:8',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bad7d664-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(142,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-api-07','10.20.4.29','c5:87:4e:76:7:95',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bada623a-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(143,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-api-08','10.20.4.31','42:73:18:e2:4d:e7',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'badbfed8-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(144,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-service-api-09','10.20.4.33','30:f:6b:2:61:1',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'badcf9c8-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(145,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-web-01','10.20.4.35','2:21:b7:46:10:e2',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bade0304-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(146,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-web-02','10.20.4.37','17:75:a9:36:64:cd',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'badefbb0-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(147,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-web-03','10.20.4.39','62:b9:c5:49:80:aa',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'badff236-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(148,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-web-04','10.20.4.41','65:64:ef:b5:c0:c6',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bae0eb50-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(149,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-web-05','10.20.4.43','de:6b:34:a9:6b:52',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bae1e53c-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(150,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-web-06','10.20.4.45','26:9f:42:c1:5e:c6',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bae2dc08-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(151,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-web-07','10.20.4.47','2a:b4:ea:cd:ad:ba',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bae3d2f2-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(152,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-web-08','10.20.4.49','4:54:e5:1:20:22',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bae4ce5a-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(153,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-web-09','10.20.4.51','2b:e5:37:3c:92:6b',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bae5c3dc-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(154,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-wap-01','10.20.4.53','b2:22:a1:2f:ea:2c',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bae6c8c2-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(155,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-wap-02','10.20.4.55','ce:7c:25:68:2f:b1',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bae7c524-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(156,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-wap-03','10.20.4.57','ca:6d:3e:77:ca:a1',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bae8bf2e-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(157,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-wap-04','10.20.4.59','70:f3:76:47:49:eb',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bae9bf78-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(158,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-wap-05','10.20.4.61','fb:24:33:e3:7b:83',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baeab766-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(159,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-wap-06','10.20.4.63','52:d1:22:3:10:80',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baebb0d0-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(160,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-wap-07','10.20.4.65','dc:f4:ec:28:29:bf',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baeca742-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(161,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-wap-08','10.20.4.67','88:68:ea:b5:3f:7a',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baed9e40-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(162,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-wap-09','10.20.4.69','2b:45:f7:3:25:b7',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baee9458-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(163,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-app-01','10.20.4.71','8d:a2:c6:be:a9:72',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baef8ade-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(164,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-app-02','10.20.4.73','74:96:0:47:f1:83',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baf0822c-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(165,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-app-03','10.20.4.75','4b:18:2f:73:18:80',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baf1867c-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(166,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-app-04','10.20.4.77','1b:2d:97:c0:8d:2a',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baf2802c-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(167,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-app-05','10.20.4.79','82:31:dd:f:86:f7',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baf377f2-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(168,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-app-06','10.20.4.81','67:de:2f:a1:62:ed',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baf47c06-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(169,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-app-07','10.20.4.83','97:25:5a:3c:e5:92',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baf5847a-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(170,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-app-08','10.20.4.85','fe:ab:5e:dc:31:ed',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baf680dc-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(171,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-app-09','10.20.4.87','b1:f:b:3b:fb:33',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baf78798-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(172,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-api-01','10.20.4.89','80:73:3c:d9:c7:b8',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baf87e46-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(173,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-api-02','10.20.4.91','e9:a8:78:94:5:7a',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baf976de-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(174,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-api-03','10.20.4.93','63:c0:b6:46:b3:8f',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bafa6eea-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(175,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-api-04','10.20.4.95','aa:41:eb:c5:41:24',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bafb6430-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(176,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-api-05','10.20.4.97','d8:4a:d7:b:d3:98',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bafc5a7a-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(177,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-api-06','10.20.4.99','38:eb:a9:12:62:3e',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bafd51d2-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(178,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-api-07','10.20.4.101','25:fb:39:22:bd:2b',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bafe4a42-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(179,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-api-08','10.20.4.103','b4:6b:8f:8f:e5:7f',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'baff3fd8-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(180,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','yz-pay-api-09','10.20.4.105','4a:f:3f:d:b2:c4',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bb0035be-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(181,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','zw-fang-web-01','10.20.4.107','b1:ca:16:e:b9:47',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bb0139e6-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(182,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','zw-fang-web-02','10.20.4.109','82:7b:11:33:59:c6',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bb022fea-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(183,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','zw-fang-web-03','10.20.4.111','e0:bd:f1:8a:db:3e',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bb032c88-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(184,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','zw-fang-web-04','10.20.4.113','1:2f:a4:99:6b:e2',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bb0425c0-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(185,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','zw-fang-web-05','10.20.4.115','3e:f2:85:48:f3:66',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bb051f02-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(186,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','zw-fang-web-06','10.20.4.117','a:79:22:9e:5e:d1',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bb06160a-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(187,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','zw-fang-web-07','10.20.4.119','ef:94:8:90:b4:a4',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bb070f10-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(188,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','zw-fang-web-08','10.20.4.121','77:6c:41:4a:92:52',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bb081216-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(189,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','zw-fang-web-09','10.20.4.123','83:43:89:50:ff:f0',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bb090acc-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(190,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','zw-fang-wap-01','10.20.4.125','e0:70:d8:58:a5:ef',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bb0a0134-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(191,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','zw-fang-wap-02','10.20.4.127','19:1c:12:b8:49:4',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bb0b0f70-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(192,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','zw-fang-wap-03','10.20.4.129','29:e:f:23:95:a8',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bb0da1ae-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(193,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','zw-fang-wap-04','10.20.4.131','39:ce:61:5f:9b:88',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bb0eada6-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(194,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','zw-fang-wap-05','10.20.4.133','52:3a:fe:85:b6:e7',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bb0fa5c6-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(195,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','zw-fang-wap-06','10.20.4.135','7b:c2:73:a8:9a:7d',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bb109f80-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(196,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','zw-fang-wap-07','10.20.4.137','fb:bc:c0:95:db:7c',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bb11952a-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(197,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','zw-fang-wap-08','10.20.4.139','8a:c2:91:2b:6e:c2',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bb128d2c-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(198,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','zw-fang-wap-09','10.20.4.141','69:81:82:52:6c:59',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bb1387ae-4bfd-11e7-9953-00163e0066b5',NULL,NULL),(199,NULL,'innotek GmbH','2006-12-01','VirtualBox','0','CentOS 6.6 Final','zw-fang-app-01','10.20.4.143','d4:13:56:55:1b:a8',NULL,'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1','9','490.39 MB',NULL,NULL,NULL,NULL,1,'bb148546-4bfd-11e7-9953-00163e0066b5',NULL,NULL);
/*!40000 ALTER TABLE `server` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `status`
--

DROP TABLE IF EXISTS `status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `status` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `status`
--

LOCK TABLES `status` WRITE;
/*!40000 ALTER TABLE `status` DISABLE KEYS */;
INSERT INTO `status` VALUES (1,'online'),(2,'remove'),(3,'offline');
/*!40000 ALTER TABLE `status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `work_order_workorder`
--

DROP TABLE IF EXISTS `work_order_workorder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `work_order_workorder` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `type` int(11) NOT NULL,
  `order_contents` longtext NOT NULL,
  `status` int(11) NOT NULL,
  `result_desc` longtext,
  `apply_time` datetime NOT NULL,
  `complete_time` datetime NOT NULL,
  `applicant_id` int(11) NOT NULL,
  `assign_to_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `work_order_workorder_afed695d` (`applicant_id`),
  KEY `work_order_workorder_43309e6f` (`assign_to_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `work_order_workorder`
--

LOCK TABLES `work_order_workorder` WRITE;
/*!40000 ALTER TABLE `work_order_workorder` DISABLE KEYS */;
INSERT INTO `work_order_workorder` VALUES (3,'????',0,'??',2,'aaa','2017-05-27 08:09:38','2017-05-27 09:37:03',1,1),(6,'nihao',0,'nihao',2,'nihao','2017-05-29 16:24:00','2017-05-29 16:24:14',1,1),(8,'aaaaaaaaaa',0,'aaaaaaaa',2,'hahah','2017-06-05 23:08:58','2017-06-06 14:53:18',1,1);
/*!40000 ALTER TABLE `work_order_workorder` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-06-09 16:58:23
