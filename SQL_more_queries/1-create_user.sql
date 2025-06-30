-- Create MySQL user user_0d_1 with all privileges
-- The user should have password user_0d_1_pwd
-- Script should not fail if user already exists

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
