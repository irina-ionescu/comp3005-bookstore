import customer_menu as menu
import db
from prettytable import PrettyTable

def printBook(ISBN:int , title:str, author:str, price:int, currQuantity:int, publisher:str):
  print ( str(ISBN) + "\t" + title + "\t" + author + "\t" + str(price) + "\t" + str(currQuantity) + "\t" + publisher )

def printOrder(oNum:int , shipAddress:str, billAddress:str, name:str, trackingInfo:str, cost:int, datePlaced:str):
  print(str(oNum) + "\t" + shipAddress + "\t" + billAddress + "\t" + name + "\t" + trackingInfo + "\t" + "$" + str(cost) + datePlaced)
  

def printBookList(books):
    table = PrettyTable(["Book ID","ISBN","Author","Title","Genre","Stock","Price","Publisher"])
    for row in books:
      table.add_row(row[:8])
    print(table)


def doBookSearch():
  searchChoice = menu.getUChoiceSearchColl()

  books = []
  if searchChoice == 0:
    return
  elif searchChoice < 6: #text searches allowing for partial matches
    textAttr = ["ISBN","Author","Title","Genre","Publisher"]
    searchVals = []
    for attr in textAttr:
      searchVals.append("")
    searchVals[searchChoice-1] = "%" + input(textAttr[searchChoice-1]+":") + "%"
    books = db.searchBooksByText(searchVals[0],searchVals[1],searchVals[2], searchVals[3], searchVals[4])
  elif searchChoice == 6: #price range
    range = menu.getUChoiceRange("Price")
    books = db.searchBooksByPriceRange(range[0],range[1])
  elif searchChoice == 7: #stock range
    range = menu.getUChoiceRange("Stock")
    books = db.searchBooksByStockRange(range[0],range[1])

  printBookList(books)

#menu.printBook(12345, "Amazing book", "Stephen King", 200, 2, "Random Books")

#print("your choice was: " + str(menu.getUChoiceMainMenu()))

while True:
  choice = menu.getUChoiceMainMenu()
  if choice == 0:
    exit()
  elif choice == 1:
    books = db.getAllBooks()
    printBookList(books)
  elif choice == 2:
    doBookSearch()
