-- Create the 'users' table if it doesn't already exist
CREATE TABLE IF NOT EXISTS users (
		id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
		email VARCHAR(255) UNIQUE NOT NULL,
		name VARCHAR(255)
	);