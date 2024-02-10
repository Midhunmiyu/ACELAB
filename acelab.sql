-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: acelab
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add user',6,'add_login'),(22,'Can change user',6,'change_login'),(23,'Can delete user',6,'delete_login'),(24,'Can view user',6,'view_login'),(25,'Can add department',7,'add_department'),(26,'Can change department',7,'change_department'),(27,'Can delete department',7,'delete_department'),(28,'Can view department',7,'view_department'),(29,'Can add doc schedule',8,'add_docschedule'),(30,'Can change doc schedule',8,'change_docschedule'),(31,'Can delete doc schedule',8,'delete_docschedule'),(32,'Can view doc schedule',8,'view_docschedule'),(33,'Can add doctor notification',9,'add_doctornotification'),(34,'Can change doctor notification',9,'change_doctornotification'),(35,'Can delete doctor notification',9,'delete_doctornotification'),(36,'Can view doctor notification',9,'view_doctornotification'),(37,'Can add patient notification',10,'add_patientnotification'),(38,'Can change patient notification',10,'change_patientnotification'),(39,'Can delete patient notification',10,'delete_patientnotification'),(40,'Can view patient notification',10,'view_patientnotification'),(41,'Can add doctor',11,'add_doctor'),(42,'Can change doctor',11,'change_doctor'),(43,'Can delete doctor',11,'delete_doctor'),(44,'Can view doctor',11,'view_doctor'),(45,'Can add patient',12,'add_patient'),(46,'Can change patient',12,'change_patient'),(47,'Can delete patient',12,'delete_patient'),(48,'Can view patient',12,'view_patient'),(49,'Can add feedback',13,'add_feedback'),(50,'Can change feedback',13,'change_feedback'),(51,'Can delete feedback',13,'delete_feedback'),(52,'Can view feedback',13,'view_feedback'),(53,'Can add appointment',14,'add_appointment'),(54,'Can change appointment',14,'change_appointment'),(55,'Can delete appointment',14,'delete_appointment'),(56,'Can view appointment',14,'view_appointment'),(57,'Can add patient data',15,'add_patientdata'),(58,'Can change patient data',15,'change_patientdata'),(59,'Can delete patient data',15,'delete_patientdata'),(60,'Can view patient data',15,'view_patientdata');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_home_login_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_home_login_id` FOREIGN KEY (`user_id`) REFERENCES `home_login` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(14,'home','appointment'),(7,'home','department'),(8,'home','docschedule'),(11,'home','doctor'),(9,'home','doctornotification'),(13,'home','feedback'),(6,'home','login'),(12,'home','patient'),(15,'home','patientdata'),(10,'home','patientnotification'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-02-10 16:37:34.768958'),(2,'contenttypes','0002_remove_content_type_name','2024-02-10 16:37:34.904779'),(3,'auth','0001_initial','2024-02-10 16:37:35.254949'),(4,'auth','0002_alter_permission_name_max_length','2024-02-10 16:37:35.368977'),(5,'auth','0003_alter_user_email_max_length','2024-02-10 16:37:35.380969'),(6,'auth','0004_alter_user_username_opts','2024-02-10 16:37:35.393962'),(7,'auth','0005_alter_user_last_login_null','2024-02-10 16:37:35.408954'),(8,'auth','0006_require_contenttypes_0002','2024-02-10 16:37:35.418947'),(9,'auth','0007_alter_validators_add_error_messages','2024-02-10 16:37:35.439935'),(10,'auth','0008_alter_user_username_max_length','2024-02-10 16:37:35.456925'),(11,'auth','0009_alter_user_last_name_max_length','2024-02-10 16:37:35.475912'),(12,'auth','0010_alter_group_name_max_length','2024-02-10 16:37:35.524882'),(13,'auth','0011_update_proxy_permissions','2024-02-10 16:37:35.541875'),(14,'auth','0012_alter_user_first_name_max_length','2024-02-10 16:37:35.560860'),(15,'home','0001_initial','2024-02-10 16:37:36.637829'),(16,'admin','0001_initial','2024-02-10 16:37:36.812621'),(17,'admin','0002_logentry_remove_auto_add','2024-02-10 16:37:36.844864'),(18,'admin','0003_logentry_add_action_flag_choices','2024-02-10 16:37:36.874846'),(19,'home','0002_alter_patient_aadhar_number','2024-02-10 16:37:37.024752'),(20,'sessions','0001_initial','2024-02-10 16:37:37.065186');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_appointment`
--

DROP TABLE IF EXISTS `home_appointment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_appointment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` int NOT NULL,
  `Schedule_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `home_appointment_Schedule_id_daf69398_fk_home_docschedule_id` (`Schedule_id`),
  KEY `home_appointment_user_id_0cd8b1ec_fk_home_patient_id` (`user_id`),
  CONSTRAINT `home_appointment_Schedule_id_daf69398_fk_home_docschedule_id` FOREIGN KEY (`Schedule_id`) REFERENCES `home_docschedule` (`id`),
  CONSTRAINT `home_appointment_user_id_0cd8b1ec_fk_home_patient_id` FOREIGN KEY (`user_id`) REFERENCES `home_patient` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_appointment`
--

LOCK TABLES `home_appointment` WRITE;
/*!40000 ALTER TABLE `home_appointment` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_appointment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_department`
--

DROP TABLE IF EXISTS `home_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_department` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `dept_name` varchar(100) NOT NULL,
  `dept_desc` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_department`
--

LOCK TABLES `home_department` WRITE;
/*!40000 ALTER TABLE `home_department` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_docschedule`
--

DROP TABLE IF EXISTS `home_docschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_docschedule` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Date` date NOT NULL,
  `Start_time` time(6) NOT NULL,
  `End_time` time(6) NOT NULL,
  `Doc_name_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `home_docschedule_Doc_name_id_982bcfe7_fk_home_doctor_user_id` (`Doc_name_id`),
  CONSTRAINT `home_docschedule_Doc_name_id_982bcfe7_fk_home_doctor_user_id` FOREIGN KEY (`Doc_name_id`) REFERENCES `home_doctor` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_docschedule`
--

LOCK TABLES `home_docschedule` WRITE;
/*!40000 ALTER TABLE `home_docschedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_docschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_doctor`
--

DROP TABLE IF EXISTS `home_doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_doctor` (
  `user_id` bigint NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `Image` varchar(100) NOT NULL,
  `status` int NOT NULL,
  `department_id` bigint NOT NULL,
  PRIMARY KEY (`user_id`),
  KEY `home_doctor_department_id_eb682975_fk_home_department_id` (`department_id`),
  CONSTRAINT `home_doctor_department_id_eb682975_fk_home_department_id` FOREIGN KEY (`department_id`) REFERENCES `home_department` (`id`),
  CONSTRAINT `home_doctor_user_id_12f5b0c1_fk_home_login_id` FOREIGN KEY (`user_id`) REFERENCES `home_login` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_doctor`
--

LOCK TABLES `home_doctor` WRITE;
/*!40000 ALTER TABLE `home_doctor` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_doctornotification`
--

DROP TABLE IF EXISTS `home_doctornotification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_doctornotification` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `subject` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_doctornotification`
--

LOCK TABLES `home_doctornotification` WRITE;
/*!40000 ALTER TABLE `home_doctornotification` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_doctornotification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_feedback`
--

DROP TABLE IF EXISTS `home_feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_feedback` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `feedback` varchar(200) NOT NULL,
  `date` date NOT NULL,
  `reply` longtext,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `home_feedback_user_id_56f97b5a_fk_home_login_id` (`user_id`),
  CONSTRAINT `home_feedback_user_id_56f97b5a_fk_home_login_id` FOREIGN KEY (`user_id`) REFERENCES `home_login` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_feedback`
--

LOCK TABLES `home_feedback` WRITE;
/*!40000 ALTER TABLE `home_feedback` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_login`
--

DROP TABLE IF EXISTS `home_login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_login` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `is_doctor` tinyint(1) NOT NULL,
  `is_patient` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_login`
--

LOCK TABLES `home_login` WRITE;
/*!40000 ALTER TABLE `home_login` DISABLE KEYS */;
INSERT INTO `home_login` VALUES (1,'pbkdf2_sha256$390000$jJOPsikpRna5mQLH41otGE$Mo9M9vP0gSO2EpLBUmEneH5e9lOALeWlawAELF7FtJ4=',NULL,1,'admin','','','',1,1,'2024-02-10 16:38:07.345570',0,0);
/*!40000 ALTER TABLE `home_login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_login_groups`
--

DROP TABLE IF EXISTS `home_login_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_login_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `login_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `home_login_groups_login_id_group_id_4360ad36_uniq` (`login_id`,`group_id`),
  KEY `home_login_groups_group_id_348e5d11_fk_auth_group_id` (`group_id`),
  CONSTRAINT `home_login_groups_group_id_348e5d11_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `home_login_groups_login_id_1c70a0a1_fk_home_login_id` FOREIGN KEY (`login_id`) REFERENCES `home_login` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_login_groups`
--

LOCK TABLES `home_login_groups` WRITE;
/*!40000 ALTER TABLE `home_login_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_login_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_login_user_permissions`
--

DROP TABLE IF EXISTS `home_login_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_login_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `login_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `home_login_user_permissions_login_id_permission_id_bd701345_uniq` (`login_id`,`permission_id`),
  KEY `home_login_user_perm_permission_id_b152caac_fk_auth_perm` (`permission_id`),
  CONSTRAINT `home_login_user_perm_permission_id_b152caac_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `home_login_user_permissions_login_id_021329d0_fk_home_login_id` FOREIGN KEY (`login_id`) REFERENCES `home_login` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_login_user_permissions`
--

LOCK TABLES `home_login_user_permissions` WRITE;
/*!40000 ALTER TABLE `home_login_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_login_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_patient`
--

DROP TABLE IF EXISTS `home_patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_patient` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `aadhar_number` varchar(12) NOT NULL,
  `email` varchar(254) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `home_patient_aadhar_number_46ca683c_uniq` (`aadhar_number`),
  KEY `home_patient_user_id_163213ac_fk_home_login_id` (`user_id`),
  CONSTRAINT `home_patient_user_id_163213ac_fk_home_login_id` FOREIGN KEY (`user_id`) REFERENCES `home_login` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_patient`
--

LOCK TABLES `home_patient` WRITE;
/*!40000 ALTER TABLE `home_patient` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_patientdata`
--

DROP TABLE IF EXISTS `home_patientdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_patientdata` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Title` varchar(100) NOT NULL,
  `P_data` varchar(100) NOT NULL,
  `user_id` bigint NOT NULL,
  `Doc_name_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `home_patientdata_user_id_a75c06e7_fk_home_login_id` (`user_id`),
  KEY `home_patientdata_Doc_name_id_8626f1b3_fk_home_doctor_user_id` (`Doc_name_id`),
  CONSTRAINT `home_patientdata_Doc_name_id_8626f1b3_fk_home_doctor_user_id` FOREIGN KEY (`Doc_name_id`) REFERENCES `home_doctor` (`user_id`),
  CONSTRAINT `home_patientdata_user_id_a75c06e7_fk_home_login_id` FOREIGN KEY (`user_id`) REFERENCES `home_login` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_patientdata`
--

LOCK TABLES `home_patientdata` WRITE;
/*!40000 ALTER TABLE `home_patientdata` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_patientdata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_patientnotification`
--

DROP TABLE IF EXISTS `home_patientnotification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_patientnotification` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `subject` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_patientnotification`
--

LOCK TABLES `home_patientnotification` WRITE;
/*!40000 ALTER TABLE `home_patientnotification` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_patientnotification` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-10 22:10:13
