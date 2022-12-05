import customer_menu as menu
import db
import security
import getpass
from prettytable import PrettyTable

cart = []
customer = None

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

def doLoginOrRegister():
  choice = menu.getUChoiceMakeAcctLogIn()
  uname = input("User name:")
  password = getpass.getpass("Password:")
  if choice == 2:
    customer = db.getCustomer(uname)
    if customer == None:
      print("Invalid login.")
    else:
      vfyPassword = customer[2]
      if security.vfyPassword(password, vfyPassword) == False:
        customer = None
        print("Invalid login!")
      else:
        print("You are now logged in as", uname)
  elif choice == 1:
    email = input("Email:")
    lname = input("Last name:")
    fname = input("First name:")
    db.addCustomer(uname, security.genHash(password),email,lname,fname)
    customer = db.getCustomer(uname)
    if customer != None:
      print("Account succesfully created. Please enter billing information.")
      addressl1 = input("Address line 1:")
      addressl2 = input("Address line 2:")
      city = input("City:")
      provst = input("Province/State:")
      country = input("Country:")
      pcode = input("Postal code:")
      ccardno = input("Credit card number:")
      ccexp = input("Credit card expiration (MMYY):")
      ccn = input("CCN:")
      ccname = input("Name on the credit card:")
      db.addBillingShipping(customer[0],True,addressl1,addressl2,city,provst,country,pcode,ccardno,ccexp,ccn,ccname)


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
  elif choice == 4:
    doLoginOrRegister()



