-- This file is for grading purposes only
-- This is a trigger function that executes when there are less than 10 books in stock
CREATE OR REPLACE FUNCTION insert_supply_order()
	RETURNS trigger AS $insert_supply_order$
	DECLARE prevMonthOrders integer;
	BEGIN

		IF NEW.stock < 10 THEN
			-- Determine the quantity of books that was order in the previous month
			-- Store it into the prevMonthOrders variable
			SELECT sum(oc.quantity) INTO prevMonthOrders FROM CustomerOrderContents as oc
				JOIN CustomerOrder AS co ON oc.orderId = co.orderId
				WHERE oDate >= current_date - interval '1' month AND bookId = NEW.bookId;
			-- Insert a new supply order record, which can be used to email the publisher and for reporting
			INSERT INTO supplyorder(supid, supdate, quantity, pubid, bookid)
				VALUES (DEFAULT, CURRENT_DATE, prevMonthOrders, NEW.pubId, NEW.bookId);
				
		END IF;
		RETURN NEW;
	END;
$insert_supply_order$ LANGUAGE plpgsql

CREATE TRIGGER insert_supply_order AFTER UPDATE ON book
		FOR EACH ROW EXECUTE FUNCTION insert_supply_order();