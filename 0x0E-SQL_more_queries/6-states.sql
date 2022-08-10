-- States table
-- A script that create a dtabase and a table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE AUTO_GENERATE NOT NULL PRIMARY KEY, name  VARCHAR(256) NOT NULL);
