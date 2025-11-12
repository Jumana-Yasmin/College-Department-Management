/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - mes_dpt_mgt
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`mes_dpt_mgt` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `mes_dpt_mgt`;

/*Table structure for table `attendance` */

DROP TABLE IF EXISTS `attendance`;

CREATE TABLE `attendance` (
  `attendance_id` int(11) NOT NULL AUTO_INCREMENT,
  `stud_id` int(11) DEFAULT NULL,
  `attendance` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `period` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`attendance_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `attendance` */

insert  into `attendance`(`attendance_id`,`stud_id`,`attendance`,`date`,`period`) values 
(1,1,'present','2023-11-18',NULL),
(2,19,'present','2023-11-18',NULL),
(3,1,'present','2023-11-18','1'),
(4,3,'present','2023-11-25','2');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) DEFAULT NULL,
  `complaint` varchar(50) DEFAULT NULL,
  `reply` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`sender_id`,`complaint`,`reply`,`date`) values 
(1,2,'hgvhg','yrdydtyd','12-02-2022'),
(2,6,'gfg','done','16-02-2022'),
(3,7,'hgvjg','okay, i wiil manage it','18-02-2022'),
(4,8,'hfyhvj','pending','11-02-2022'),
(5,11,'fsfsvsdvsd','pending','2023-02-13 17:14:50'),
(6,11,'sdcfvgbhn','zsexdcfgv bh','2023-11-18 09:23:55'),
(7,6,'adfsdf','pending','2023-11-18 09:59:27'),
(8,1,'e5rtydty','pending','2023-11-18 10:13:06'),
(9,6,'tgv ','pending','2023-11-18 12:28:09');

/*Table structure for table `department` */

DROP TABLE IF EXISTS `department`;

CREATE TABLE `department` (
  `dept_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `d_name` varchar(50) DEFAULT NULL,
  `d_phone` varchar(50) DEFAULT NULL,
  `d_mail` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`dept_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `department` */

insert  into `department`(`dept_id`,`login_id`,`d_name`,`d_phone`,`d_mail`) values 
(1,2,'chemistry','986265298','mi@mailazsx'),
(2,3,'physics','15487415','gbg@rfg'),
(3,4,'botony','741852955','botony@gmail.com');

/*Table structure for table `faculty` */

DROP TABLE IF EXISTS `faculty`;

CREATE TABLE `faculty` (
  `fac_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `dept_id` int(11) DEFAULT NULL,
  `f_name` varchar(50) DEFAULT NULL,
  `f_address` varchar(50) DEFAULT NULL,
  `f_phone` varchar(50) DEFAULT NULL,
  `f_mail` varchar(50) DEFAULT NULL,
  `f_qualification` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`fac_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `faculty` */

insert  into `faculty`(`fac_id`,`login_id`,`dept_id`,`f_name`,`f_address`,`f_phone`,`f_mail`,`f_qualification`) values 
(1,6,2,'neha','sgsg','ssg','gsgs@grwc','s vjdf kdfdqe'),
(2,10,2,'liya','fjsbvjdbks','dsnksdnksdnk','sdcdskjds','sdnlsvnldsvndv'),
(3,11,2,'devika',';;wmflmlwzsd','12345678','devika@gmail.com','bsc'),
(4,14,1,'shine','thalore','1234567877','shin@gmail.com','Btech');

/*Table structure for table `fee` */

DROP TABLE IF EXISTS `fee`;

CREATE TABLE `fee` (
  `fee_id` int(11) NOT NULL AUTO_INCREMENT,
  `dept_id` int(11) DEFAULT NULL,
  `fee` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`fee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Data for the table `fee` */

insert  into `fee`(`fee_id`,`dept_id`,`fee`) values 
(1,1,'150000'),
(2,2,'200000'),
(3,3,'20000'),
(4,5,'400050'),
(5,7,'50000');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `stud_id` int(11) DEFAULT NULL,
  `feedback` varchar(222) DEFAULT NULL,
  `date` varchar(222) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`stud_id`,`feedback`,`date`) values 
(1,1,'segfsdgsdg','2023-11-18'),
(2,1,'zxrdctfvygbuhn','2023-11-18');

/*Table structure for table `leave` */

DROP TABLE IF EXISTS `leave`;

CREATE TABLE `leave` (
  `leave_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `reason` varchar(100) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `user_type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`leave_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

/*Data for the table `leave` */

insert  into `leave`(`leave_id`,`sender_id`,`date`,`reason`,`status`,`user_type`) values 
(1,11,'12','bjbjm','reject','faculty'),
(2,11,'2023-02-28','sdgdbdfdsvs','reject','faculty'),
(3,13,'2023-02-16','sdvdvdfdbv dxdf','approved','student'),
(4,11,'2023-11-03','marriage','approved','faculty'),
(5,6,'','arwestxdcfhgvjh','reject','faculty'),
(6,6,'2023-11-30','function','pending','faculty'),
(7,7,'2023-11-29','qazsexdfc','pending','student');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varbinary(50) DEFAULT NULL,
  `usertype` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(2,'chemistry','chemistry','department'),
(3,'physics','physics','department'),
(4,'botony','botony','department'),
(5,'bca','bca','department'),
(6,'staff1','staff1','faculty'),
(7,'fayas','stud1','student'),
(10,'liya','liya','faculty'),
(11,'devika','devika','faculty'),
(12,'mariyu','mariyu','student'),
(13,'sheza','sheza','student'),
(14,'shine','shine','faculty'),
(31,'jum','jum','faculty'),
(32,'rono','rono','student');

/*Table structure for table `request_scholarship` */

DROP TABLE IF EXISTS `request_scholarship`;

CREATE TABLE `request_scholarship` (
  `app_id` int(11) NOT NULL AUTO_INCREMENT,
  `stud_id` int(11) DEFAULT NULL,
  `dept_id` int(11) DEFAULT NULL,
  `documents` varchar(200) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `scholarship_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`app_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `request_scholarship` */

/*Table structure for table `result` */

DROP TABLE IF EXISTS `result`;

CREATE TABLE `result` (
  `result_id` int(11) NOT NULL AUTO_INCREMENT,
  `stud_id` int(11) DEFAULT NULL,
  `sub_id` int(11) DEFAULT NULL,
  `mark_awarded` varchar(20) DEFAULT NULL,
  `grand_total` varchar(20) DEFAULT NULL,
  `result` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`result_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `result` */

insert  into `result`(`result_id`,`stud_id`,`sub_id`,`mark_awarded`,`grand_total`,`result`) values 
(1,1,1,'85','200','pass'),
(2,1,5,'55','155','pass');

/*Table structure for table `scholarship` */

DROP TABLE IF EXISTS `scholarship`;

CREATE TABLE `scholarship` (
  `scholarship_id` int(11) NOT NULL AUTO_INCREMENT,
  `details` varchar(50) DEFAULT NULL,
  `scholarship` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`scholarship_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `scholarship` */

insert  into `scholarship`(`scholarship_id`,`details`,`scholarship`) values 
(2,'qqqqqqqqqqqqqqqqqqq','aaaaaaaaaaqqqqqqqqqqqq');

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `stud_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `s_name` varchar(50) DEFAULT NULL,
  `s_address` varchar(50) DEFAULT NULL,
  `s_phone` varchar(50) DEFAULT NULL,
  `s_mail` varchar(50) DEFAULT NULL,
  `dept_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`stud_id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4;

/*Data for the table `student` */

insert  into `student`(`stud_id`,`login_id`,`s_name`,`s_address`,`s_phone`,`s_mail`,`dept_id`) values 
(1,7,'fayas','asdnbd','dfvd','sfbsdbvs',2),
(2,8,'qwe','dfs','ssg','sgw@g',2),
(3,12,'mariyu','svsdvdshj','ksjdnvkdsj','dskjvnks',2),
(4,13,'sheza','ewfesksjn','msldkmvls','v kdsv kdsv ',2),
(19,32,'ronald jose','meleth','21323534','rono@gmail.com',2);

/*Table structure for table `subject` */

DROP TABLE IF EXISTS `subject`;

CREATE TABLE `subject` (
  `sub_id` int(11) NOT NULL AUTO_INCREMENT,
  `sub_name` varchar(50) DEFAULT NULL,
  `fac_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`sub_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Data for the table `subject` */

insert  into `subject`(`sub_id`,`sub_name`,`fac_id`) values 
(1,'english',1),
(2,'English',1),
(3,'sdvsdv',3),
(4,'quantum chemistry',4),
(5,'quantum physics',3);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
