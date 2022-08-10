-- Root user
-- A script that craetes the MySQL server
CREATE USER IF NOT EXISTS `user_0d_1`@`localhost` IDENTIFIED BY `user_0d_1_pwd`;
GRANT ALL PRIVILAGES ON * . * TO `user_0d_1`@`localhost`;
FLUSH PRIVILEGES;
