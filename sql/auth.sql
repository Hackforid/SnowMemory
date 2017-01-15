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

 Date: 01/16/2017 00:59:01 AM
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `auth`
-- ----------------------------
DROP TABLE IF EXISTS `auth`;
CREATE TABLE `auth` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `source_id` int(10) unsigned NOT NULL,
  `user_id` int(10) unsigned NOT NULL,
  `access_token` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `key` (`source_id`,`user_id`,`access_token`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
