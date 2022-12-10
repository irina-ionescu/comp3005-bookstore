import psycopg2
import os

BOOK_SELECT="""SELECT b.bookId, b.isbn, b.author, b.title, b.genre, b.price, b.stock, b.nopages, p.pubname
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

def getAllPublishers():
  conn = getConn()
  cur = conn.cursor()
  cur.execute("SELECT * FROM Publisher")
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

#returns sales by parameter from book, publisher and customerordercontents
def getSalesByParam(paramType:str, value):
  conn = getConn()
  cur = conn.cursor()

  if paramType not in ["b.title","b.bookId","b.author", "b.genre","p.pubname"]:
    raise Exception("Invalid param type")
  
  query = """SELECT {0}, sum(quantity*price) 
  FROM customerordercontents as c 
  JOIN book as b on b.bookid = c.bookid
  JOIN publisher as p on b.pubId = p.pubId
  WHERE {0} = %s GROUP BY {0}""".format(paramType)
  cur.execute(query, (value,))
  rows = cur.fetchall()
  cur.close()
  conn.close()
  return rows

def getSalesLastMonthByBook(bookId):
  conn = getConn()
  cur = conn.cursor()
  query = '''SELECT '''
  cur.execute(query, (bookId,))
  rows = cur.fetchall()
  cur.close()
  conn.close()

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

def getCustomer(uname):
  conn = getConn()
  cur = conn.cursor()
  query = "SELECT * FROM Customer WHERE uname=%s"
  cur.execute(query,(uname,))
  customer = cur.fetchone()
  conn.commit()
  cur.close()
  conn.close()
  return customer

def addCustomer(uname, pword, email, lname, fname):
  conn = getConn()
  cur = conn.cursor()
  query = "INSERT INTO Customer (cnumber, uname, pword, email, lname, fname) "
  query += "VALUES (DEFAULT, %s, %s, %s, %s, %s)"
  cur.execute(query, (uname, pword, email, lname, fname))
  conn.commit()
  cur.close()
  conn.close()

def getBillingShipping(cNumber,isPrimary = None):
  conn = getConn()
  cur = conn.cursor()
  query = """
  SELECT * FROM BillingShippingInfo as bsi 
  JOIN BSIDirectory as bsiDir on bsi.bsid=bsidir.bsid
  WHERE cNumber = %s
  """
  if isPrimary == True :
    query+=" AND isPrimary = True"
  cur.execute(query, (cNumber,))
  bsi = cur.fetchall()
  conn.commit()
  cur.close()
  conn.close()
  return bsi

def addBillingShipping(cNumber, isPrimary, addressl1, addressl2, city, provst, country, pcode, ccardno, exp, ccn, ccname):
  conn = getConn()
  cur = conn.cursor()
  query = "INSERT INTO BillingShippingInfo (bsid, addressl1, addressl2, city, provst, country, pcode, ccardno, exp, ccn, ccname) "
  query += "VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) returning bsid"
  cur.execute(query, (addressl1, addressl2, city, provst, country, pcode, ccardno, exp, ccn, ccname))
  
  bsid = None

  res = cur.fetchone()
  if res != None:
    bsid = res[0]

  query = "INSERT INTO BSIDirectory (bsid, cnumber, isprimary) VALUES (%s, %s, %s)"
  cur.execute(query, (bsid, cNumber, isPrimary))
  
  conn.commit()
  cur.close()
  conn.close()
  return bsid

#gets publisher id by name, returns publisher id (id, None)
def addPublisher(pubname:str, pubemail:str, bankacctNo:str, pubaddress:str, phoneno:str):
  conn = getConn()
  cur = conn.cursor()
  query = "INSERT INTO Publisher (pubid, pubname, pubemail, bankacctno, pubaddress, phoneno) "
  query += "VALUES (DEFAULT, %s, %s, %s, %s, %s) returning pubid"
  cur.execute(query, (pubname, pubemail, bankacctNo, pubaddress, phoneno) )
  pubId = None
  res = cur.fetchone()
  if res != None:
    pubId = res[0]
  conn.commit()
  cur.close()
  conn.close()
  return pubId

#gets publisher id by name, returns publisher id  (id, None)
def getPublisherId(name)->int:
  conn = getConn()
  cur = conn.cursor()
  query = "SELECT pubid FROM Publisher WHERE pubname LIKE %s"
  cur.execute(query, (name,))
  res = cur.fetchone()
  pubId = None
  if res != None:
    pubId = res[0]
  conn.commit()
  cur.close()
  conn.close()
  return pubId


def addCustomerOrder(bsid,cnumber,cart):
  conn = getConn()
  cur = conn.cursor()

  query = """
  INSERT INTO customerorder 
  (orderid, odate, ostatus, bsid, cnumber)
	VALUES ( DEFAULT, CURRENT_DATE, 'SUBMITTED', %s, %s) returning orderid
  """
  cur.execute(query, (bsid, cnumber))
  orderid = None

  res = cur.fetchone()
  if res != None:
    orderid = res[0]
  
  query = """
  INSERT INTO customerordercontents (
	bookid, orderid, quantity)
	VALUES (%s, %s, %s);
  """
  for book in cart:
    cur.execute(query,(book[0],orderid,book[6]))

  #update stock
  query = "UPDATE Book SET stock = %s WHERE bookId = %s"
  cur.execute(query,(book[6],book[0]))

  conn.commit()
  cur.close()
  conn.close()
  return orderid

def getCustomerOrder(orderId,cNumber):
  conn = getConn()
  cur = conn.cursor()
  query = """
  SELECT orderId, oDate, oStatus, fName, lName FROM CustomerOrder as co
  JOIN Customer as cu ON co.cNumber=cu.cNumber
  WHERE orderId=%s AND co.cNumber=%s
  """
  cur.execute(query, (orderId,cNumber))
  order = cur.fetchone()
  conn.commit()
  cur.close()
  conn.close()
  return order

