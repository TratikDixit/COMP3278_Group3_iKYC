-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Feb 17, 2020 at 09:41 PM
-- Server version: 5.7.28-0ubuntu0.18.04.4
-- PHP Version: 7.2.24-0ubuntu0.18.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `facerecognition`
--

-- --------------------------------------------------------

--
-- Table structure for table `Customer`
--
DROP TABLE IF EXISTS `Customer`;

# Create TABLE 'Customer'
CREATE TABLE `Customer` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `middle_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `custom_message` varchar(200) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--LOCK TABLES `Customer` WRITE;
/*!40000 ALTER TABLE `Customer` DISABLE KEYS */;
--INSERT INTO `Customer` VALUES (1, "JACK", NOW(), '2021-09-01');
/*!40000 ALTER TABLE `Customer` ENABLE KEYS */;
--UNLOCK TABLES;

DROP TABLE IF EXISTS `LoginHistory`;

# Create TABLE 'LoginHistory'
CREATE TABLE `LoginHistory` (
  `username` varchar(50) NOT NULL,
  `date_time` datetime NOT NULL,
  FOREIGN KEY (`username`) REFERENCES `Customer` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `Account`;

# Create TABLE 'Account'
CREATE TABLE `Account` (
  `account_number` INT NOT NULL,
  `username` varchar(50) NOT NULL,
  `account_type` ENUM('Current','Saving') NOT NULL,
  `currency` varchar(3) NOT NULL,
  `balance` DECIMAL(50,2) NOT NULL,
  PRIMARY KEY (`account_number`)
  FOREIGN KEY (`username`) REFERENCES `Customer` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `Transaction`;

# Create TABLE 'Transaction'
CREATE TABLE `Transaction` (
  `transaction_id` varchar(25) NOT NULL,
  `amount` DECIMAL(50,2) NOT NULL,
  `date_time` datetime NOT NULL,
  `from_account` INT NOT NULL,
  `to_account` INT NOT NULL,
  PRIMARY KEY (`transaction_id`)
  FOREIGN KEY (`from_account`) REFERENCES `Account` (`account_number`)
  FOREIGN KEY (`to_account`) REFERENCES `Account` (`account_number`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

# Create other TABLE...


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
