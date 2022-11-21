-- MySQL dump 10.13  Distrib 5.5.62, for Linux (x86_64)
--
-- Host: localhost    Database: petcharm
-- ------------------------------------------------------
-- Server version	5.5.62-log

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
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comment` (
  `comment_id` int(11) NOT NULL AUTO_INCREMENT,
  `comment_content` varchar(500) DEFAULT NULL,
  `comment_post_id` int(11) DEFAULT NULL,
  `comment_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`comment_id`),
  KEY `comment_post_post_id_fk` (`comment_post_id`),
  KEY `comment_user_user_id_fk` (`comment_user_id`),
  CONSTRAINT `comment_post_post_id_fk` FOREIGN KEY (`comment_post_id`) REFERENCES `post` (`post_id`),
  CONSTRAINT `comment_user_user_id_fk` FOREIGN KEY (`comment_user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hospital`
--

DROP TABLE IF EXISTS `hospital`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hospital` (
  `hospital_id` int(11) NOT NULL AUTO_INCREMENT,
  `hospital_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`hospital_id`),
  UNIQUE KEY `hospital_hospital_id_uindex` (`hospital_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hospital`
--

LOCK TABLES `hospital` WRITE;
/*!40000 ALTER TABLE `hospital` DISABLE KEYS */;
/*!40000 ALTER TABLE `hospital` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pet`
--

DROP TABLE IF EXISTS `pet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pet` (
  `pet_id` int(11) NOT NULL AUTO_INCREMENT,
  `pet_display_name` varchar(100) DEFAULT NULL,
  `pet_type` varchar(100) DEFAULT NULL,
  `pet_breed` varchar(100) DEFAULT NULL,
  `pet_gender` varchar(100) DEFAULT NULL,
  `pet_date_of_birth` datetime DEFAULT NULL,
  PRIMARY KEY (`pet_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pet`
--

LOCK TABLES `pet` WRITE;
/*!40000 ALTER TABLE `pet` DISABLE KEYS */;
/*!40000 ALTER TABLE `pet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post`
--

DROP TABLE IF EXISTS `post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `post` (
  `post_id` int(11) NOT NULL AUTO_INCREMENT,
  `post_content` varchar(500) DEFAULT NULL,
  `post_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`post_id`),
  KEY `post_user_user_id_fk` (`post_user_id`),
  CONSTRAINT `post_user_user_id_fk` FOREIGN KEY (`post_user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post`
--

LOCK TABLES `post` WRITE;
/*!40000 ALTER TABLE `post` DISABLE KEYS */;
/*!40000 ALTER TABLE `post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rating`
--

DROP TABLE IF EXISTS `rating`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rating` (
  `rating_id` int(11) NOT NULL AUTO_INCREMENT,
  `rating_content` varchar(200) DEFAULT NULL,
  `rating_score` int(11) DEFAULT NULL,
  `rating_user_id` int(11) DEFAULT NULL,
  `rating_by_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`rating_id`),
  UNIQUE KEY `rating_rating_id_uindex` (`rating_id`),
  KEY `rating_user_user_id_fk` (`rating_user_id`),
  KEY `rating_user_user_id_fk_2` (`rating_by_user_id`),
  CONSTRAINT `rating_user_user_id_fk` FOREIGN KEY (`rating_user_id`) REFERENCES `user` (`user_id`),
  CONSTRAINT `rating_user_user_id_fk_2` FOREIGN KEY (`rating_by_user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rating`
--

LOCK TABLES `rating` WRITE;
/*!40000 ALTER TABLE `rating` DISABLE KEYS */;
/*!40000 ALTER TABLE `rating` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `service`
--

DROP TABLE IF EXISTS `service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `service` (
  `service_id` int(11) NOT NULL AUTO_INCREMENT,
  `service_name` varchar(100) DEFAULT NULL,
  `service_content` varchar(500) DEFAULT NULL,
  `service_price` decimal(10,2) DEFAULT NULL,
  `service_type` varchar(100) DEFAULT NULL,
  `service_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`service_id`),
  UNIQUE KEY `service_service_id_uindex` (`service_id`),
  KEY `service_user_user_id_fk` (`service_user_id`),
  CONSTRAINT `service_user_user_id_fk` FOREIGN KEY (`service_user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `service`
--

LOCK TABLES `service` WRITE;
/*!40000 ALTER TABLE `service` DISABLE KEYS */;
/*!40000 ALTER TABLE `service` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `star`
--

DROP TABLE IF EXISTS `star`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `star` (
  `star_id` int(11) NOT NULL AUTO_INCREMENT,
  `star_user_id` int(11) DEFAULT NULL,
  `star_by_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`star_id`),
  UNIQUE KEY `star_star_id_uindex` (`star_id`),
  KEY `star_user_user_id_fk` (`star_user_id`),
  KEY `star_user_user_id_fk_2` (`star_by_user_id`),
  CONSTRAINT `star_user_user_id_fk` FOREIGN KEY (`star_user_id`) REFERENCES `user` (`user_id`),
  CONSTRAINT `star_user_user_id_fk_2` FOREIGN KEY (`star_by_user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `star`
--

LOCK TABLES `star` WRITE;
/*!40000 ALTER TABLE `star` DISABLE KEYS */;
/*!40000 ALTER TABLE `star` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(100) NOT NULL,
  `user_display_name` varchar(100) DEFAULT NULL,
  `user_password` varchar(100) DEFAULT NULL,
  `user_type` varchar(100) DEFAULT NULL,
  `pet_id` int(11) DEFAULT NULL,
  `user_icon_url` varchar(200) DEFAULT NULL,
  `user_email` varchar(100) DEFAULT NULL,
  `user_phone_number` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `user_user_name_uindex` (`user_name`),
  KEY `user_pet_pet_id_fk` (`pet_id`),
  CONSTRAINT `user_pet_pet_id_fk` FOREIGN KEY (`pet_id`) REFERENCES `pet` (`pet_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vet_hospital`
--

DROP TABLE IF EXISTS `vet_hospital`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vet_hospital` (
  `vet_hospital_id` int(11) DEFAULT NULL,
  `vet_id` int(11) NOT NULL DEFAULT '0',
  `hospital_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`vet_id`,`hospital_id`),
  KEY `vet_hospital_hospital_hospital_id_fk` (`hospital_id`),
  CONSTRAINT `vet_hospital_hospital_hospital_id_fk` FOREIGN KEY (`hospital_id`) REFERENCES `hospital` (`hospital_id`),
  CONSTRAINT `vet_hospital_user_user_id_fk` FOREIGN KEY (`vet_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vet_hospital`
--

LOCK TABLES `vet_hospital` WRITE;
/*!40000 ALTER TABLE `vet_hospital` DISABLE KEYS */;
/*!40000 ALTER TABLE `vet_hospital` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `walk_point`
--

DROP TABLE IF EXISTS `walk_point`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `walk_point` (
  `walk_point_id` int(11) NOT NULL AUTO_INCREMENT,
  `walk_point_x` double DEFAULT NULL,
  `walk_point_y` double DEFAULT NULL,
  `walk_point_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`walk_point_id`),
  UNIQUE KEY `walk_point_walk_point_id_uindex` (`walk_point_id`),
  KEY `walk_point_user_user_id_fk` (`walk_point_user_id`),
  CONSTRAINT `walk_point_user_user_id_fk` FOREIGN KEY (`walk_point_user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `walk_point`
--

LOCK TABLES `walk_point` WRITE;
/*!40000 ALTER TABLE `walk_point` DISABLE KEYS */;
/*!40000 ALTER TABLE `walk_point` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'petcharm'
--

--
-- Dumping routines for database 'petcharm'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-21 16:47:21
