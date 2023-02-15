-- A script to create a table with id column that cannot be null
CREATE TABLE IF NOT EXISTS id_not_null (
id INT DEFAULT 1 NOT NULL,
name VARCHAR(256)
);
