-- This file is for grading purposes only
-- Returns all books including publisher name by doing a JOIN with Publisher
SELECT b.bookId, b.isbn, b.author, b.title, b.genre, b.price, b.stock, b.nopages, p.pubname
    FROM book as b JOIN publisher as p ON b.pubId=p.pubId

-- Returns all publisher records
SELECT * FROM Publisher

-- Returns search results for text based book attributes
-- Uses a partial match 
-- There is a JOIN with publisher to allow retrieving all books for a particular publisher name
SELECT b.bookId, b.isbn, b.author, b.title, b.genre, b.price, b.stock, b.nopages, p.pubname
    FROM book as b JOIN publisher as p ON b.pubId=p.pubId
    WHERE b.isbn LIKE <isbnVal> OR b.author LIKE <authorVal> OR b.title LIKE <titleVal> OR <genre> LIKE <genreval> OR p.pubname LIKE <pubnameVal>

-- Returns all books within a price range
SELECT b.bookId, b.isbn, b.author, b.title, b.genre, b.price, b.stock, b.nopages, p.pubname
    FROM book as b JOIN publisher as p ON b.pubId=p.pubId 
    WHERE b.price >= <minVal> AND b.price <= <maxVal>

-- Returns all books within a stock range
SELECT b.bookId, b.isbn, b.author, b.title, b.genre, b.price, b.stock, b.nopages, p.pubname
    FROM book as b JOIN publisher as p ON b.pubId=p.pubId
    WHERE b.stock >= <minVal> AND b.stock <= <maxVal>

-- Returns sales reports by <paramType>
--paramType can be "b.title","b.bookId","b.author", "b.genre","p.pubname"
--<val> is given by user
SELECT <paramType>, sum(quantity*price) 
  FROM customerordercontents as c 
  JOIN book as b on b.bookid = c.bookid
  JOIN publisher as p on b.pubId = p.pubId
  WHERE <paramType> = <val> GROUP BY <paramType>

-- Returns customer entry by user name
SELECT * FROM Customer WHERE uname=<usernameVal>

-- Returns all billing and shipping info entries associated with a customer number
SELECT * FROM BillingShippingInfo as bsi 
  JOIN BSIDirectory as bsiDir on bsi.bsid=bsidir.bsid
  WHERE cNumber = <customerNumberVal>

-- Returns the primary billing and shipping info for a customer
SELECT * FROM BillingShippingInfo as bsi 
  JOIN BSIDirectory as bsiDir on bsi.bsid=bsidir.bsid
  WHERE cNumber = <customerNumberVal> AND isPrimary = True

-- Returns publisher id matching a publisher name
SELECT pubid FROM Publisher WHERE pubname LIKE <pubnameVal>

-- Returns a CustomerOrder entry associated with a given order id a customer number
-- Used in tracking order status
SELECT orderId, oDate, oStatus, fName, lName FROM CustomerOrder as co
  JOIN Customer as cu ON co.cNumber=cu.cNumber
  WHERE orderId=<orderIdVal> AND co.cNumber=<customerNumberVal>


-- Deletes book by id
DELETE FROM Book WHERE bookId=<value>

-- Adds a customer order entry during checkout
INSERT INTO customerorder 
  (orderid, odate, ostatus, bsid, cnumber)
	VALUES ( DEFAULT, CURRENT_DATE, 'SUBMITTED', <bsidvalue>, <cnumbervalue> ) returning orderid

-- Associates books with a customer order entry during checkout
INSERT INTO customerordercontents (bookid, orderid, quantity) VALUES (book.bookId, orderid, book.price)

-- Updates book stock during checkout
-- Will trigger a supply order when stock is less than 10
UPDATE Book SET stock = stock - <quantityvalue> WHERE bookId = <idvalue>
