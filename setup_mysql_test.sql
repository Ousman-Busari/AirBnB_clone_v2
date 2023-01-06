-- prepares a MySQL server for the hbnb project
-- creates a database hbnb_test_db
-- creates a user hbnb_test with all privileges on hbnb_test_db database
-- and only select privilege on preformance schema database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER
    IF NOT EXISTS "hbnb_test"@"localhost"
    IDENTIFIED BY "hbnb_test_pwd";
GRANT ALL PRIVILEGES
    ON hbnb_test_db.*
    TO "hbnb_test"@"localhost";
GRANT SELECT
    ON performance_schema.*
    TO "hbnb_test"@"localhost";
FLUSH PRIVILEGES;
    