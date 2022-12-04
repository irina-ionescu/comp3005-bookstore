import customer_menu as menu
import db
from prettytable import PrettyTable

cart = []


def printBook(book):
  printBookList([book])

def printOrder(oNum:int , shipAddress:str, billAddress:str, name:str, trackingInfo:str, cost:int, datePlaced:str):
  print(str(oNum) + "\t" + shipAddress + "\t" + billAddress + "\t" + name + "\t" + trackingInfo + "\t" + "$" + str(cost) + datePlaced)
  

def printBookList(books):
    table = PrettyTable(["Book ID","ISBN","Author","Title","Genre","Price","Stock","Publisher"])
    for row in books:
      table.add_row(row[:8])
    print(table)
    choice = menu.getUChoiceBookViewMenu()
    if choice == 1 or choice == 2:
      bookId = menu.getUChoiceInputInt("Enter book id:")
      selected = None
      for book in books:
        if book[0] == bookId:
          selected = book
          break
      if selected:
        if choice == 2:
          printBook(selected)
        if choice == 1:
          stock = selected[6]
          quantity = menu.getUChoiceInputInt("Enter quantity:",1,stock)
          for i in range(quantity):
            cart.append(selected)
          print("Book added to cart.")
          printCart(cart)

def printCart(cart):
  if len(cart) == 0:
    print("Cart is empty.")
    return
  print("Cart contents:")
  table = PrettyTable(["Book ID","ISBN","Author","Title","Genre","Price"])
  total = 0
  for row in cart:
      table.add_row(row[:6])
      total+=row[5]
  print(table)
  print("Total:",total)
  choice = menu.getUChoiceCartMenu()
  if(choice==2):
    cart.clear()

def doBookSearch():
  searchChoice = menu.getUChoiceSearchColl()

  books = []
  if searchChoice == 0:
    return
  elif searchChoice < 6: #text searches allowing for partial matches
    textAttr = ["ISBN","Author","Title","Genre","Publisher"]
    searchVals = ["","","","",""]
    searchVals[searchChoice-1] = "%" + input(textAttr[searchChoice-1]+":") + "%"
    books = db.searchBooksByText(searchVals[0],searchVals[1],searchVals[2], searchVals[3], searchVals[4])
  elif searchChoice == 6: #price range
    range = menu.getUChoiceRange("Price")
    books = db.searchBooksByPriceRange(range[0],range[1])
  elif searchChoice == 7: #stock range
    range = menu.getUChoiceRange("Stock")
    books = db.searchBooksByStockRange(range[0],range[1])

  printBookList(books)


while True:
  choice = menu.getUChoiceMainMenu()
  if choice == 0:
    exit()
  elif choice == 1:
    books = db.getAllBooks()
    printBookList(books)
  elif choice == 2:
    doBookSearch()
  elif choice == 3:
    printCart(cart)
