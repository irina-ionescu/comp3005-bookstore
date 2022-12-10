	CREATE OR REPLACE FUNCTION insert_supply_order()
		RETURNS trigger AS $insert_supply_order$
		BEGIN
			IF NEW.stock < 10 THEN
				INSERT INTO supplyorder(supid, supdate, quantity, pubid, bookid)
				VALUES (DEFAULT, CURRENT_DATE, 10, NEW.pubId, NEW.bookId);
			END IF;
			RETURN NEW;
		END;
	$insert_supply_order$ LANGUAGE plpgsql

	CREATE TRIGGER insert_supply_order AFTER UPDATE ON book
			FOR EACH ROW EXECUTE FUNCTION insert_supply_order();