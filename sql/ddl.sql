--This file is for grading purposes only
-- Stores billing and shipping information
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
-- Stores customer entries
CREATE TABLE if not exists Customer (
    cNumber serial,
  	uname varchar(50) UNIQUE NOT NULL,
  	pword varchar(100) NOT NULL,
  	email varchar(100) UNIQUE NOT NULL,
  	lname varchar(100) NOT NULL,
	  fname varchar(100) NOT NULL,
  
  PRIMARY KEY (cNumber)
);

-- Stores the relation from customer records to billing and shipping information entries
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

-- Stores publisher information
CREATE TABLE if not exists Publisher (
	pubId serial,
  pubName varchar (50) NOT NULL UNIQUE,
	pubEmail varchar (100) NOT NULL,
	bankAcctNo varchar (100) NOT NULL,
  pubAddress varchar (100),
  phoneNo varchar (25),

  PRIMARY KEY (pubId)	 
);

-- Stores book information
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

-- Stores customer orders
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

-- Stores the relation between customer orders and books
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

-- Stores supply order entries
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