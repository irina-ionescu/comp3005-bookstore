import psycopg2
import os

BOOK_SELECT="""SELECT b.bookId, b.isbn, b.author, b.title, b.genre, b.price, b.stock, p.pubname
    FROM book as b JOIN publisher as p ON b.pubId=p.pubId """

def getConn():
  try:
    conn = psycopg2.connect(database="Bookstore", 
      user = os.environ['PGUSER'], 
      password = os.environ['PGPASS'], 
      host = "127.0.0.1", 
      port = os.environ['PGPORT'])
  except:
    print("Failed to connect to database")
    exit(1)
  return conn

def getAllBooks():
  conn = getConn()
  cur = conn.cursor()
  cur.execute(BOOK_SELECT)
  rows = cur.fetchall()
  cur.close()
  conn.close()
  return rows

def searchBooksByText(ISBN=None,author=None,title=None,genre=None,publisher=None):
  conn = getConn()
  cur = conn.cursor()
  query = BOOK_SELECT + "WHERE b.isbn LIKE %s OR b.author LIKE %s OR b.title LIKE %s OR b.genre LIKE %s OR p.pubname LIKE %s"
  cur.execute(query, (ISBN, author, title, genre, publisher))
  rows = cur.fetchall()
  cur.close()
  conn.close()
  return rows

def searchBooksByPriceRange(minPrice,maxPrice):
  conn = getConn()
  cur = conn.cursor()
  query = BOOK_SELECT + "WHERE b.price >= %s AND b.price <= %s"
  cur.execute(query, (minPrice, maxPrice))
  rows = cur.fetchall()
  cur.close()
  conn.close()
  return rows

def searchBooksByStockRange(minStock,maxStock):
  conn = getConn()
  cur = conn.cursor()
  query = BOOK_SELECT + "WHERE b.stock >= %s AND b.stock <= %s"
  cur.execute(query, (minStock, maxStock))
  rows = cur.fetchall()
  cur.close()
  conn.close()
  return rows

def deleteBookById(bookId):
  conn = getConn()
  cur = conn.cursor()
  query = "DELETE FROM Book WHERE bookId=%s"
  cur.execute(query, (bookId,))
  conn.commit()
  cur.close()
  conn.close()


def addBook(ISBN, author, title, genre, stock, price, percentRoyalty, noPages, pubId):
  conn = getConn()
  cur = conn.cursor()
  query = "INSERT INTO Book(bookId, ISBN, author, title, genre, stock, price, percentRoyalty, noPages, pubId) "
  query += "VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
  cur.execute(query, (ISBN, author, title, genre, stock, price, percentRoyalty, noPages, pubId))
  conn.commit()
  cur.close()
  conn.close()

def addCustomer(uname, pword, email, lname, fname):
  conn = getConn()
  cur = conn.cursor()
  query = "INSERT INTO Customer (cnumber, uname, pword, email, lname, fname) "
  query += "VALUES (DEFAULT, %s, %s, %s, %s, %s)"
  cur.execute(query, (uname, pword, email, lname, fname))
  conn.commit()
  cur.close()
  conn.close()

def addBillingShipping(cNumber, isPrimary, addressl1, addressl2, city, provst, country, pcode, ccardno, exp, ccn, ccname):
  conn = getConn()
  cur = conn.cursor()
  query = "INSERT INTO BillingShippingInfo (bsid, addressl1, addressl2, city, provst, country, pcode, ccardno, exp, ccn, ccname) "
  query += "VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) returning bsid"
  cur.execute(query, (addressl1, addressl2, city, provst, country, pcode, ccardno, exp, ccn, ccname))
  bsid = cur.fetchone()[0]

  query = "INSERT INTO BSIDirectory (bsid, cnumber, isprimary) VALUES (%s, %s, %s)"
  cur.execute(query, (bsid, cNumber, isPrimary))
  
  conn.commit()
  cur.close()
  conn.close()

#deleteBookById(15)
#addBook("1234-5678-9103", "Irina Ionescu", "Adventures in Postgres", "Drama", 1, 10000.01, 100, 1, 4 )
#addCustomer("dippy", "402375329.N3ZnpkqkIQ1EI5aZ3h7WB66b7d1-VKgFd_3-XCmsWsw=", "dippy@kittyworld.com", "Dot", "Dippin")
#addBillingShipping(1, True, "123 Any Street", None, "Whoville", "FL", "North Pole", "111111", "123456789", "0101", "123", "Mr. Grinch")