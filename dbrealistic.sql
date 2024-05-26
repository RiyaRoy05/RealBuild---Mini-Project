/*
SQLyog Ultimate v11.33 (64 bit)
MySQL - 5.5.8-log : Database - dbrealistic
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`dbrealistic` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `dbrealistic`;

/*Table structure for table `account` */

DROP TABLE IF EXISTS `account`;

CREATE TABLE `account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `u_id` varchar(110) NOT NULL,
  `acc_no` varchar(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `card_no` varchar(25) NOT NULL,
  `cvv` int(11) NOT NULL,
  `exp_date` varchar(15) NOT NULL,
  `upi` int(11) NOT NULL,
  `bal` int(11) NOT NULL,
  `st` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Table structure for table `booking` */

DROP TABLE IF EXISTS `booking`;

CREATE TABLE `booking` (
  `bid` int(11) NOT NULL AUTO_INCREMENT,
  `sid` varchar(90) NOT NULL,
  `pid` varchar(90) NOT NULL,
  `q` varchar(90) NOT NULL,
  `uid` varchar(90) NOT NULL,
  PRIMARY KEY (`bid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `subject` varchar(50) NOT NULL,
  `feedback` varchar(50) NOT NULL,
  `uid` varchar(50) NOT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `sid` varchar(90) NOT NULL,
  `pname` varchar(90) NOT NULL,
  `price` varchar(90) NOT NULL,
  `description` varchar(90) NOT NULL,
  `image` varchar(90) NOT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Table structure for table `tblallocation` */

DROP TABLE IF EXISTS `tblallocation`;

CREATE TABLE `tblallocation` (
  `allocid` int(11) NOT NULL AUTO_INCREMENT,
  `requid` varchar(50) NOT NULL,
  `archid` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`allocid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Table structure for table `tblarchitect` */

DROP TABLE IF EXISTS `tblarchitect`;

CREATE TABLE `tblarchitect` (
  `aName` varchar(50) NOT NULL,
  `aAddress` varchar(100) NOT NULL,
  `aContact` varchar(50) NOT NULL,
  `aEmail` varchar(50) NOT NULL,
  `aPhoto` varchar(100) NOT NULL,
  `aqualification` varchar(500) NOT NULL,
  `aqproof` varchar(500) NOT NULL,
  PRIMARY KEY (`aEmail`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Table structure for table `tblcontractor` */

DROP TABLE IF EXISTS `tblcontractor`;

CREATE TABLE `tblcontractor` (
  `cName` varchar(50) NOT NULL,
  `cAddress` varchar(100) NOT NULL,
  `cContact` varchar(50) NOT NULL,
  `cEmail` varchar(50) NOT NULL,
  `cPhoto` varchar(100) NOT NULL,
  `cprework` varchar(500) NOT NULL,
  PRIMARY KEY (`cEmail`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Table structure for table `tblcustomer` */

DROP TABLE IF EXISTS `tblcustomer`;

CREATE TABLE `tblcustomer` (
  `cName` varchar(50) NOT NULL,
  `cAddress` varchar(50) NOT NULL,
  `cContact` varchar(50) NOT NULL,
  `cEmail` varchar(50) NOT NULL,
  `aadhar` varchar(500) NOT NULL,
  PRIMARY KEY (`cEmail`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Table structure for table `tbldesigner` */

DROP TABLE IF EXISTS `tbldesigner`;

CREATE TABLE `tbldesigner` (
  `dName` varchar(50) NOT NULL,
  `dAddress` varchar(100) NOT NULL,
  `dContact` varchar(50) NOT NULL,
  `dEmail` varchar(50) NOT NULL,
  `dPhoto` varchar(100) NOT NULL,
  `dqualification` varchar(500) NOT NULL,
  `dqproof` varchar(500) NOT NULL,
  PRIMARY KEY (`dEmail`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Table structure for table `tbldesignrequest` */

DROP TABLE IF EXISTS `tbldesignrequest`;

CREATE TABLE `tbldesignrequest` (
  `dreqId` int(11) NOT NULL AUTO_INCREMENT,
  `planId` int(11) NOT NULL,
  `dEmail` varchar(50) NOT NULL,
  `dreqStatus` varchar(50) NOT NULL,
  PRIMARY KEY (`dreqId`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Table structure for table `tbllogin` */

DROP TABLE IF EXISTS `tbllogin`;

CREATE TABLE `tbllogin` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `utype` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Table structure for table `tblplan` */

DROP TABLE IF EXISTS `tblplan`;

CREATE TABLE `tblplan` (
  `planId` int(11) NOT NULL AUTO_INCREMENT,
  `aEmail` varchar(50) NOT NULL,
  `reqId` int(11) NOT NULL,
  `plan` varchar(100) NOT NULL,
  `sqft` int(11) NOT NULL,
  `cost` bigint(20) NOT NULL,
  `planStatus` varchar(50) NOT NULL,
  `fees` int(11) NOT NULL,
  `feesstatus` varchar(11) NOT NULL,
  PRIMARY KEY (`planId`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Table structure for table `tblrequirement` */

DROP TABLE IF EXISTS `tblrequirement`;

CREATE TABLE `tblrequirement` (
  `reqId` int(11) NOT NULL AUTO_INCREMENT,
  `cEmail` varchar(50) NOT NULL,
  `bedroom` varchar(50) NOT NULL,
  `bathroom` varchar(50) NOT NULL,
  `attached` varchar(50) NOT NULL,
  `carporch` varchar(50) NOT NULL,
  `kitchen` varchar(50) NOT NULL,
  `sitout` varchar(50) NOT NULL,
  `workarea` varchar(50) NOT NULL,
  `floor` varchar(50) NOT NULL,
  `sqft` varchar(50) NOT NULL,
  `other` varchar(100) NOT NULL,
  `reqDate` datetime NOT NULL,
  `reqStatus` varchar(50) NOT NULL,
  PRIMARY KEY (`reqId`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Table structure for table `tblvideo` */

DROP TABLE IF EXISTS `tblvideo`;

CREATE TABLE `tblvideo` (
  `videoId` int(11) NOT NULL AUTO_INCREMENT,
  `dreqId` int(11) NOT NULL,
  `video` varchar(100) NOT NULL,
  `videoStatus` varchar(50) NOT NULL,
  `amount` int(11) NOT NULL,
  `paymentstatus` varchar(50) NOT NULL,
  PRIMARY KEY (`videoId`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Table structure for table `tblwork` */

DROP TABLE IF EXISTS `tblwork`;

CREATE TABLE `tblwork` (
  `workId` int(11) NOT NULL AUTO_INCREMENT,
  `videoId` int(11) NOT NULL,
  `cEmail` varchar(50) NOT NULL,
  `wDate` date NOT NULL,
  `wStatus` varchar(50) NOT NULL,
  `cost` int(11) NOT NULL,
  PRIMARY KEY (`workId`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
