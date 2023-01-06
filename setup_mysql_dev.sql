-- prepares a MySQL server for the hbnb project
-- creates a database hbnb_dev_db
-- creates a user hbnb_dev with all privileges on hbnb_dev_db database
-- and only select privilege on preformance schema database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER
    IF NOT EXISTS "hbnb_dev"@"localhost"
    IDENTIFIED BY "hbnb_dev_pwd";
GRANT ALL PRIVILEGES
    ON hbnb_dev_db.*
    TO "hbnb_dev"@"localhost";
GRANT SELECT
    ON performance_schema.*
    TO "hbnb_dev"@"localhost";
FLUSH PRIVILEGES;
    