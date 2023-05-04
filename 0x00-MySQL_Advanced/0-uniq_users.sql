-- Create a user table that can run on any database.
-- The script should not fail
CREATE TABLE If NOT EXISTS users (  
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
