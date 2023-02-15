-- A script that creates the db hbtn_0d_usa and table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
state_id INT NOT NULL,
FOREIGN KEY (state_id) REFERENCES states(id),
name VARCHAR(256)
);
