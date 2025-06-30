-- Create table id_not_null with id having default value 1
-- id field has default value 1
-- name field is VARCHAR(256)
-- Script should not fail if table already exists

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
