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

 Date: 01/18/2017 21:33:16 PM
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(10) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `username` varchar(64) NOT NULL,
  `password` varchar(64) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `enable` tinyint(1) NOT NULL DEFAULT '1' COMMENT '1 true 0 false',
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
