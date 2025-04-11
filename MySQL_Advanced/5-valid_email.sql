-- Create a trigger reseting mail when email has been changed
DELIMITER $$

CREATE TRIGGER email_changed
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN 
IF OLD.email <> NEW.email THEN
SET NEW.valid_email = 0;
END IF;
END$$
DELIMITER;