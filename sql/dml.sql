-- This file is for grading purposes only

INSERT INTO BillingShippingInfo(
	bsId,addressL1, addressL2, city, provSt, country, pCode, ccardNo, exp, ccn, ccName)
	VALUES (DEFAULT,'1 Sycamore Dr.', NULL, 'Springfield', 'CA', 'US', '700123', '1234-5678-9012', '0124', '123', 'John Smith');

INSERT INTO BillingShippingInfo(
	bsId,addressL1, addressL2, city, provSt, country, pCode, ccardNo, exp, ccn, ccName)
	VALUES (DEFAULT,'10 Main St.', NULL, 'Toronto', 'ON', 'Canada', 'M1Z 123', '4567-1111-2222', '0922', '555', 'Jane Doe');

INSERT INTO BillingShippingInfo(
	bsId,addressL1, addressL2, city, provSt, country, pCode, ccardNo, exp, ccn, ccName)
	VALUES (DEFAULT,'54 Country Rd.', 'Suite 1B', 'Springfield', 'CA', 'US', '700124', '4555-2222-3333', '1224', '111', 'John Smith Enterprises');

INSERT INTO Customer(
	cNumber,uName, pword, email, lname, fname)
	VALUES (DEFAULT,'jsmith', '961804260.yqTq6SZYMoNbOpY1t2h37U7zhyuFd1vmeAx8g-KPEQc=', 'jsmith@gmail.com', 'Smith', 'John');

INSERT INTO Customer(
	cNumber,uName, pword, email, lname, fname)
	VALUES (DEFAULT,'jdoe', '0169402691.-1H4VX0WCrSI449OBmcs6ycLOQwbR7hqEQwYQ6GNvkg=', 'jdoe@carleton.ca', 'Doe', 'Jane');

INSERT INTO bsiDirectory(bsId, cNumber, isPrimary) VALUES (1, 1, TRUE);
INSERT INTO bsiDirectory(bsId, cNumber, isPrimary) VALUES (2, 2, TRUE);
INSERT INTO bsiDirectory(bsId, cNumber, isPrimary) VALUES (3, 1, TRUE);

INSERT INTO Publisher(
  pubId,pubName,pubEmail,bankAcctNo,pubAddress,phoneNo) 
  VALUES (DEFAULT, 'Meow Books','order@meowbooks.com','JPMorgan 001-1234-11111','1 Kitty Kat Rd., Los Angeles, CA, US, 90210','(945) 123-4567');
INSERT INTO Publisher(
  pubId,pubName,pubEmail,bankAcctNo,pubAddress,phoneNo) 
  VALUES (DEFAULT, 'Nebulous','contact@nebulous.com','BoA 002-4321-22222','54 5th Rd., New York, NY, US, 70000','(768) 321-7654');
INSERT INTO Publisher(
  pubId, pubName,pubEmail,bankAcctNo) 
  VALUES (DEFAULT, 'Fictional Press','info@fictional.com','BoA 002-5678-33333');
INSERT INTO Publisher(
  pubId, pubName,pubEmail,bankAcctNo) 
  VALUES (DEFAULT, 'Random Mouse','orders@random.com','Wells Fargo 003-6789-44444');

INSERT INTO Book(
	bookId, ISBN, author, title, genre, stock, price, percentRoyalty, noPages, pubId)
	VALUES (DEFAULT, '1234-1111-9012', 'Mark Twain', 'Adventures of Huckleberry Finn', 'Fiction', 10, 12.5, 10, 321, 3);
INSERT INTO Book(
	bookId, ISBN, author, title, genre, stock, price, percentRoyalty, noPages, pubId)
	VALUES (DEFAULT, '1234-1111-9014', 'Mark Twain', 'The Adventures of Tom Sawyer', 'Fiction', 5, 9.5, 10, 231, 3);
INSERT INTO Book(
	bookId, ISBN, author, title, genre, stock, price, percentRoyalty, noPages, pubId)
	VALUES (DEFAULT, '1333-2222-3061', 'Isaac Asimov', 'Foundation', 'Sci-Fi', 15, 21.75, 15, 431, 2);
INSERT INTO Book(
	bookId, ISBN, author, title, genre, stock, price, percentRoyalty, noPages, pubId)
	VALUES (DEFAULT, '1333-2222-3064', 'Isaac Asimov', 'Foundation and Empire', 'Sci-Fi', 2, 22, 15, 441, 2);
INSERT INTO Book(
	bookId, ISBN, author, title, genre, stock, price, percentRoyalty, noPages, pubId)
	VALUES (DEFAULT, '1333-2222-3066', 'Isaac Asimov', 'Second Foundation', 'Sci-Fi', 5, 15.25, 15, 330, 2);
INSERT INTO Book(
	bookId, ISBN, author, title, genre, stock, price, percentRoyalty, noPages, pubId)
	VALUES (DEFAULT, '5432-3333-2311', 'Mo Willems', 'Don''t Let the Pigeon Drive the Bus', 'Fiction', 20, 5, 20, 15, 1);
INSERT INTO Book(
	bookId, ISBN, author, title, genre, stock, price, percentRoyalty, noPages, pubId)
	VALUES (DEFAULT, '5432-3333-2313', 'Mo Willems', 'The Pigeon Finds a Hot Dog', 'Fiction', 11, 6, 20, 12, 1);
INSERT INTO Book(
	bookId, ISBN, author, title, genre, stock, price, percentRoyalty, noPages, pubId)
	VALUES (DEFAULT, '5432-3333-2315', 'Mo Willems', 'Don''t Let Pigeon Stay Up Late', 'Fiction', 15, 6, 20, 10,1);
INSERT INTO Book(
	bookId, ISBN, author, title, genre, stock, price, percentRoyalty, noPages, pubId)
	VALUES (DEFAULT, '0987-4444-1121', 'J. R. R. Tolkien', 'The Lord of the Rings Box Set', 'Fiction', 12, 66.7, 25, 1905, 3);
INSERT INTO Book(
	bookId, ISBN, author, title, genre, stock, price, percentRoyalty, noPages, pubId)
	VALUES (DEFAULT, '0001-0002-0003', 'Rick Silva', 'Essential Postgres', 'Technical', 2, 39.05, 5, 90, 4);



DELETE FROM Book WHERE bookId=<value>


INSERT INTO customerorder 
  (orderid, odate, ostatus, bsid, cnumber)
	VALUES ( DEFAULT, CURRENT_DATE, 'SUBMITTED', <bsidvalue>, <cnumbervalue> ) returning orderid


INSERT INTO customerordercontents (bookid, orderid, quantity) VALUES (book.bookId, orderid, book.price)


UPDATE Book SET stock = stock - <pricevalue> WHERE bookId = <idvalue>
