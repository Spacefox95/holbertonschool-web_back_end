-- Create a trigger on quantity decrease
DELIMITER $$

CREATE TRIGGER item_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items
	SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;

END$$

DELIMITER;