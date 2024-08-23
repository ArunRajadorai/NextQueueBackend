-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               11.4.2-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             12.6.0.6765
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumping structure for table virtualqueue.auth_token
CREATE TABLE IF NOT EXISTS `auth_token` (
  `Authid` int(11) NOT NULL AUTO_INCREMENT,
  `App_name` varchar(50) DEFAULT NULL,
  `App_password` varchar(50) DEFAULT NULL,
  `access_token` varchar(255) DEFAULT NULL,
  `request_time` datetime DEFAULT NULL,
  PRIMARY KEY (`Authid`),
  KEY `ix_auth_token_request_time` (`request_time`),
  KEY `ix_auth_token_access_token` (`access_token`),
  KEY `ix_auth_token_App_password` (`App_password`),
  KEY `ix_auth_token_App_name` (`App_name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table virtualqueue.auth_token: ~5 rows (approximately)
INSERT INTO `auth_token` (`Authid`, `App_name`, `App_password`, `access_token`, `request_time`) VALUES
	(1, 'nextQueue', 'v1', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBfbmFtZSI6Im5leHRRdWV1ZSIsImFwcF9wYXNzd29yZCI6InYxIiwiZXhwIjoxNzIwNzA3MjIyfQ._UeZj6pc4H1t7GjZP-8plsVwEKi42ZQ_vbY3AsII-J0', '2024-07-11 13:43:42'),
	(2, 'nextQueue', 'v1', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBfbmFtZSI6Im5leHRRdWV1ZSIsImFwcF9wYXNzd29yZCI6InYxIiwiZXhwIjoxNzIxMDQ1NDUyfQ.7cJWIQ9GgItGz4m4L8fcviOv221LlA3htsQo_QDvi0c', '2024-07-15 11:40:52'),
	(3, 'nextQueue', 'v1', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBfbmFtZSI6Im5leHRRdWV1ZSIsImFwcF9wYXNzd29yZCI6InYxIiwiZXhwIjoxNzIxMDUwMTUyfQ.5I077--0uqGNeYGSz-iCWCFIdsYnOh_jWTKe7NHdx7Y', '2024-07-15 11:49:12'),
	(4, 'nextQueue', 'v1', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBfbmFtZSI6Im5leHRRdWV1ZSIsImFwcF9wYXNzd29yZCI6InYxIiwiZXhwIjoxNzIxMDUwMTg3fQ.ZqJHJ76L-kUwYRwZv7mootK4G4VHw_7gstkt-NgzPg0', '2024-07-15 11:49:47'),
	(5, 'nextQueue', 'v1', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBfbmFtZSI6Im5leHRRdWV1ZSIsImFwcF9wYXNzd29yZCI6InYxIiwiZXhwIjoxNzIxMDUwMjI0fQ.VSmseaJmYN_NS_MtUupMGywXUdNgXqPpD7yZYfjLYmw', '2024-07-15 11:50:24');

-- Dumping structure for table virtualqueue.company
CREATE TABLE IF NOT EXISTS `company` (
  `CompanyID` int(11) NOT NULL AUTO_INCREMENT,
  `CompanyName` varchar(100) DEFAULT NULL,
  `CompanyOwnerName` varchar(100) DEFAULT NULL,
  `PhoneNumber` varchar(100) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Address` varchar(100) DEFAULT NULL,
  `Address2` varchar(100) DEFAULT NULL,
  `Town` varchar(100) DEFAULT NULL,
  `PostalCode` varchar(100) DEFAULT NULL,
  `State` varchar(100) DEFAULT NULL,
  `Country` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`CompanyID`),
  KEY `ix_company_Email` (`Email`),
  KEY `ix_company_CompanyID` (`CompanyID`),
  KEY `ix_company_PostalCode` (`PostalCode`),
  KEY `ix_company_Address` (`Address`),
  KEY `ix_company_CompanyOwnerName` (`CompanyOwnerName`),
  KEY `ix_company_State` (`State`),
  KEY `ix_company_Address2` (`Address2`),
  KEY `ix_company_Country` (`Country`),
  KEY `ix_company_PhoneNumber` (`PhoneNumber`),
  KEY `ix_company_Town` (`Town`),
  KEY `ix_company_CompanyName` (`CompanyName`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table virtualqueue.company: ~9 rows (approximately)
INSERT INTO `company` (`CompanyID`, `CompanyName`, `CompanyOwnerName`, `PhoneNumber`, `Email`, `Address`, `Address2`, `Town`, `PostalCode`, `State`, `Country`) VALUES
	(3, 'ADS Security Solutions Inc.', 'Alice Johnson', '+1-800-555-1234', 'contact@techinnovators.com', '123 Tech Lane', 'Suite 100', 'San Francisco', '94107', 'California', 'USA'),
	(4, 'KRL Ltd.', 'Bob Smith', '+1-800-555-5678', 'info@greensolutions.com', '456 Green Street', NULL, 'Seattle', '98101', 'Washington', 'USA'),
	(6, 'Health Partners', 'Diana Adams', '+1-800-555-4321', 'support@healthpartners.com', '101 Health Drive', NULL, 'Chicago', '60614', 'Illinois', 'USA'),
	(7, 'EduTech Solutions', 'Edward Lee', '+1-800-555-6789', 'admin@edutechsolutions.com', '202 Education Blvd', 'Suite 301', 'Boston', '02115', 'Massachusetts', 'USA'),
	(8, 'Finance Hub', 'Fiona Williams', '+1-800-555-3456', 'contact@financehub.com', '303 Finance Circle', NULL, 'Los Angeles', '90001', 'California', 'USA'),
	(10, 'Retail Giants', 'Hannah Davis', '+1-800-555-0987', 'hello@retailgiants.com', '505 Retail Park', NULL, 'Dallas', '75201', 'Texas', 'USA'),
	(11, 'Construction Co.', 'Ian Brown', '+1-800-555-6543', 'contact@constructionco.com', '606 Build Street', 'Office 10', 'Denver', '80201', 'Colorado', 'USA'),
	(13, 'KFC Aylesbury', 'KFC', '+3847398247', 'contact@kfc.com', 'Aylesbury', '', 'Aylesbury', 'HP218LN', 'Buckinghamshire', 'United Kingdom'),
	(14, 'Dominos Aylesbury', 'Dominos', '23423', 'contact@kfc.com', 'Aylesbury', '', 'Aylesbury', 'HP218LN', 'Buckinghamshire', 'United Kingdom');

-- Dumping structure for table virtualqueue.customer
CREATE TABLE IF NOT EXISTS `customer` (
  `CustomerID` int(11) NOT NULL AUTO_INCREMENT,
  `phoneNumber` varchar(100) NOT NULL,
  PRIMARY KEY (`CustomerID`)
) ENGINE=InnoDB AUTO_INCREMENT=106 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table virtualqueue.customer: ~30 rows (approximately)
INSERT INTO `customer` (`CustomerID`, `phoneNumber`) VALUES
	(1, '1234567890'),
	(2, '1234567890'),
	(3, '7393152916'),
	(4, '2353152546'),
	(5, '2353152546'),
	(6, '2353152546'),
	(7, '2353152546'),
	(8, '2353152546'),
	(9, '7567456456'),
	(10, '7567456456'),
	(11, '7567456456'),
	(12, '7567456456'),
	(13, '7567456456'),
	(14, '7540188809'),
	(15, '7540188809'),
	(16, '7540188809'),
	(17, '7540188809'),
	(18, '7540188809'),
	(19, '7540188809'),
	(20, '7540188809'),
	(21, '7540188809'),
	(22, '7540188809'),
	(23, '832748388398'),
	(24, '7540188809'),
	(100, '000000'),
	(101, '7540188809'),
	(102, '7444543534'),
	(103, '7444543534'),
	(104, '7444543534'),
	(105, '7444543534');

-- Dumping structure for table virtualqueue.dealers
CREATE TABLE IF NOT EXISTS `dealers` (
  `DealerID` int(11) NOT NULL AUTO_INCREMENT,
  `DealerName` varchar(100) DEFAULT NULL,
  `DealerPhone` varchar(100) DEFAULT NULL,
  `DealerEmail` varchar(100) DEFAULT NULL,
  `DealerAddress` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`DealerID`),
  KEY `ix_dealers_DealerPhone` (`DealerPhone`),
  KEY `ix_dealers_DealerID` (`DealerID`),
  KEY `ix_dealers_DealerEmail` (`DealerEmail`),
  KEY `ix_dealers_DealerAddress` (`DealerAddress`),
  KEY `ix_dealers_DealerName` (`DealerName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table virtualqueue.dealers: ~0 rows (approximately)

-- Dumping structure for table virtualqueue.qrcode
CREATE TABLE IF NOT EXISTS `qrcode` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Qr_code` varchar(100) NOT NULL,
  `ShopID` int(11) DEFAULT NULL,
  `CreatedAt` timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`Id`),
  KEY `ShopID` (`ShopID`),
  CONSTRAINT `qrcode_ibfk_1` FOREIGN KEY (`ShopID`) REFERENCES `shop` (`ShopID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table virtualqueue.qrcode: ~8 rows (approximately)
INSERT INTO `qrcode` (`Id`, `Qr_code`, `ShopID`, `CreatedAt`) VALUES
	(1, 'http://127.0.0.1:8000/static/qr_codes/72.png', 72, '2024-07-30 12:13:45'),
	(2, 'http://127.0.0.1:8000/static/qr_codes/72.png', 27, '2024-07-31 09:27:52'),
	(3, 'http://127.0.0.1:8000/static/qr_codes/72.png', 33, '2024-07-31 09:27:52'),
	(4, 'http://127.0.0.1:8000/static/qr_codes/72.png', 31, '2024-07-31 09:27:52'),
	(5, 'http://127.0.0.1:8000/static/qr_codes/72.png', 32, '2024-07-31 09:27:52'),
	(6, 'http://127.0.0.1:8000/static/qr_codes/72.png', 34, '2024-07-31 09:27:52'),
	(7, 'http://127.0.0.1:8000/static/qr_codes/72.png', 37, '2024-07-31 09:27:52'),
	(8, 'http://127.0.0.1:8000/static/qr_codes/76.png', 76, '2024-07-31 16:30:00');

-- Dumping structure for table virtualqueue.queue
CREATE TABLE IF NOT EXISTS `queue` (
  `Token_number` int(11) NOT NULL AUTO_INCREMENT,
  `CustomerID` int(11) DEFAULT NULL,
  `Entry_time` datetime DEFAULT NULL,
  `status` enum('waiting','approved','served') DEFAULT NULL,
  PRIMARY KEY (`Token_number`),
  KEY `CustomerID` (`CustomerID`),
  KEY `ix_queue_Token_number` (`Token_number`),
  CONSTRAINT `queue_ibfk_1` FOREIGN KEY (`CustomerID`) REFERENCES `customer` (`CustomerID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table virtualqueue.queue: ~0 rows (approximately)

-- Dumping structure for table virtualqueue.shop
CREATE TABLE IF NOT EXISTS `shop` (
  `ShopID` int(11) NOT NULL AUTO_INCREMENT,
  `ShopName` varchar(255) NOT NULL,
  `ShopOwnerName` varchar(100) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `Address2` varchar(100) DEFAULT NULL,
  `Town` varchar(100) DEFAULT NULL,
  `State` varchar(100) DEFAULT NULL,
  `Country` varchar(100) DEFAULT NULL,
  `PhoneNumber` varchar(20) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `PostalCode` varchar(50) DEFAULT NULL,
  `CompanyID` int(11) DEFAULT NULL,
  PRIMARY KEY (`ShopID`),
  KEY `fk_company` (`CompanyID`),
  CONSTRAINT `fk_company` FOREIGN KEY (`CompanyID`) REFERENCES `company` (`CompanyID`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table virtualqueue.shop: ~11 rows (approximately)
INSERT INTO `shop` (`ShopID`, `ShopName`, `ShopOwnerName`, `Address`, `Address2`, `Town`, `State`, `Country`, `PhoneNumber`, `Email`, `PostalCode`, `CompanyID`) VALUES
	(27, 'Green Mart', 'Bob Smith', '456 Green Lane', NULL, 'Seattle', 'Washington', 'USA', '+1-206-555-4567', 'info@greenmart.com', '98109', 13),
	(31, 'Finance Central', 'Fiona Williams', '303 Finance Drive', NULL, 'Los Angeles', 'California', 'USA', '+1-310-555-3456', 'contact@financecentral.com', '90001', 13),
	(32, 'Travel World', 'George White', '404 Travel Road', 'Suite 12', 'Miami', 'Florida', 'USA', '+1-305-555-7890', 'info@travelworld.com', '33101', 13),
	(33, 'Retail Bazaar', 'Hannah Davis', '505 Market Street', NULL, 'Dallas', 'Texas', 'USA', '+1-214-555-6789', 'hello@retailbazaar.com', '75201', 13),
	(34, 'Build Supplies', 'Ian Brown', '606 Construction Lane', 'Unit 5', 'Denver', 'Colorado', 'USA', '+1-303-555-0123', 'contact@buildsupplies.com', '80202', 13),
	(37, 'Google from Alphabet Inc', 'John', 'John', 'John', 'John', 'John', 'Canada', 'John', 'John', NULL, 13),
	(72, 'SpaceX from Elon', 'John', 'John', 'John', 'John', 'John', 'Canada', 'John', 'John', NULL, 13),
	(73, 'Marvel Avengers', 'Marvel Avengers', 'Marvel Avengers', '', 'Marvel Avengers', 'Marvel Avengers', 'United Kingdom', 'Marvel Avengers', 'Marvel Avengers', NULL, 13),
	(74, 'Sports Direct', 'Sports Direct', 'Sports Direct', '', 'Sports Direct', 'Sports Direct', 'France', 'Sports Direct', 'Sports Direct', NULL, 13),
	(75, 'Retail Bazaar1', 'John', 'John', 'John', 'John', 'John', 'Canada', 'John', 'John', NULL, 13),
	(76, 'Retail Bazaar2', 'John', 'John', 'John', 'John', 'John', 'Canada', 'John', 'John', NULL, 13);

-- Dumping structure for table virtualqueue.tokens
CREATE TABLE IF NOT EXISTS `tokens` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ShopID` int(11) DEFAULT NULL,
  `CustomerID` int(11) DEFAULT NULL,
  `Entry_time` timestamp NULL DEFAULT current_timestamp(),
  `status` int(11) DEFAULT 0,
  `token_number` int(11) NOT NULL,
  `last_updated` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `CustomerID` (`CustomerID`),
  KEY `fk_shop` (`ShopID`),
  CONSTRAINT `fk_shop` FOREIGN KEY (`ShopID`) REFERENCES `shop` (`ShopID`),
  CONSTRAINT `tokens_ibfk_1` FOREIGN KEY (`CustomerID`) REFERENCES `customer` (`CustomerID`)
) ENGINE=InnoDB AUTO_INCREMENT=153 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table virtualqueue.tokens: ~18 rows (approximately)
INSERT INTO `tokens` (`id`, `ShopID`, `CustomerID`, `Entry_time`, `status`, `token_number`, `last_updated`) VALUES
	(133, 32, 23, '2024-08-21 11:22:33', 1, 1, '2024-08-21 12:25:52'),
	(135, 31, NULL, '2024-08-23 11:09:06', 1, 2, '2024-08-23 12:09:20'),
	(137, 31, NULL, '2024-08-23 11:19:59', 1, 4, '2024-08-23 12:21:02'),
	(138, 31, NULL, '2024-08-23 11:19:59', 0, 5, '2024-08-23 12:21:06'),
	(139, 31, NULL, '2024-08-23 11:19:59', 0, 6, '2024-08-23 12:21:07'),
	(140, 31, NULL, '2024-08-23 11:19:59', 0, 7, '2024-08-23 12:21:08'),
	(141, 31, NULL, '2024-08-23 11:19:59', 1, 8, '2024-08-23 12:21:11'),
	(142, 31, 101, '2024-08-23 12:27:11', 0, 9, '2024-08-23 13:27:26'),
	(143, 31, 102, '2024-08-23 12:27:11', 0, 10, '2024-08-23 13:31:02'),
	(144, 31, 103, '2024-08-23 12:35:09', 0, 11, '2024-08-23 13:36:24'),
	(145, 31, 104, '2024-08-23 13:00:49', 1, 12, '2024-08-23 14:01:26'),
	(146, 32, NULL, '2024-08-23 14:16:19', 0, 2, '2024-08-23 15:22:46'),
	(147, 32, NULL, '2024-08-23 14:16:19', 1, 3, '2024-08-23 15:22:50'),
	(148, 32, NULL, '2024-08-23 14:16:19', 0, 4, '2024-08-23 15:22:53'),
	(149, 32, NULL, '2024-08-23 14:16:19', 0, 5, '2024-08-23 15:23:26'),
	(150, 32, NULL, '2024-08-23 14:16:19', 1, 6, '2024-08-23 15:23:26'),
	(151, 32, NULL, '2024-08-23 14:16:19', 0, 7, '2024-08-23 15:39:44'),
	(152, 31, 105, '2024-08-23 16:53:12', 1, 13, '2024-08-23 17:57:45');

-- Dumping structure for table virtualqueue.token_sequence
CREATE TABLE IF NOT EXISTS `token_sequence` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ShopID` int(11) DEFAULT NULL,
  `LastTokenNumber` int(11) DEFAULT 0,
  `last_updated` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `ix_token_sequence_id` (`id`),
  KEY `ix_token_sequence_ShopID` (`ShopID`),
  CONSTRAINT `token_sequence_ibfk_1` FOREIGN KEY (`ShopID`) REFERENCES `shop` (`ShopID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table virtualqueue.token_sequence: ~2 rows (approximately)
INSERT INTO `token_sequence` (`id`, `ShopID`, `LastTokenNumber`, `last_updated`) VALUES
	(1, 32, 7, '2024-08-23 15:39:44'),
	(2, 31, 13, '2024-08-23 17:57:45');

-- Dumping structure for table virtualqueue.user
CREATE TABLE IF NOT EXISTS `user` (
  `UserID` int(11) NOT NULL AUTO_INCREMENT,
  `UserName` varchar(100) DEFAULT NULL,
  `UserPassword` varchar(100) DEFAULT NULL,
  `UserEmail` varchar(100) DEFAULT NULL,
  `UserPhone` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`UserID`),
  KEY `ix_user_UserEmail` (`UserEmail`),
  KEY `ix_user_UserPhone` (`UserPhone`),
  KEY `ix_user_UserName` (`UserName`),
  KEY `ix_user_UserID` (`UserID`),
  KEY `ix_user_UserPassword` (`UserPassword`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table virtualqueue.user: ~0 rows (approximately)
INSERT INTO `user` (`UserID`, `UserName`, `UserPassword`, `UserEmail`, `UserPhone`) VALUES
	(1, 'Arun', 'admin123', 'arunrajadorai23@gmail.com', '4464644'),
	(2, 'Vicky', 'admin123', 'vig234@gmail.com', NULL);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
