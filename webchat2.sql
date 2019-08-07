-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: localhost    Database: webchat_db
-- ------------------------------------------------------
-- Server version	5.7.27-0ubuntu0.18.04.1

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
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
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
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
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add city',7,'add_city'),(20,'Can change city',7,'change_city'),(21,'Can delete city',7,'delete_city'),(22,'Can add messages',8,'add_messages'),(23,'Can change messages',8,'change_messages'),(24,'Can delete messages',8,'delete_messages'),(25,'Can add messages type',9,'add_messagestype'),(26,'Can change messages type',9,'change_messagestype'),(27,'Can delete messages type',9,'delete_messagestype'),(28,'Can add province',10,'add_province'),(29,'Can change province',10,'change_province'),(30,'Can delete province',10,'delete_province'),(31,'Can add user',11,'add_user'),(32,'Can change user',11,'change_user'),(33,'Can delete user',11,'delete_user'),(34,'Can add user_ group',12,'add_user_group'),(35,'Can change user_ group',12,'change_user_group'),(36,'Can delete user_ group',12,'delete_user_group'),(37,'Can add user_ groups msg content',13,'add_user_groupsmsgcontent'),(38,'Can change user_ groups msg content',13,'change_user_groupsmsgcontent'),(39,'Can delete user_ groups msg content',13,'delete_user_groupsmsgcontent'),(40,'Can add user_ groups msg to user',14,'add_user_groupsmsgtouser'),(41,'Can change user_ groups msg to user',14,'change_user_groupsmsgtouser'),(42,'Can delete user_ groups msg to user',14,'delete_user_groupsmsgtouser'),(43,'Can add user_ groups to user',15,'add_user_groupstouser'),(44,'Can change user_ groups to user',15,'change_user_groupstouser'),(45,'Can delete user_ groups to user',15,'delete_user_groupstouser'),(46,'Can add user info',16,'add_userinfo'),(47,'Can change user info',16,'change_userinfo'),(48,'Can delete user info',16,'delete_userinfo');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `city_code`
--

DROP TABLE IF EXISTS `city_code`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `city_code` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `city` varchar(20) NOT NULL,
  `code` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=464 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `city_code`
--

LOCK TABLES `city_code` WRITE;
/*!40000 ALTER TABLE `city_code` DISABLE KEYS */;
INSERT INTO `city_code` VALUES (2,'北京','101010100'),(3,'海淀','101010200'),(4,'朝阳','101010300'),(5,'顺义','101010400'),(6,'怀柔','101010500'),(7,'通州','101010600'),(8,'昌平','101010700'),(9,'延庆','101010800'),(10,'丰台','101010900'),(11,'石景山','101011000'),(12,'大兴','101011100'),(13,'房山','101011200'),(14,'密云','101011300'),(15,'门头沟','101011400'),(16,'平谷','101011500'),(17,'东城','101011600'),(18,'西城','101011700'),(19,'天津','101030100'),(20,'武清','101030200'),(21,'宝坻','101030300'),(22,'东丽','101030400'),(23,'西青','101030500'),(24,'北辰','101030600'),(25,'宁河','101030700'),(26,'和平','101030800'),(27,'静海','101030900'),(28,'津南','101031000'),(29,'滨海新区','101031100'),(30,'河东','101031200'),(31,'河西','101031300'),(32,'蓟州','101031400'),(33,'南开','101031500'),(34,'河北','101031600'),(35,'红桥','101031700'),(36,'石家庄','101090101'),(37,'保定','101090201'),(38,'张家口','101090301'),(39,'承德','101090402'),(40,'唐山','101090501'),(41,'廊坊','101090601'),(42,'沧州','101090701'),(43,'衡水','101090801'),(44,'邢台','101090901'),(45,'邯郸','101091001'),(46,'秦皇岛','101091101'),(47,'雄安新区','101091201'),(48,'太原','101100101'),(49,'大同','101100201'),(50,'阳泉','101100301'),(51,'晋中','101100401'),(52,'长治','101100501'),(53,'晋城','101100601'),(54,'临汾','101100701'),(55,'运城','101100801'),(56,'朔州','101100901'),(57,'忻州','101101001'),(58,'吕梁','101101100'),(59,'呼和浩特','101080101'),(60,'包头','101080201'),(61,'乌海','101080301'),(62,'乌兰察布','101080401'),(63,'通辽','101080501'),(64,'赤峰','101080601'),(65,'鄂尔多斯','101080701'),(66,'巴彦淖尔','101080801'),(67,'锡林郭勒','101080901'),(68,'呼伦贝尔','101081001'),(69,'兴安盟','101081101'),(70,'阿拉善盟','101081201'),(71,'哈尔滨','101050101'),(72,'齐齐哈尔','101050201'),(73,'牡丹江','101050301'),(74,'佳木斯','101050401'),(75,'绥化','101050501'),(76,'黑河','101050601'),(77,'大兴安岭','101050701'),(78,'伊春','101050801'),(79,'大庆','101050901'),(80,'七台河','101051002'),(81,'鸡西','101051101'),(82,'鹤岗','101051201'),(83,'双鸭山','101051301'),(84,'长春','101060101'),(85,'吉林','101060201'),(86,'延边','101060301'),(87,'四平','101060401'),(88,'通化','101060501'),(89,'白城','101060601'),(90,'辽源','101060701'),(91,'松原','101060801'),(92,'白山','101060901'),(93,'沈阳','101070101'),(94,'大连','101070201'),(95,'鞍山','101070301'),(96,'抚顺','101070401'),(97,'本溪','101070501'),(98,'丹东','101070601'),(99,'锦州','101070701'),(100,'营口','101070801'),(101,'阜新','101070901'),(102,'辽阳','101071001'),(103,'铁岭','101071101'),(104,'朝阳','101071201'),(105,'盘锦','101071301'),(106,'葫芦岛','101071401'),(107,'上海','101020100'),(108,'闵行','101020200'),(109,'宝山','101020300'),(110,'黄浦','101020400'),(111,'嘉定','101020500'),(112,'浦东新区','101020600'),(113,'金山','101020700'),(114,'青浦','101020800'),(115,'松江','101020900'),(116,'奉贤','101021000'),(117,'崇明','101021100'),(118,'徐汇','101021200'),(119,'长宁','101021300'),(120,'静安','101021400'),(121,'普陀','101021500'),(122,'虹口','101021600'),(123,'杨浦','101021700'),(124,'合肥','101220101'),(125,'蚌埠','101220201'),(126,'芜湖','101220301'),(127,'淮南','101220401'),(128,'马鞍山','101220501'),(129,'安庆','101220601'),(130,'宿州','101220701'),(131,'阜阳','101220801'),(132,'亳州','101220901'),(133,'黄山','101221001'),(134,'滁州','101221101'),(135,'淮北','101221201'),(136,'铜陵','101221301'),(137,'宣城','101221401'),(138,'六安','101221501'),(139,'池州','101221701'),(140,'南京','101190101'),(141,'无锡','101190201'),(142,'镇江','101190301'),(143,'苏州','101190401'),(144,'南通','101190501'),(145,'扬州','101190601'),(146,'盐城','101190701'),(147,'徐州','101190801'),(148,'淮安','101190901'),(149,'连云港','101191001'),(150,'常州','101191101'),(151,'泰州','101191201'),(152,'宿迁','101191301'),(153,'济南','101120101'),(154,'青岛','101120201'),(155,'淄博','101120301'),(156,'德州','101120401'),(157,'烟台','101120501'),(158,'潍坊','101120601'),(159,'济宁','101120701'),(160,'泰安','101120801'),(161,'临沂','101120901'),(162,'菏泽','101121001'),(163,'滨州','101121101'),(164,'东营','101121201'),(165,'威海','101121301'),(166,'枣庄','101121401'),(167,'日照','101121501'),(168,'莱芜','101121601'),(169,'聊城','101121701'),(170,'杭州','101210101'),(171,'湖州','101210201'),(172,'嘉兴','101210301'),(173,'宁波','101210401'),(174,'绍兴','101210501'),(175,'台州','101210601'),(176,'温州','101210701'),(177,'丽水','101210801'),(178,'金华','101210901'),(179,'衢州','101211001'),(180,'舟山','101211101'),(181,'福州','101230101'),(182,'厦门','101230201'),(183,'宁德','101230301'),(184,'莆田','101230401'),(185,'泉州','101230501'),(186,'漳州','101230601'),(187,'龙岩','101230701'),(188,'三明','101230801'),(189,'南平','101230901'),(190,'钓鱼岛','101231001'),(191,'南昌','101240101'),(192,'九江','101240201'),(193,'上饶','101240301'),(194,'抚州','101240401'),(195,'宜春','101240501'),(196,'吉安','101240601'),(197,'赣州','101240701'),(198,'景德镇','101240801'),(199,'萍乡','101240901'),(200,'新余','101241001'),(201,'鹰潭','101241101'),(202,'武汉','101200101'),(203,'襄阳','101200201'),(204,'鄂州','101200301'),(205,'孝感','101200401'),(206,'黄冈','101200501'),(207,'黄石','101200601'),(208,'咸宁','101200701'),(209,'荆州','101200801'),(210,'宜昌','101200901'),(211,'恩施','101201001'),(212,'十堰','101201101'),(213,'神农架','101201201'),(214,'随州','101201301'),(215,'荆门','101201401'),(216,'天门','101201501'),(217,'仙桃','101201601'),(218,'潜江','101201701'),(219,'长沙','101250101'),(220,'湘潭','101250201'),(221,'株洲','101250301'),(222,'衡阳','101250401'),(223,'郴州','101250501'),(224,'常德','101250601'),(225,'益阳','101250700'),(226,'娄底','101250801'),(227,'邵阳','101250901'),(228,'岳阳','101251001'),(229,'张家界','101251101'),(230,'怀化','101251201'),(231,'永州','101251401'),(232,'湘西','101251501'),(233,'郑州','101180101'),(234,'安阳','101180201'),(235,'新乡','101180301'),(236,'许昌','101180401'),(237,'平顶山','101180501'),(238,'信阳','101180601'),(239,'南阳','101180701'),(240,'开封','101180801'),(241,'洛阳','101180901'),(242,'商丘','101181001'),(243,'焦作','101181101'),(244,'鹤壁','101181201'),(245,'濮阳','101181301'),(246,'周口','101181401'),(247,'漯河','101181501'),(248,'驻马店','101181601'),(249,'三门峡','101181701'),(250,'济源','101181801'),(251,'南宁','101300101'),(252,'崇左','101300201'),(253,'柳州','101300301'),(254,'来宾','101300401'),(255,'桂林','101300501'),(256,'梧州','101300601'),(257,'贺州','101300701'),(258,'贵港','101300801'),(259,'玉林','101300901'),(260,'百色','101301001'),(261,'钦州','101301101'),(262,'河池','101301201'),(263,'北海','101301301'),(264,'防城港','101301401'),(265,'广州','101280101'),(266,'韶关','101280201'),(267,'惠州','101280301'),(268,'梅州','101280401'),(269,'汕头','101280501'),(270,'深圳','101280601'),(271,'珠海','101280701'),(272,'佛山','101280800'),(273,'肇庆','101280901'),(274,'湛江','101281001'),(275,'江门','101281101'),(276,'河源','101281201'),(277,'清远','101281301'),(278,'云浮','101281401'),(279,'潮州','101281501'),(280,'东莞','101281601'),(281,'中山','101281701'),(282,'阳江','101281801'),(283,'揭阳','101281901'),(284,'茂名','101282001'),(285,'汕尾','101282101'),(286,'海口','101310101'),(287,'三亚','101310201'),(288,'东方','101310202'),(289,'临高','101310203'),(290,'澄迈','101310204'),(291,'儋州','101310205'),(292,'昌江','101310206'),(293,'白沙','101310207'),(294,'琼中','101310208'),(295,'定安','101310209'),(296,'屯昌','101310210'),(297,'琼海','101310211'),(298,'文昌','101310212'),(299,'保亭','101310214'),(300,'万宁','101310215'),(301,'陵水','101310216'),(302,'乐东','101310221'),(303,'五指山','101310222'),(304,'西沙','101310302'),(305,'中沙','101310303'),(306,'南沙','101310304'),(307,'西安','101110101'),(308,'咸阳','101110200'),(309,'延安','101110300'),(310,'榆林','101110401'),(311,'渭南','101110501'),(312,'商洛','101110601'),(313,'安康','101110701'),(314,'汉中','101110801'),(315,'宝鸡','101110901'),(316,'铜川','101111001'),(317,'杨凌','101111101'),(318,'兰州','101160101'),(319,'定西','101160201'),(320,'平凉','101160301'),(321,'庆阳','101160401'),(322,'武威','101160501'),(323,'金昌','101160601'),(324,'张掖','101160701'),(325,'酒泉','101160801'),(326,'天水','101160901'),(327,'陇南','101161001'),(328,'临夏','101161101'),(329,'甘南','101161201'),(330,'白银','101161301'),(331,'嘉峪关','101161401'),(332,'乌鲁木齐','101130101'),(333,'克拉玛依','101130201'),(334,'石河子','101130301'),(335,'昌吉','101130401'),(336,'吐鲁番','101130501'),(337,'巴音郭楞','101130601'),(338,'阿拉尔','101130701'),(339,'阿克苏','101130801'),(340,'喀什','101130901'),(341,'伊犁','101131001'),(342,'塔城','101131101'),(343,'哈密','101131201'),(344,'和田','101131301'),(345,'阿勒泰','101131401'),(346,'克州','101131501'),(347,'博尔塔拉','101131601'),(348,'图木舒克','101131701'),(349,'五家渠','101131801'),(350,'铁门关','101131901'),(351,'北屯','101132101'),(352,'双河','101132201'),(353,'可克达拉','101132301'),(354,'西宁','101150101'),(355,'海东','101150201'),(356,'黄南','101150301'),(357,'海南','101150401'),(358,'果洛','101150501'),(359,'玉树','101150601'),(360,'海西','101150701'),(361,'海北','101150801'),(362,'银川','101170101'),(363,'石嘴山','101170201'),(364,'吴忠','101170301'),(365,'固原','101170401'),(366,'中卫','101170501'),(367,'成都','101270101'),(368,'攀枝花','101270201'),(369,'自贡','101270301'),(370,'绵阳','101270401'),(371,'南充','101270501'),(372,'达州','101270601'),(373,'遂宁','101270701'),(374,'广安','101270801'),(375,'巴中','101270901'),(376,'泸州','101271001'),(377,'宜宾','101271101'),(378,'内江','101271201'),(379,'资阳','101271301'),(380,'乐山','101271401'),(381,'眉山','101271501'),(382,'凉山','101271601'),(383,'雅安','101271701'),(384,'甘孜','101271801'),(385,'阿坝','101271901'),(386,'德阳','101272001'),(387,'广元','101272101'),(388,'重庆','101040100'),(389,'永川','101040200'),(390,'合川','101040300'),(391,'南川','101040400'),(392,'江津','101040500'),(393,'渝北','101040700'),(394,'北碚','101040800'),(395,'巴南','101040900'),(396,'长寿','101041000'),(397,'黔江','101041100'),(398,'渝中','101041200'),(399,'万州','101041300'),(400,'涪陵','101041400'),(401,'城口','101041600'),(402,'云阳','101041700'),(403,'巫溪','101041800'),(404,'奉节','101041900'),(405,'巫山','101042000'),(406,'潼南','101042100'),(407,'垫江','101042200'),(408,'梁平','101042300'),(409,'忠县','101042400'),(410,'石柱','101042500'),(411,'大足','101042600'),(412,'荣昌','101042700'),(413,'铜梁','101042800'),(414,'璧山','101042900'),(415,'丰都','101043000'),(416,'武隆','101043100'),(417,'彭水','101043200'),(418,'綦江','101043300'),(419,'酉阳','101043400'),(420,'大渡口','101043500'),(421,'秀山','101043600'),(422,'江北','101043700'),(423,'沙坪坝','101043800'),(424,'九龙坡','101043900'),(425,'南岸','101044000'),(426,'开州','101044100'),(427,'贵阳','101260101'),(428,'遵义','101260201'),(429,'安顺','101260301'),(430,'黔南','101260401'),(431,'黔东南','101260501'),(432,'铜仁','101260601'),(433,'毕节','101260701'),(434,'六盘水','101260801'),(435,'黔西南','101260901'),(436,'昆明','101290101'),(437,'大理','101290201'),(438,'红河','101290301'),(439,'曲靖','101290401'),(440,'保山','101290501'),(441,'文山','101290601'),(442,'玉溪','101290701'),(443,'楚雄','101290801'),(444,'普洱','101290901'),(445,'昭通','101291001'),(446,'临沧','101291101'),(447,'怒江','101291201'),(448,'迪庆','101291301'),(449,'丽江','101291401'),(450,'德宏','101291501'),(451,'西双版纳','101291601'),(452,'拉萨','101140101'),(453,'日喀则','101140201'),(454,'山南','101140301'),(455,'林芝','101140401'),(456,'昌都','101140501'),(457,'那曲','101140601'),(458,'阿里','101140701'),(459,'香港','101320101'),(460,'澳门','101330101'),(461,'台北','101340101'),(462,'高雄','101340201'),(463,'台中','101340401');
/*!40000 ALTER TABLE `city_code` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(7,'verify','city'),(8,'verify','messages'),(9,'verify','messagestype'),(10,'verify','province'),(11,'verify','user'),(16,'verify','userinfo'),(12,'verify','user_group'),(13,'verify','user_groupsmsgcontent'),(14,'verify','user_groupsmsgtouser'),(15,'verify','user_groupstouser');
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
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-08-03 13:22:50.746458'),(2,'auth','0001_initial','2019-08-03 13:22:57.358963'),(3,'admin','0001_initial','2019-08-03 13:22:58.865807'),(4,'admin','0002_logentry_remove_auto_add','2019-08-03 13:22:58.975424'),(5,'contenttypes','0002_remove_content_type_name','2019-08-03 13:22:59.770241'),(6,'auth','0002_alter_permission_name_max_length','2019-08-03 13:23:00.297161'),(7,'auth','0003_alter_user_email_max_length','2019-08-03 13:23:00.781093'),(8,'auth','0004_alter_user_username_opts','2019-08-03 13:23:00.817077'),(9,'auth','0005_alter_user_last_login_null','2019-08-03 13:23:01.254810'),(10,'auth','0006_require_contenttypes_0002','2019-08-03 13:23:01.282661'),(11,'auth','0007_alter_validators_add_error_messages','2019-08-03 13:23:01.336699'),(12,'auth','0008_alter_user_username_max_length','2019-08-03 13:23:02.499636'),(13,'sessions','0001_initial','2019-08-03 13:23:02.995177'),(14,'verify','0001_initial','2019-08-03 13:23:14.491419');
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
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('2y8fvdw19pk33uhh6ot5xr79vkqeg5hm','OTM5MjQ4MWI2NjBkY2U0Y2UxOWUxMDE4YWE1ODUxMmI0ODhmZmUwMTp7InVzZXIiOnsibmFtZSI6Im5ld3MiLCJpZCI6MX19','2019-08-21 00:46:42.736585'),('euemqn0avdxu37wv8tfuqqnm8rmbfh5p','OTM5MjQ4MWI2NjBkY2U0Y2UxOWUxMDE4YWE1ODUxMmI0ODhmZmUwMTp7InVzZXIiOnsibmFtZSI6Im5ld3MiLCJpZCI6MX19','2019-08-19 12:16:06.026214'),('f2crfmwxnni294eqn85byi5xogc5degw','MjliMjZiOGFmNmJiNGY4MDdlMDE0MjYxNWVhM2JiNzU3MWZhNDg0Mzp7InVzZXIiOnsibmFtZSI6IkFuZHkiLCJpZCI6Mn19','2019-08-19 00:39:14.524372'),('iyhbv8v26zy0dlzrknztflg6i1zdo5ch','OTM5MjQ4MWI2NjBkY2U0Y2UxOWUxMDE4YWE1ODUxMmI0ODhmZmUwMTp7InVzZXIiOnsibmFtZSI6Im5ld3MiLCJpZCI6MX19','2019-08-20 13:08:06.476436'),('k3sx4udpyt856xti0yz7edx0z1tget7h','MjliMjZiOGFmNmJiNGY4MDdlMDE0MjYxNWVhM2JiNzU3MWZhNDg0Mzp7InVzZXIiOnsibmFtZSI6IkFuZHkiLCJpZCI6Mn19','2019-08-20 13:16:15.275656'),('rpak4yg4mxbd1zq4pba1e1uf64g7ir0y','NGMxZTYzMzQyZjczMDJjOTRmZDUzY2FjZWMwOGFhZTEwNDc2YzhhZjp7InVzZXIiOnsibmFtZSI6IkVyaWMiLCJpZCI6M319','2019-08-19 12:14:11.314698'),('rup5wzg75p7x31g7k4kabed1j9r04afy','OTM5MjQ4MWI2NjBkY2U0Y2UxOWUxMDE4YWE1ODUxMmI0ODhmZmUwMTp7InVzZXIiOnsibmFtZSI6Im5ld3MiLCJpZCI6MX19','2019-08-17 13:29:05.831843'),('wmz2f6kgdno8acbe8gi2h105cxb01wx8','MjliMjZiOGFmNmJiNGY4MDdlMDE0MjYxNWVhM2JiNzU3MWZhNDg0Mzp7InVzZXIiOnsibmFtZSI6IkFuZHkiLCJpZCI6Mn19','2019-08-18 03:53:28.922874');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `verify_city`
--

DROP TABLE IF EXISTS `verify_city`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `verify_city` (
  `C_ID` int(11) NOT NULL AUTO_INCREMENT,
  `C_Name` varchar(30) NOT NULL,
  `P_ProcvinceID_id` int(11) NOT NULL,
  PRIMARY KEY (`C_ID`),
  KEY `verify_city_P_ProcvinceID_id_00a1a968_fk_verify_province_P_ID` (`P_ProcvinceID_id`),
  CONSTRAINT `verify_city_P_ProcvinceID_id_00a1a968_fk_verify_province_P_ID` FOREIGN KEY (`P_ProcvinceID_id`) REFERENCES `verify_province` (`P_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `verify_city`
--

LOCK TABLES `verify_city` WRITE;
/*!40000 ALTER TABLE `verify_city` DISABLE KEYS */;
INSERT INTO `verify_city` VALUES (1,'11',1);
/*!40000 ALTER TABLE `verify_city` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `verify_messages`
--

DROP TABLE IF EXISTS `verify_messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `verify_messages` (
  `M_ID` int(11) NOT NULL AUTO_INCREMENT,
  `M_PostMessages` longtext NOT NULL,
  `M_status` tinyint(1) NOT NULL,
  `M_time` datetime(6) NOT NULL,
  `M_FromUserID_id` int(11) NOT NULL,
  `M_MessagesTypeID_id` int(11) NOT NULL,
  `M_ToUserID_id` int(11) NOT NULL,
  PRIMARY KEY (`M_ID`),
  UNIQUE KEY `M_FromUserID_id` (`M_FromUserID_id`),
  UNIQUE KEY `M_ToUserID_id` (`M_ToUserID_id`),
  KEY `verify_messages_M_MessagesTypeID_id_484feee1_fk_verify_me` (`M_MessagesTypeID_id`),
  CONSTRAINT `verify_messages_M_FromUserID_id_3d80624e_fk_verify_user_id` FOREIGN KEY (`M_FromUserID_id`) REFERENCES `verify_user` (`id`),
  CONSTRAINT `verify_messages_M_MessagesTypeID_id_484feee1_fk_verify_me` FOREIGN KEY (`M_MessagesTypeID_id`) REFERENCES `verify_messagestype` (`MT_ID`),
  CONSTRAINT `verify_messages_M_ToUserID_id_68ff2a80_fk_verify_user_id` FOREIGN KEY (`M_ToUserID_id`) REFERENCES `verify_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `verify_messages`
--

LOCK TABLES `verify_messages` WRITE;
/*!40000 ALTER TABLE `verify_messages` DISABLE KEYS */;
INSERT INTO `verify_messages` VALUES (9,'',0,'2019-08-05 12:09:45.690046',1,1,2),(10,'{\"sender\": \"Andy\", \"reciver\": \"news\", \"step\": 0, \"dataType\": 0}',0,'2019-08-06 13:40:39.354248',2,1,1);
/*!40000 ALTER TABLE `verify_messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `verify_messagestype`
--

DROP TABLE IF EXISTS `verify_messagestype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `verify_messagestype` (
  `MT_ID` int(11) NOT NULL AUTO_INCREMENT,
  `MT_Name` varchar(20) NOT NULL,
  PRIMARY KEY (`MT_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `verify_messagestype`
--

LOCK TABLES `verify_messagestype` WRITE;
/*!40000 ALTER TABLE `verify_messagestype` DISABLE KEYS */;
INSERT INTO `verify_messagestype` VALUES (1,'0'),(2,'1');
/*!40000 ALTER TABLE `verify_messagestype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `verify_province`
--

DROP TABLE IF EXISTS `verify_province`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `verify_province` (
  `P_ID` int(11) NOT NULL AUTO_INCREMENT,
  `P_name` varchar(30) NOT NULL,
  PRIMARY KEY (`P_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `verify_province`
--

LOCK TABLES `verify_province` WRITE;
/*!40000 ALTER TABLE `verify_province` DISABLE KEYS */;
INSERT INTO `verify_province` VALUES (1,'收发');
/*!40000 ALTER TABLE `verify_province` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `verify_user`
--

DROP TABLE IF EXISTS `verify_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `verify_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `email` varchar(254) NOT NULL,
  `mobile_number` varchar(128) NOT NULL,
  `login_time` datetime(6) NOT NULL,
  `logout_time` datetime(6) NOT NULL,
  `creat_time` datetime(6) NOT NULL,
  `ip_address` varchar(15) NOT NULL,
  `is_active` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `verify_user`
--

LOCK TABLES `verify_user` WRITE;
/*!40000 ALTER TABLE `verify_user` DISABLE KEYS */;
INSERT INTO `verify_user` VALUES (1,'news','pbkdf2_sha1$36000$a$jH5oMRlbfNiwjwWFRD4cD0xdEcQ=','1530358836@qq.com','18720988525','2019-08-03 13:29:51.918495','2019-08-03 13:29:51.918511','2019-07-20 13:12:29.872674','',1),(2,'Andy','pbkdf2_sha1$36000$a$EHe72IBKpqN8TA95mAmvVirZwqQ=','','','2019-07-20 13:24:32.814979','2019-07-20 13:24:32.815032','2019-07-20 13:24:32.815052','',1),(3,'Eric','pbkdf2_sha1$36000$a$/6kqubnxRYMgwSfpKFQ0NSYB4+k=','','','2019-07-20 13:40:46.348813','2019-07-20 13:40:46.348870','2019-07-20 13:40:46.348889','',1),(4,'Ski','pbkdf2_sha1$36000$a$G4eH6XfwLdu3SigDUvGr5l2F93I=','asdf@121.com','18613214564','2019-07-21 02:09:35.532917','2019-07-21 02:09:35.532963','2019-07-21 02:09:35.532982','',1);
/*!40000 ALTER TABLE `verify_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `verify_user_friends`
--

DROP TABLE IF EXISTS `verify_user_friends`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `verify_user_friends` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_user_id` int(11) NOT NULL,
  `to_user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `verify_user_friends_from_user_id_to_user_id_ee73a22c_uniq` (`from_user_id`,`to_user_id`),
  KEY `verify_user_friends_to_user_id_11c69a6e_fk_verify_user_id` (`to_user_id`),
  CONSTRAINT `verify_user_friends_from_user_id_b789f432_fk_verify_user_id` FOREIGN KEY (`from_user_id`) REFERENCES `verify_user` (`id`),
  CONSTRAINT `verify_user_friends_to_user_id_11c69a6e_fk_verify_user_id` FOREIGN KEY (`to_user_id`) REFERENCES `verify_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `verify_user_friends`
--

LOCK TABLES `verify_user_friends` WRITE;
/*!40000 ALTER TABLE `verify_user_friends` DISABLE KEYS */;
INSERT INTO `verify_user_friends` VALUES (1,1,2),(2,2,1);
/*!40000 ALTER TABLE `verify_user_friends` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `verify_user_group`
--

DROP TABLE IF EXISTS `verify_user_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `verify_user_group` (
  `UG_ID` int(11) NOT NULL AUTO_INCREMENT,
  `UG_Name` varchar(30) NOT NULL,
  `UG_CreatTime` datetime(6) NOT NULL,
  `UG_ICon` varchar(30) NOT NULL,
  `UG_Notice` varchar(200) NOT NULL,
  `UG_Intro` varchar(200) NOT NULL,
  `UG_AdminId_id` int(11) NOT NULL,
  PRIMARY KEY (`UG_ID`),
  KEY `verify_user_group_UG_AdminId_id_bf951bab_fk_verify_user_id` (`UG_AdminId_id`),
  CONSTRAINT `verify_user_group_UG_AdminId_id_bf951bab_fk_verify_user_id` FOREIGN KEY (`UG_AdminId_id`) REFERENCES `verify_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `verify_user_group`
--

LOCK TABLES `verify_user_group` WRITE;
/*!40000 ALTER TABLE `verify_user_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `verify_user_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `verify_user_groupsmsgcontent`
--

DROP TABLE IF EXISTS `verify_user_groupsmsgcontent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `verify_user_groupsmsgcontent` (
  `GM_ID` int(11) NOT NULL,
  `GM_Content` longtext NOT NULL,
  `GM_FromID` int(11) NOT NULL,
  `GM_CreateTime` datetime(6) NOT NULL,
  PRIMARY KEY (`GM_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `verify_user_groupsmsgcontent`
--

LOCK TABLES `verify_user_groupsmsgcontent` WRITE;
/*!40000 ALTER TABLE `verify_user_groupsmsgcontent` DISABLE KEYS */;
/*!40000 ALTER TABLE `verify_user_groupsmsgcontent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `verify_user_groupsmsgtouser`
--

DROP TABLE IF EXISTS `verify_user_groupsmsgtouser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `verify_user_groupsmsgtouser` (
  `GM_ID` int(11) NOT NULL AUTO_INCREMENT,
  `GM_UserID` int(11) NOT NULL,
  `GM_State` tinyint(1) NOT NULL,
  `GM_CreateTime` datetime(6) NOT NULL,
  `GM_GroupMessageID_id` int(11) NOT NULL,
  PRIMARY KEY (`GM_ID`),
  UNIQUE KEY `GM_GroupMessageID_id` (`GM_GroupMessageID_id`),
  CONSTRAINT `verify_user_groupsms_GM_GroupMessageID_id_32ef2b47_fk_verify_us` FOREIGN KEY (`GM_GroupMessageID_id`) REFERENCES `verify_user_groupsmsgcontent` (`GM_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `verify_user_groupsmsgtouser`
--

LOCK TABLES `verify_user_groupsmsgtouser` WRITE;
/*!40000 ALTER TABLE `verify_user_groupsmsgtouser` DISABLE KEYS */;
/*!40000 ALTER TABLE `verify_user_groupsmsgtouser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `verify_user_groupstouser`
--

DROP TABLE IF EXISTS `verify_user_groupstouser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `verify_user_groupstouser` (
  `UG_ID` int(11) NOT NULL AUTO_INCREMENT,
  `UG_CreateTime` datetime(6) NOT NULL,
  `UG_GroupID_id` int(11) NOT NULL,
  PRIMARY KEY (`UG_ID`),
  UNIQUE KEY `UG_GroupID_id` (`UG_GroupID_id`),
  CONSTRAINT `verify_user_groupsto_UG_GroupID_id_e44085ee_fk_verify_us` FOREIGN KEY (`UG_GroupID_id`) REFERENCES `verify_user_group` (`UG_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `verify_user_groupstouser`
--

LOCK TABLES `verify_user_groupstouser` WRITE;
/*!40000 ALTER TABLE `verify_user_groupstouser` DISABLE KEYS */;
/*!40000 ALTER TABLE `verify_user_groupstouser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `verify_user_groupstouser_UG_UserID`
--

DROP TABLE IF EXISTS `verify_user_groupstouser_UG_UserID`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `verify_user_groupstouser_UG_UserID` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_groupstouser_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `verify_user_groupstouser_user_groupstouser_id_use_ef89483d_uniq` (`user_groupstouser_id`,`user_id`),
  KEY `verify_user_groupsto_user_id_bee39ecc_fk_verify_us` (`user_id`),
  CONSTRAINT `verify_user_groupsto_user_groupstouser_id_bd5c43a1_fk_verify_us` FOREIGN KEY (`user_groupstouser_id`) REFERENCES `verify_user_groupstouser` (`UG_ID`),
  CONSTRAINT `verify_user_groupsto_user_id_bee39ecc_fk_verify_us` FOREIGN KEY (`user_id`) REFERENCES `verify_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `verify_user_groupstouser_UG_UserID`
--

LOCK TABLES `verify_user_groupstouser_UG_UserID` WRITE;
/*!40000 ALTER TABLE `verify_user_groupstouser_UG_UserID` DISABLE KEYS */;
/*!40000 ALTER TABLE `verify_user_groupstouser_UG_UserID` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `verify_userinfo`
--

DROP TABLE IF EXISTS `verify_userinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `verify_userinfo` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `nickname` varchar(128) NOT NULL,
  `sex` int(11) NOT NULL,
  `age` int(11) NOT NULL,
  `birthday` varchar(100) DEFAULT NULL,
  `profile_head` varchar(100) DEFAULT NULL,
  `profile` varchar(255) DEFAULT NULL,
  `city_id_id` int(11) NOT NULL,
  `province_id_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`uid`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `verify_userinfo_city_id_id_9c250114_fk_verify_city_C_ID` (`city_id_id`),
  KEY `verify_userinfo_province_id_id_499da4c8_fk_verify_province_P_ID` (`province_id_id`),
  CONSTRAINT `verify_userinfo_city_id_id_9c250114_fk_verify_city_C_ID` FOREIGN KEY (`city_id_id`) REFERENCES `verify_city` (`C_ID`),
  CONSTRAINT `verify_userinfo_province_id_id_499da4c8_fk_verify_province_P_ID` FOREIGN KEY (`province_id_id`) REFERENCES `verify_province` (`P_ID`),
  CONSTRAINT `verify_userinfo_user_id_3a09f6be_fk_verify_user_id` FOREIGN KEY (`user_id`) REFERENCES `verify_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `verify_userinfo`
--

LOCK TABLES `verify_userinfo` WRITE;
/*!40000 ALTER TABLE `verify_userinfo` DISABLE KEYS */;
INSERT INTO `verify_userinfo` VALUES (1,'nsdnf',1,12,'1224','',NULL,1,1,1),(2,'bigben',1,23,'1213','sds',NULL,1,1,2),(3,'bitqu3',1,33,'125413','22sds',NULL,1,1,3);
/*!40000 ALTER TABLE `verify_userinfo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-07  8:56:30
