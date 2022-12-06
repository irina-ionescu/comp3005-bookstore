import owner_menu as menu
import db
import util
import psycopg2
from prettytable import PrettyTable

#This is the application that can be run by the store owners.
#It allows adding/removing new books, generating reports, 

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
  return

def salesByParam():
  return

def automatedOrderReport():
  return


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
  