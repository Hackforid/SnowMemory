/*
 Navicat Premium Data Transfer

 Source Server         : maclocal
 Source Server Type    : MySQL
 Source Server Version : 100120
 Source Host           : localhost
 Source Database       : snowmemory

 Target Server Type    : MySQL
 Target Server Version : 100120
 File Encoding         : utf-8

 Date: 01/16/2017 00:21:49 AM
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
  `nickname` varchar(20) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `enable` tinyint(1) NOT NULL DEFAULT '1' COMMENT '1 true 0 false',
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
