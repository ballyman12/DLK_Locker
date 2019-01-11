-- phpMyAdmin SQL Dump
-- version 4.8.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 11, 2019 at 10:27 AM
-- Server version: 10.1.31-MariaDB
-- PHP Version: 7.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `locker`
--

-- --------------------------------------------------------

--
-- Table structure for table `access`
--

CREATE TABLE `access` (
  `Access_Id` int(7) NOT NULL,
  `DLK_Id_User` int(5) NOT NULL,
  `DLK_RFID` varchar(100) NOT NULL,
  `DLK_Position_User` varchar(10) NOT NULL,
  `DLK_RFID_START` datetime NOT NULL,
  `DLK_RFID_EXP` datetime NOT NULL,
  `DLK_Id_Blacklist` int(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `access`
--

INSERT INTO `access` (`Access_Id`, `DLK_Id_User`, `DLK_RFID`, `DLK_Position_User`, `DLK_RFID_START`, `DLK_RFID_EXP`, `DLK_Id_Blacklist`) VALUES
(1, 1, 'DRF1879TR5', 'admin', '2018-08-30 00:00:00', '2022-10-04 00:00:00', NULL),
(2, 2, 'TU874F5OP3', 'Student', '2018-05-31 00:00:00', '2022-03-31 00:00:00', NULL),
(3, 3, 'SU410OCT39', 'Student', '2018-12-10 00:00:00', '2022-06-30 00:00:00', NULL),
(4, 4, 'N4MD5EW548', 'Student', '2018-05-31 00:00:00', '2022-05-31 00:00:00', 1),
(5, 5, 'OM48D16PQ2', 'Student', '2018-05-31 00:00:00', '2022-05-31 00:00:00', 2),
(6, 6, 'TWP15LO3U7', 'Student', '2018-05-31 00:00:00', '2023-05-31 00:00:00', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `conditions`
--

CREATE TABLE `conditions` (
  `DLK_Id_Condi` int(5) NOT NULL,
  `DLK_Name_Condi` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `conditions`
--

INSERT INTO `conditions` (`DLK_Id_Condi`, `DLK_Name_Condi`) VALUES
(0, 'ตู้ความเสียหาย'),
(4, 'ไม่บอกหรอก'),
(5, 'ไม่รู้ อยากยกเลิก'),
(6, 'ไม่มีเงินมาเปิดตู้เล่น'),
(8, 'ตู้สกปรก555'),
(9, 'อื่น ๆ');

-- --------------------------------------------------------

--
-- Table structure for table `details`
--

CREATE TABLE `details` (
  `DLK_Id_Detail` int(10) NOT NULL,
  `DLK_Id_User` int(5) NOT NULL,
  `DLK_RFID` varchar(100) NOT NULL,
  `DLK_Number_Locker` int(5) NOT NULL,
  `DLK_id_Result` int(5) NOT NULL,
  `DLK_Id_condi` int(5) DEFAULT NULL,
  `DLK_Date_Detail` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `DLK_Date_Curent` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `details`
--

INSERT INTO `details` (`DLK_Id_Detail`, `DLK_Id_User`, `DLK_RFID`, `DLK_Number_Locker`, `DLK_id_Result`, `DLK_Id_condi`, `DLK_Date_Detail`, `DLK_Date_Curent`) VALUES
(3, 2, 'TU874F5OP3', 1, 8, NULL, '2018-12-28 15:51:32', '2018-12-28 08:57:57'),
(7, 2, 'TU874F5OP3', 1, 8, NULL, '2019-01-09 10:59:33', '2019-01-09 03:59:33'),
(8, 2, 'TU874F5OP3', 5, 8, NULL, '2019-01-09 14:19:30', '2019-01-09 07:19:30'),
(9, 2, 'TU874F5OP3', 8, 8, NULL, '2019-01-09 14:44:47', '2019-01-09 07:47:08');

-- --------------------------------------------------------

--
-- Table structure for table `lockers`
--

CREATE TABLE `lockers` (
  `DLK_Id_Locker` int(10) NOT NULL,
  `DLK_Number_Locker` int(5) NOT NULL,
  `DLK_Name_Locker` varchar(255) NOT NULL,
  `DLK_Status_Locker` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `lockers`
--

INSERT INTO `lockers` (`DLK_Id_Locker`, `DLK_Number_Locker`, `DLK_Name_Locker`, `DLK_Status_Locker`) VALUES
(1, 1, 'Computer Science floor 6th', 2),
(2, 2, 'Computer Science floor 6th', 3),
(3, 3, 'Computer Science floor 6th', 2),
(4, 4, 'Computer Science floor 6th', 2),
(5, 5, 'Computer Science floor 6th', 2),
(6, 6, 'Computer Science floor 6th', 2),
(7, 7, 'Computer Science floor 6th', 2),
(8, 8, 'Computer Science floor 6th', 3),
(9, 9, 'Computer Science floor 6th', 2);

-- --------------------------------------------------------

--
-- Table structure for table `log_status_locker`
--

CREATE TABLE `log_status_locker` (
  `log_Id` int(10) NOT NULL,
  `DLK_Id_User` int(5) NOT NULL,
  `DLK_RFID` varchar(100) NOT NULL,
  `DLK_Number_Locker` int(5) NOT NULL,
  `DLK_Status_Locker` int(5) NOT NULL,
  `Time_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `MQTT_Status` int(5) NOT NULL,
  `MQTT_Mass` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `log_status_locker`
--

INSERT INTO `log_status_locker` (`log_Id`, `DLK_Id_User`, `DLK_RFID`, `DLK_Number_Locker`, `DLK_Status_Locker`, `Time_update`, `MQTT_Status`, `MQTT_Mass`) VALUES
(1, 1, 'DRF1879TR5', 1, 2, '2018-12-28 08:57:21', 0, NULL),
(2, 1, 'DRF1879TR5', 1, 1, '2018-12-28 08:57:57', 0, NULL),
(3, 1, 'DRF1879TR5', 1, 3, '2018-12-28 08:57:57', 0, NULL),
(4, 1, 'DRF1879TR5', 9, 2, '2018-12-28 09:21:20', 0, NULL),
(5, 1, 'DRF1879TR5', 1, 2, '2018-12-28 09:29:04', 0, NULL),
(6, 1, 'DRF1879TR5', 1, 1, '2018-12-28 09:29:12', 0, NULL),
(7, 1, 'DRF1879TR5', 2, 2, '2018-12-28 09:35:38', 0, NULL),
(8, 1, 'DRF1879TR5', 2, 1, '2018-12-28 09:35:44', 0, NULL),
(9, 1, 'DRF1879TR5', 2, 3, '2018-12-28 09:35:44', 0, NULL),
(10, 1, 'DRF1879TR5', 9, 3, '2019-01-07 04:42:09', 0, NULL),
(11, 1, 'DRF1879TR5', 1, 3, '2019-01-07 04:57:32', 0, NULL),
(12, 1, 'DRF1879TR5', 1, 3, '2019-01-09 07:38:29', 0, NULL),
(13, 2, 'TU874F5OP3', 8, 2, '2019-01-09 07:44:41', 0, NULL),
(14, 2, 'TU874F5OP3', 8, 1, '2019-01-09 07:44:47', 0, NULL),
(15, 2, 'TU874F5OP3', 8, 4, '2019-01-09 07:44:47', 0, NULL),
(16, 2, 'TU874F5OP3', 8, 2, '2019-01-09 07:47:01', 0, NULL),
(17, 2, 'TU874F5OP3', 8, 1, '2019-01-09 07:47:08', 0, NULL),
(18, 2, 'TU874F5OP3', 8, 3, '2019-01-09 07:47:09', 0, NULL),
(19, 3, 'SU410OCT39', 2, 2, '2019-01-09 07:53:58', 0, NULL),
(20, 3, 'SU410OCT39', 2, 1, '2019-01-09 07:54:10', 0, NULL),
(21, 3, 'SU410OCT39', 2, 4, '2019-01-09 07:54:10', 0, NULL),
(22, 2, 'TU874F5OP3', 4, 2, '2019-01-09 08:44:47', 0, NULL),
(23, 2, 'TU874F5OP3', 4, 1, '2019-01-09 08:44:53', 0, NULL),
(24, 2, 'TU874F5OP3', 4, 4, '2019-01-09 08:44:53', 0, NULL),
(25, 6, 'TWP15LO3U7', 3, 2, '2019-01-09 10:13:42', 0, NULL),
(26, 6, 'TWP15LO3U7', 3, 1, '2019-01-09 10:13:47', 0, NULL),
(27, 6, 'TWP15LO3U7', 5, 2, '2019-01-09 10:15:15', 0, NULL),
(28, 6, 'TWP15LO3U7', 5, 1, '2019-01-09 10:15:20', 0, NULL),
(29, 6, 'TWP15LO3U7', 1, 2, '2019-01-09 10:16:47', 0, NULL),
(30, 6, 'TWP15LO3U7', 1, 1, '2019-01-09 10:16:50', 0, NULL),
(31, 6, 'TWP15LO3U7', 1, 4, '2019-01-09 10:16:50', 0, NULL),
(32, 6, 'TWP15LO3U7', 7, 2, '2019-01-09 10:20:52', 0, NULL),
(33, 6, 'TWP15LO3U7', 7, 1, '2019-01-09 10:20:55', 0, NULL),
(34, 6, 'TWP15LO3U7', 7, 4, '2019-01-09 10:20:55', 0, NULL),
(35, 6, 'TWP15LO3U7', 1, 2, '2019-01-09 10:21:49', 0, NULL),
(36, 6, 'TWP15LO3U7', 1, 1, '2019-01-09 10:21:52', 0, NULL),
(37, 6, 'TWP15LO3U7', 1, 4, '2019-01-09 10:21:52', 0, NULL),
(38, 6, 'TWP15LO3U7', 8, 2, '2019-01-09 10:28:54', 0, NULL),
(39, 6, 'TWP15LO3U7', 8, 1, '2019-01-09 10:28:56', 0, NULL),
(40, 6, 'TWP15LO3U7', 8, 4, '2019-01-09 10:28:56', 0, NULL),
(41, 2, 'TU874F5OP3', 1, 2, '2019-01-11 06:16:48', 0, NULL),
(42, 2, 'TU874F5OP3', 9, 2, '2019-01-11 06:20:08', 0, NULL),
(43, 2, 'TU874F5OP3', 3, 2, '2019-01-11 06:22:54', 0, NULL),
(44, 2, 'TU874F5OP3', 3, 2, '2019-01-11 06:22:55', 0, NULL),
(45, 2, 'TU874F5OP3', 1, 2, '2019-01-11 06:25:06', 0, NULL),
(46, 2, 'TU874F5OP3', 1, 2, '2019-01-11 06:25:06', 0, NULL),
(47, 2, 'TU874F5OP3', 1, 2, '2019-01-11 06:25:06', 0, NULL),
(48, 2, 'TU874F5OP3', 1, 2, '2019-01-11 06:27:42', 0, NULL),
(49, 2, 'TU874F5OP3', 1, 2, '2019-01-11 06:27:42', 0, NULL),
(50, 2, 'TU874F5OP3', 1, 2, '2019-01-11 06:27:42', 0, NULL),
(51, 2, 'TU874F5OP3', 4, 2, '2019-01-11 06:31:19', 0, NULL),
(52, 2, 'TU874F5OP3', 4, 2, '2019-01-11 06:31:19', 0, NULL),
(53, 2, 'TU874F5OP3', 4, 2, '2019-01-11 06:31:19', 0, NULL),
(54, 2, 'TU874F5OP3', 8, 2, '2019-01-11 06:33:31', 0, NULL),
(55, 2, 'TU874F5OP3', 8, 2, '2019-01-11 06:33:31', 0, NULL),
(56, 2, 'TU874F5OP3', 8, 2, '2019-01-11 06:33:31', 0, NULL),
(57, 2, 'TU874F5OP3', 7, 2, '2019-01-11 06:37:27', 0, NULL),
(58, 2, 'TU874F5OP3', 7, 2, '2019-01-11 06:37:27', 0, NULL),
(59, 2, 'TU874F5OP3', 7, 2, '2019-01-11 06:37:27', 0, NULL),
(60, 2, 'TU874F5OP3', 9, 2, '2019-01-11 06:43:07', 0, NULL),
(61, 2, 'TU874F5OP3', 9, 2, '2019-01-11 06:43:07', 0, NULL),
(62, 2, 'TU874F5OP3', 9, 2, '2019-01-11 06:43:07', 0, NULL),
(63, 2, 'TU874F5OP3', 2, 2, '2019-01-11 06:47:49', 0, NULL),
(64, 2, 'TU874F5OP3', 2, 2, '2019-01-11 06:47:49', 0, NULL),
(65, 2, 'TU874F5OP3', 3, 2, '2019-01-11 06:49:19', 0, NULL),
(66, 2, 'TU874F5OP3', 3, 2, '2019-01-11 06:49:19', 0, NULL),
(67, 2, 'TU874F5OP3', 6, 2, '2019-01-11 06:49:39', 0, NULL),
(68, 2, 'TU874F5OP3', 6, 2, '2019-01-11 06:49:39', 0, NULL),
(69, 2, 'TU874F5OP3', 5, 2, '2019-01-11 06:53:24', 0, NULL),
(70, 2, 'TU874F5OP3', 5, 2, '2019-01-11 06:53:24', 0, NULL),
(71, 2, 'TU874F5OP3', 5, 2, '2019-01-11 06:53:24', 0, NULL),
(72, 2, 'TU874F5OP3', 1, 2, '2019-01-11 07:01:42', 0, NULL),
(73, 2, 'TU874F5OP3', 1, 2, '2019-01-11 07:01:42', 0, NULL),
(74, 2, 'TU874F5OP3', 6, 2, '2019-01-11 07:07:24', 0, NULL),
(75, 2, 'TU874F5OP3', 6, 2, '2019-01-11 07:07:24', 0, NULL),
(76, 2, 'TU874F5OP3', 1, 2, '2019-01-11 07:08:10', 0, NULL),
(77, 2, 'TU874F5OP3', 1, 2, '2019-01-11 07:08:10', 0, NULL),
(78, 2, 'TU874F5OP3', 6, 2, '2019-01-11 07:09:23', 0, NULL),
(79, 2, 'TU874F5OP3', 6, 2, '2019-01-11 07:09:24', 0, NULL),
(80, 2, 'TU874F5OP3', 7, 2, '2019-01-11 07:20:49', 0, NULL),
(81, 2, 'TU874F5OP3', 7, 2, '2019-01-11 07:20:49', 0, NULL),
(82, 2, 'TU874F5OP3', 5, 2, '2019-01-11 07:22:21', 0, NULL),
(83, 2, 'TU874F5OP3', 5, 2, '2019-01-11 07:22:21', 0, NULL),
(84, 2, 'TU874F5OP3', 5, 1, '2019-01-11 07:22:29', 0, NULL),
(85, 2, 'TU874F5OP3', 5, 1, '2019-01-11 07:22:29', 0, NULL),
(86, 2, 'TU874F5OP3', 8, 2, '2019-01-11 07:25:00', 0, NULL),
(87, 2, 'TU874F5OP3', 8, 2, '2019-01-11 07:25:00', 0, NULL),
(88, 2, 'TU874F5OP3', 8, 1, '2019-01-11 07:25:40', 0, NULL),
(89, 2, 'TU874F5OP3', 8, 1, '2019-01-11 07:25:40', 0, NULL),
(90, 2, 'TU874F5OP3', 7, 2, '2019-01-11 07:30:53', 0, NULL),
(91, 2, 'TU874F5OP3', 7, 2, '2019-01-11 07:30:53', 0, NULL),
(92, 2, 'TU874F5OP3', 7, 1, '2019-01-11 07:31:27', 0, NULL),
(93, 2, 'TU874F5OP3', 7, 1, '2019-01-11 07:31:28', 0, NULL),
(94, 2, 'TU874F5OP3', 9, 2, '2019-01-11 07:33:26', 0, NULL),
(95, 2, 'TU874F5OP3', 9, 2, '2019-01-11 07:33:26', 0, NULL),
(96, 2, 'TU874F5OP3', 9, 1, '2019-01-11 07:34:21', 0, NULL),
(97, 2, 'TU874F5OP3', 9, 1, '2019-01-11 07:34:21', 0, NULL),
(98, 2, 'TU874F5OP3', 4, 2, '2019-01-11 07:36:49', 0, NULL),
(99, 2, 'TU874F5OP3', 4, 2, '2019-01-11 07:36:49', 0, NULL),
(100, 2, 'TU874F5OP3', 5, 2, '2019-01-11 07:38:46', 0, NULL),
(101, 2, 'TU874F5OP3', 5, 2, '2019-01-11 07:38:47', 0, NULL),
(102, 2, 'TU874F5OP3', 6, 2, '2019-01-11 07:41:47', 0, NULL),
(103, 2, 'TU874F5OP3', 6, 2, '2019-01-11 07:41:47', 0, NULL),
(104, 2, 'TU874F5OP3', 7, 2, '2019-01-11 07:44:38', 0, NULL),
(105, 2, 'TU874F5OP3', 7, 2, '2019-01-11 07:44:38', 0, NULL),
(106, 2, 'TU874F5OP3', 8, 2, '2019-01-11 07:48:08', 0, NULL),
(107, 2, 'TU874F5OP3', 8, 2, '2019-01-11 07:48:08', 0, NULL),
(108, 2, 'TU874F5OP3', 9, 2, '2019-01-11 07:49:50', 0, NULL),
(109, 2, 'TU874F5OP3', 9, 2, '2019-01-11 07:49:50', 0, NULL),
(110, 2, 'TU874F5OP3', 2, 2, '2019-01-11 07:51:41', 0, NULL),
(111, 2, 'TU874F5OP3', 2, 2, '2019-01-11 07:51:41', 0, NULL),
(112, 2, 'TU874F5OP3', 9, 2, '2019-01-11 07:57:35', 0, NULL),
(113, 2, 'TU874F5OP3', 9, 2, '2019-01-11 07:57:35', 0, NULL),
(114, 2, 'TU874F5OP3', 1, 2, '2019-01-11 08:00:04', 0, NULL),
(115, 2, 'TU874F5OP3', 1, 2, '2019-01-11 08:00:04', 0, NULL),
(116, 2, 'TU874F5OP3', 1, 2, '2019-01-11 08:00:45', 0, NULL),
(117, 2, 'TU874F5OP3', 1, 2, '2019-01-11 08:00:45', 0, NULL),
(118, 2, 'TU874F5OP3', 9, 2, '2019-01-11 08:01:35', 0, NULL),
(119, 2, 'TU874F5OP3', 9, 2, '2019-01-11 08:01:35', 0, NULL),
(120, 2, 'TU874F5OP3', 3, 2, '2019-01-11 08:02:57', 0, NULL),
(121, 2, 'TU874F5OP3', 3, 2, '2019-01-11 08:02:58', 0, NULL),
(122, 2, 'TU874F5OP3', 3, 2, '2019-01-11 08:08:47', 0, NULL),
(123, 2, 'TU874F5OP3', 3, 2, '2019-01-11 08:08:47', 0, NULL),
(124, 2, 'TU874F5OP3', 5, 2, '2019-01-11 08:29:51', 0, NULL),
(125, 2, 'TU874F5OP3', 5, 2, '2019-01-11 08:29:51', 0, NULL),
(126, 2, 'TU874F5OP3', 1, 2, '2019-01-11 08:30:17', 0, NULL),
(127, 2, 'TU874F5OP3', 1, 2, '2019-01-11 08:30:17', 0, NULL),
(128, 2, 'TU874F5OP3', 1, 2, '2019-01-11 08:31:07', 0, NULL),
(129, 2, 'TU874F5OP3', 1, 2, '2019-01-11 08:31:07', 0, NULL),
(130, 2, 'TU874F5OP3', 9, 2, '2019-01-11 08:32:31', 0, NULL),
(131, 2, 'TU874F5OP3', 9, 2, '2019-01-11 08:32:32', 0, NULL),
(132, 2, 'TU874F5OP3', 1, 2, '2019-01-11 08:34:08', 0, NULL),
(133, 2, 'TU874F5OP3', 1, 2, '2019-01-11 08:34:08', 0, NULL),
(134, 2, 'TU874F5OP3', 4, 2, '2019-01-11 08:45:54', 0, NULL),
(135, 2, 'TU874F5OP3', 4, 2, '2019-01-11 08:45:54', 0, NULL),
(136, 2, 'TU874F5OP3', 4, 2, '2019-01-11 08:46:50', 0, NULL),
(137, 2, 'TU874F5OP3', 4, 2, '2019-01-11 08:46:50', 0, NULL),
(138, 2, 'TU874F5OP3', 7, 2, '2019-01-11 08:47:22', 0, NULL),
(139, 2, 'TU874F5OP3', 7, 2, '2019-01-11 08:47:22', 0, NULL),
(140, 2, 'TU874F5OP3', 5, 2, '2019-01-11 09:00:33', 0, NULL),
(141, 2, 'TU874F5OP3', 5, 2, '2019-01-11 09:00:33', 0, NULL),
(142, 2, 'TU874F5OP3', 4, 2, '2019-01-11 09:05:01', 0, NULL),
(143, 2, 'TU874F5OP3', 4, 2, '2019-01-11 09:05:01', 0, NULL),
(144, 2, 'TU874F5OP3', 7, 2, '2019-01-11 09:08:49', 0, NULL),
(145, 2, 'TU874F5OP3', 7, 2, '2019-01-11 09:08:50', 0, NULL),
(146, 2, 'TU874F5OP3', 6, 2, '2019-01-11 09:14:30', 0, NULL),
(147, 2, 'TU874F5OP3', 6, 2, '2019-01-11 09:14:30', 0, NULL),
(148, 2, 'TU874F5OP3', 8, 2, '2019-01-11 09:23:03', 0, NULL),
(149, 2, 'TU874F5OP3', 8, 2, '2019-01-11 09:23:03', 0, NULL),
(150, 2, 'TU874F5OP3', 2, 2, '2019-01-11 09:23:35', 0, NULL),
(151, 2, 'TU874F5OP3', 2, 2, '2019-01-11 09:23:35', 0, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `result`
--

CREATE TABLE `result` (
  `DLK_id_Result` int(5) NOT NULL,
  `DLK_Name_Result` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

--
-- Dumping data for table `result`
--

INSERT INTO `result` (`DLK_id_Result`, `DLK_Name_Result`) VALUES
(1, 'กำลังใช้งาน'),
(2, 'ไม่มีสิทธิใช้งาน'),
(3, 'ไม่ชำระค่าเทอม'),
(4, 'ค้างชำระ'),
(5, 'ฝากไม่ปิด'),
(6, 'ไม่ปิดตู้'),
(7, 'ยกเลิกการใช้งาน'),
(8, 'สำเร็จ');

-- --------------------------------------------------------

--
-- Table structure for table `time`
--

CREATE TABLE `time` (
  `DLK_Id_Time` int(5) NOT NULL,
  `DLK_Open_Time` time NOT NULL,
  `DLK_Close_Time` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `time`
--

INSERT INTO `time` (`DLK_Id_Time`, `DLK_Open_Time`, `DLK_Close_Time`) VALUES
(1, '11:19:34', '23:19:36');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `access`
--
ALTER TABLE `access`
  ADD PRIMARY KEY (`Access_Id`);

--
-- Indexes for table `conditions`
--
ALTER TABLE `conditions`
  ADD PRIMARY KEY (`DLK_Id_Condi`);

--
-- Indexes for table `details`
--
ALTER TABLE `details`
  ADD PRIMARY KEY (`DLK_Id_Detail`),
  ADD KEY `DLK_Id_Locker` (`DLK_Number_Locker`),
  ADD KEY `DLK_id_Result` (`DLK_id_Result`),
  ADD KEY `DLK_Id_condi` (`DLK_Id_condi`);

--
-- Indexes for table `lockers`
--
ALTER TABLE `lockers`
  ADD PRIMARY KEY (`DLK_Id_Locker`);

--
-- Indexes for table `log_status_locker`
--
ALTER TABLE `log_status_locker`
  ADD PRIMARY KEY (`log_Id`);

--
-- Indexes for table `result`
--
ALTER TABLE `result`
  ADD PRIMARY KEY (`DLK_id_Result`);

--
-- Indexes for table `time`
--
ALTER TABLE `time`
  ADD PRIMARY KEY (`DLK_Id_Time`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `access`
--
ALTER TABLE `access`
  MODIFY `Access_Id` int(7) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `conditions`
--
ALTER TABLE `conditions`
  MODIFY `DLK_Id_Condi` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `details`
--
ALTER TABLE `details`
  MODIFY `DLK_Id_Detail` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `lockers`
--
ALTER TABLE `lockers`
  MODIFY `DLK_Id_Locker` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `log_status_locker`
--
ALTER TABLE `log_status_locker`
  MODIFY `log_Id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=152;

--
-- AUTO_INCREMENT for table `result`
--
ALTER TABLE `result`
  MODIFY `DLK_id_Result` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `time`
--
ALTER TABLE `time`
  MODIFY `DLK_Id_Time` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `details`
--
ALTER TABLE `details`
  ADD CONSTRAINT `details_ibfk_2` FOREIGN KEY (`DLK_Number_Locker`) REFERENCES `lockers` (`DLK_Id_Locker`),
  ADD CONSTRAINT `details_ibfk_3` FOREIGN KEY (`DLK_id_Result`) REFERENCES `result` (`DLK_id_Result`),
  ADD CONSTRAINT `details_ibfk_4` FOREIGN KEY (`DLK_Id_condi`) REFERENCES `conditions` (`DLK_Id_Condi`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
