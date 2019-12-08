CREATE DATABASE IF NOT EXISTS test_bd;
USE test_bd;

GRANT ALL ON test_bd.* TO 'django_user'@'%' IDENTIFIED BY '12345';