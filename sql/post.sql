/*
 Navicat Premium Data Transfer

 Source Server         : rmbp
 Source Server Type    : MariaDB
 Source Server Version : 100120
 Source Host           : localhost
 Source Database       : snowmemory

 Target Server Type    : MariaDB
 Target Server Version : 100120
 File Encoding         : utf-8

 Date: 01/22/2017 20:07:33 PM
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `post`
-- ----------------------------
DROP TABLE IF EXISTS `post`;
CREATE TABLE `post` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `author_id` int(11) NOT NULL,
  `target_id` int(11) NOT NULL,
  `photos` varchar(200) NOT NULL,
  `content` varchar(200) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted` tinyint(1) unsigned zerofill NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `author_id` (`author_id`),
  KEY `target_id` (`target_id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
