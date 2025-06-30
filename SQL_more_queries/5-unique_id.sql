-- Create table unique_id with id having default value 1 and unique constraint
-- id field has default value 1 and must be unique
-- name field is VARCHAR(256)
-- Script should not fail if table already exists

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
