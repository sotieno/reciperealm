-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS rr_db;
CREATE USER IF NOT EXISTS 'rr_db_user'@`localhost` IDENTIFIED BY 'rr_db_pwd';
GRANT ALL PRIVILEGES ON rr_db.* TO 'rr_db_user'@'localhost';
FLUSH PRIVILEGES;