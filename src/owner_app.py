import owner_menu as menu
import db
import util
import psycopg2
from prettytable import PrettyTable

#This is the application that can be run by the store owners.
#It allows adding/removing new books, generating reports

def listAllBooks(books):
  util.printBookList(books)

def addNewBook():
  pubId = None
  while True:
    pubName = input("Enter Publisher name (partial name allowed):") + "%"
    pubId = db.getPublisherId(pubName)
    if pubId != None:
      break
  book = getBookToAddValidInput()

  book.append(pubId)
  db.addBook(book[0], book[1], book[2], book[3], book[4], book[5], book[6], book[7], book[8])
    
#helper function to get input for adding book    
def getBookToAddValidInput()->list:
  book = []
  try:
    #TODO validate unique not null isbn, rest not null, quantity >0, percentRoyalty >0 and <100, noPages >0
    isbn = input("ISBN: ")
    author = input("Author: ")
    title = input("Title: ")
    genre = input("Genre: ")
    quant = int(input("Quantity: "))
    price = float(input("Price: "))
    percentRoyalty = int(input("Royalty to publisher (%% of price): "))
    noPages = int(input("Number of pages: "))
    book.extend((isbn, author, title, genre, quant, price, percentRoyalty, noPages))
    return book
  except:
    print("Not a valid input")
    
    
def addNewPublisher():
  #TODO catch pubname not unique exception from db
  while True:
    try:
      publisher = []
      publisher = getPublisherToAddValidInput()
      pubId = db.addPublisher(publisher[0], publisher[1], publisher[2], publisher[3], publisher[4])
      print("Success! Publisher with id {} was inserted in the database.".format(pubId))
      return
    except psycopg2.Error as e:
      print(e.pgerror)

def getPublisherToAddValidInput()->list:
  publisher = []
  try:
    pubName = input("Publisher name (must be unique): ")
    pubEmail = input("Email: ")
    bankAcctNo = input("Bank account information: ")
    pubAddress = input("Address: ")
    phoneNo = input("Phone number: ")
    if pubName != "" and pubEmail != "" and bankAcctNo != "" :
      publisher.extend((pubName, pubEmail, bankAcctNo, pubAddress, phoneNo))
    return publisher
  except:
    print("Not a valid input")

def deleteBook():
  while True:
    try:
      id = int(input("Enter id of book to be deleted: "))
      db.deleteBookById(id)
      print ("Success! Deleted book with id {}".format(id))
      return
    except psycopg2.Error as e:
      print ("Invalid input")
      print(e.pgerror)

def listAllPublishers():
  try:
    table = PrettyTable(["PubId", "Name", "Email", "Bank Account No", "Address", "Phone No"])
    publishers = db.getAllPublishers()
    for row in publishers:
      table.add_row(row)
    print(table)
  except psycopg2.Error as e:
      print ("Invalid input")

def salesVsExpenses():
  try:
    totalSales = 0.0
    totalExpenses = 0.0
    table = PrettyTable(["Book Price", "Quantity Sold", "Royalty %", "Total Sales", "Total Expense"])
    rows = db.getSalesVsExpenses()
    for row in rows:
      table.add_row(row)
      totalSales += row[3]
      totalExpenses += row[4]
    print(table)
    print("Total book sales:", totalSales)
    print("Total to be paid in royalties:", totalExpenses)
  except psycopg2.Error as e:
    print(e.pgerror)  
  return

def salesByParam():
  choice = util.getValidIntInput("""Get sales by:
  1. Book title
  2. Book id
  3. Author
  4. Genre 
  5. Publisher
  Choice: """, 1, 5)
  if choice == 1:
    try:
      paramType = "b.title"
      value = input("Enter book title: ")
      rows = db.getSalesByParam(paramType, value)
      table = PrettyTable(["Title", "Total Sales" ])
      for row in rows:
        table.add_row(row)
      print(table)
      return
    except psycopg2.Error as e:
      print(e.pgerror)
  
  if choice == 2:
    try:
      paramType = "b.bookId"
      value = input("Enter book id: ")
      rows = db.getSalesByParam(paramType, value)
      table = PrettyTable(["Book Id", "Total Sales" ])
      for row in rows:
        table.add_row(row)
      print(table)
      return 
    except psycopg2.Error as e:
      print(e.pgerror)
  
  if choice == 3:
    try:
      paramType = "b.author"
      value = input("Enter author: ")
      rows = db.getSalesByParam(paramType, value)
      table = PrettyTable(["Author", "Total Sales" ])
      for row in rows:
        table.add_row(row)
      print(table)
      return 
    except psycopg2.Error as e:
      print(e.pgerror)
    
  if choice == 4:
    try:
      paramType = "b.genre"
      value = input("Enter genre: ")
      rows = db.getSalesByParam(paramType, value)
      table = PrettyTable(["Genre", "Total Sales" ])
      for row in rows:
        table.add_row(row)
      print(table)
      return 
    except psycopg2.Error as e:
      print(e.pgerror)
  
  if choice == 5:
    try:
      paramType = "p.pubname"
      value = input("Enter publisher name: ")
      rows = db.getSalesByParam(paramType, value)
      table = PrettyTable(["Publisher", "Total Sales" ])
      for row in rows:
        table.add_row(row)
      print(table)
      return 
    except psycopg2.Error as e:
      print(e.pgerror)

def automatedOrderReport():
  try:
    rows = db.getOrdersToPublishers()
    table = PrettyTable(["Supplier Id", "Order Date", "Quantity Ordered", "Publisher Name", "Title", "Author" ])
    for row in rows:
      table.add_row(row)
      print(table)
    return
  except psycopg2.Error as e:
      print(e.pgerror)

def main():
  while True:
    choice = menu.getOChoiceMainMenu()
    if choice == 0:
      exit()
    elif choice == 1:
      books = db.getAllBooks()
      listAllBooks(books)
    elif choice == 2:
      addNewBook()
    elif choice == 3:
      deleteBook()
    elif choice == 4:
      listAllPublishers()
    elif choice == 5:
      addNewPublisher()
    elif choice == 6:
      repChoice = menu.getOChoiceReports()
      if repChoice == 0:
        continue
      elif repChoice == 1:
        salesVsExpenses()
      elif repChoice == 2:
        salesByParam()
      elif repChoice == 3:
        automatedOrderReport()
    

if __name__ == "__main__":
  main()
  