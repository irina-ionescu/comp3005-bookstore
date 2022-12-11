-- This file is for grading purposes only
SELECT b.bookId, b.isbn, b.author, b.title, b.genre, b.price, b.stock, b.nopages, p.pubname
    FROM book as b JOIN publisher as p ON b.pubId=p.pubId


SELECT * FROM Publisher

SELECT b.bookId, b.isbn, b.author, b.title, b.genre, b.price, b.stock, b.nopages, p.pubname
    FROM book as b JOIN publisher as p ON b.pubId=p.pubId
    WHERE b.isbn LIKE <isbnVal> OR b.author LIKE <authorVal> OR b.title LIKE <titleVal> OR <genre> LIKE <genreval> OR p.pubname LIKE <pubnameVal>

SELECT b.bookId, b.isbn, b.author, b.title, b.genre, b.price, b.stock, b.nopages, p.pubname
    FROM book as b JOIN publisher as p ON b.pubId=p.pubId 
    WHERE b.price >= <minVal> AND b.price <= <maxVal>


SELECT b.bookId, b.isbn, b.author, b.title, b.genre, b.price, b.stock, b.nopages, p.pubname
    FROM book as b JOIN publisher as p ON b.pubId=p.pubId
    WHERE b.stock >= <minVal> AND b.stock <= <maxVal>


--paramType can be "b.title","b.bookId","b.author", "b.genre","p.pubname"
--<val> is given by user
SELECT <paramType>, sum(quantity*price) 
  FROM customerordercontents as c 
  JOIN book as b on b.bookid = c.bookid
  JOIN publisher as p on b.pubId = p.pubId
  WHERE <paramType> = <val> GROUP BY <paramType>


SELECT * FROM Customer WHERE uname=<usernameVal>


SELECT * FROM BillingShippingInfo as bsi 
  JOIN BSIDirectory as bsiDir on bsi.bsid=bsidir.bsid
  WHERE cNumber = <customerNumberVal>


SELECT * FROM BillingShippingInfo as bsi 
  JOIN BSIDirectory as bsiDir on bsi.bsid=bsidir.bsid
  WHERE cNumber = <customerNumberVal> AND isPrimary = True


SELECT pubid FROM Publisher WHERE pubname LIKE <pubnameVal>

SELECT orderId, oDate, oStatus, fName, lName FROM CustomerOrder as co
  JOIN Customer as cu ON co.cNumber=cu.cNumber
  WHERE orderId=<orderIdVal> AND co.cNumber=<customerNumberVal>