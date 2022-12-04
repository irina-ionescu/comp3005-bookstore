
CREATE TABLE if not exists BillingShippingInfo (
  bsId serial,
  addressL1 varchar (100) NOT NULL,
  addressL2 varchar (100),
  city varchar (100) NOT NULL,
  provSt char (2) NOT NULL,
  country varchar (50) NOT NULL,
  pcode varchar (10) NOT NULL,
  ccardNo char (15) NOT NULL,
  exp char (4) NOT NULL,
  ccn char (3) NOT NULL,
  ccName varchar (100) NOT NULL,
  
  PRIMARY KEY (bsId)	 
);

CREATE TABLE if not exists Customer (
    cNumber serial,
  	uname varchar(50) UNIQUE NOT NULL,
  	pword varchar(100) NOT NULL,
  	email varchar(100) UNIQUE NOT NULL,
  	lname varchar(100) NOT NULL,
	  fname varchar(100) NOT NULL,
  
  PRIMARY KEY (cNumber)
);

CREATE TABLE if not exists bsiDirectory (
  bsId int NOT NULL,
  cNumber int NOT NULL,
  isPrimary boolean NOT NULL,

  PRIMARY KEY (bsId, cNumber),
  FOREIGN KEY (bsId)
    REFERENCES BillingShippingInfo(bsId),
  FOREIGN KEY (cNumber)
    REFERENCES Customer(cNumber)
  
);

CREATE TABLE if not exists Publisher (
	pubId serial,
  pubName varchar (50) NOT NULL,
	pubEmail varchar (100) NOT NULL,
	bankAcctNo varchar (100) NOT NULL,
  pubAddress varchar (100),
  phoneNo varchar (25),

  PRIMARY KEY (pubId)	 
);

CREATE TABLE if not exists Book (
  bookId serial,
	ISBN varchar (20) UNIQUE NOT NULL,
	author varchar(50) NOT NULL,
	title varchar(50) NOT NULL,
	genre varchar(50) NOT NULL,
	stock int NOT NULL,
	price real NOT NULL,    
	percentRoyalty int NOT NULL,
  noPages int NOT NULL,
  pubId int NOT NULL,
	
	PRIMARY KEY (bookId),
	FOREIGN KEY (pubId)
		REFERENCES Publisher(pubId)
);

CREATE TABLE if not exists basketSelection (
  bookId int NOT NULL,
  cNumber int NOT NULL,
  quantity int NOT NULL,

  PRIMARY KEY (bookId, cNumber),
  FOREIGN KEY (bookId)
    REFERENCES Book(bookId),
  FOREIGN KEY (cNumber)
    REFERENCES Customer(cNumber)
  
);


CREATE TABLE if not exists CustomerOrder (
  orderId serial,
  oDate date NOT NULL,
  oStatus varchar (15) NOT NULL,
  bsId int NOT NULL,
  cNumber int NOT NULL,
  
  PRIMARY KEY (orderId),
  FOREIGN KEY (bsId)
    REFERENCES BillingShippingInfo(bsId),
  FOREIGN KEY (cNumber)
    REFERENCES Customer(cNumber)

);

CREATE TABLE if not exists customerOrderContents (
  bookId int NOT NULL,
  orderId int NOT NULL,
  quantity int NOT NULL,
  
  PRIMARY KEY (bookId, orderId),
  FOREIGN KEY (bookId)
    REFERENCES Book(bookId),
  FOREIGN KEY (orderId)
    REFERENCES CustomerOrder(orderId)
);

CREATE TABLE if not exists SupplyOrder (
  supId serial,
  supDate date NOT NULL,
  quantity int NOT NULL,
  pubId int NOT NULL,
  bookId int NOT NULL,
  
  PRIMARY KEY (supId),
  FOREIGN KEY (pubId)
    REFERENCES Publisher(pubId),
  FOREIGN KEY (bookId)
    REFERENCES Book(bookId)
);

INSERT INTO BillingShippingInfo(
	bsId,addressL1, addressL2, city, provSt, country, pCode, ccardNo, exp, ccn, ccName)
	VALUES (1,'1 Sycamore Dr.', NULL, 'Springfield', 'CA', 'US', '700123', '1234-5678-9012', '0124', '123', 'John Smith');

INSERT INTO BillingShippingInfo(
	bsId,addressL1, addressL2, city, provSt, country, pCode, ccardNo, exp, ccn, ccName)
	VALUES (2,'10 Main St.', NULL, 'Toronto', 'ON', 'Canada', 'M1Z 123', '4567-1111-2222', '0922', '555', 'Jane Doe');

INSERT INTO BillingShippingInfo(
	bsId,addressL1, addressL2, city, provSt, country, pCode, ccardNo, exp, ccn, ccName)
	VALUES (3,'54 Country Rd.', 'Suite 1B', 'Springfield', 'CA', 'US', '700124', '4555-2222-3333', '1224', '111', 'John Smith Enterprises');

INSERT INTO Customer(
	cNumber,uName, pword, email, lname, fname)
	VALUES (1,'jsmith', '961804260.yqTq6SZYMoNbOpY1t2h37U7zhyuFd1vmeAx8g-KPEQc=', 'jsmith@gmail.com', 'Smith', 'John');

INSERT INTO Customer(
	cNumber,uName, pword, email, lname, fname)
	VALUES (2,'jdoe', '0169402691.-1H4VX0WCrSI449OBmcs6ycLOQwbR7hqEQwYQ6GNvkg=', 'jdoe@carleton.ca', 'Doe', 'Jane');

INSERT INTO bsiDirectory(bsId, cNumber, isPrimary) VALUES (1, 1, TRUE);
INSERT INTO bsiDirectory(bsId, cNumber, isPrimary) VALUES (2, 2, TRUE);
INSERT INTO bsiDirectory(bsId, cNumber, isPrimary) VALUES (3, 1, TRUE);

INSERT INTO Publisher(
  pubId,pubName,pubEmail,bankAcctNo,pubAddress,phoneNo) 
  VALUES (1, 'Meow Books','order@meowbooks.com','JPMorgan 001-1234-11111','1 Kitty Kat Rd., Los Angeles, CA, US, 90210','(945) 123-4567');
INSERT INTO Publisher(
  pubId,pubName,pubEmail,bankAcctNo,pubAddress,phoneNo) 
  VALUES (2, 'Nebulous','contact@nebulous.com','BoA 002-4321-22222','54 5th Rd., New York, NY, US, 70000','(768) 321-7654');
INSERT INTO Publisher(
  pubId, pubName,pubEmail,bankAcctNo) 
  VALUES (3, 'Fictional Press','info@fictional.com','BoA 002-5678-33333');
INSERT INTO Publisher(
  pubId, pubName,pubEmail,bankAcctNo) 
  VALUES (4, 'Random Mouse','orders@random.com','Wells Fargo 003-6789-44444');

INSERT INTO Book(
	bookId, ISBN, author, title, genre, stock, price, percentRoyalty, noPages, pubId)
	VALUES (1, '1234-1111-9012', 'Mark Twain', 'Adventures of Huckleberry Finn', 'Fiction', 10, 12.5, 10, 321, 3);
INSERT INTO Book(
	bookId, ISBN, author, title, genre, stock, price, percentRoyalty, noPages, pubId)
	VALUES (2, '1234-1111-9014', 'Mark Twain', 'The Adventures of Tom Sawyer', 'Fiction', 5, 9.5, 10, 231, 3);
INSERT INTO Book(
	bookId, ISBN, author, title, genre, stock, price, percentRoyalty, noPages, pubId)
	VALUES (3, '1333-2222-3061', 'Isac Asimov', 'Foundation', 'Sci-Fi', 15, 21.75, 15, 431, 2);
INSERT INTO Book(
	bookId, ISBN, author, title, genre, stock, price, percentRoyalty, noPages, pubId)
	VALUES (4, '1333-2222-3064', 'Isac Asimov', 'Foundation and Empire', 'Sci-Fi', 2, 22, 15, 441, 2);
INSERT INTO Book(
	bookId, ISBN, author, title, genre, stock, price, percentRoyalty, noPages, pubId)
	VALUES (5, '1333-2222-3066', 'Isac Asimov', 'Second Foundation', 'Sci-Fi', 5, 15.25, 15, 330, 2);
INSERT INTO Book(
	bookId, ISBN, author, title, genre, stock, price, percentRoyalty, noPages, pubId)
	VALUES (6, '5432-3333-2311', 'Mo Willems', 'Don''t Let the Pigeon Drive the Bus', 'Fiction', 20, 5, 20, 15, 1);
INSERT INTO Book(
	bookId, ISBN, author, title, genre, stock, price, percentRoyalty, noPages, pubId)
	VALUES (7, '5432-3333-2313', 'Mo Willems', 'The Pigeon Finds a Hot Dog', 'Fiction', 11, 6, 20, 12, 1);
INSERT INTO Book(
	bookId, ISBN, author, title, genre, stock, price, percentRoyalty, noPages, pubId)
	VALUES (8, '5432-3333-2315', 'Mo Willems', 'Don''t Let Pigeon Stay Up Late', 'Fiction', 15, 6, 20, 10,1);
INSERT INTO Book(
	bookId, ISBN, author, title, genre, stock, price, percentRoyalty, noPages, pubId)
	VALUES (9, '0987-4444-1121', 'J. R. R. Tolkien', 'The Lord of the Rings Box Set', 'Fiction', 12, 66.7, 25, 1905, 3);
INSERT INTO Book(
	bookId, ISBN, author, title, genre, stock, price, percentRoyalty, noPages, pubId)
	VALUES (10, '0001-0002-0003', 'Rick Silva', 'Essential Postgres', 'Technical', 2, 39.05, 5, 90, 4);