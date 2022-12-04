import psycopg2
import os

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
  cur.execute("SELECT * FROM Book")
  rows = cur.fetchall()
  conn.close()
  return rows

def searchBooks(ISBN=None,author=None,title=None,genre=None):
  conn = getConn()
  cur = conn.cursor()
  query = "SELECT * FROM Book WHERE ISBN LIKE %s OR author LIKE %s OR title LIKE %s OR genre LIKE %s"
  cur.execute(query, (ISBN, author, title, genre))
  rows = cur.fetchall()
  conn.close()
  return rows


