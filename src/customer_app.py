import customer_menu as menu
import db
import security
import getpass
import util
from prettytable import PrettyTable
import psycopg2


def printBook(book):
  util.printBookList([book])

def printOrder(order):
  table = PrettyTable(["Order ID","Order Date","Order Status"])
  table.add_row(order[:3])
  print(table)


def printSelectBooks(books, cart, customer):
    util.printBookList(books)
    choice = menu.getUChoiceBookViewMenu()
    if choice == 1 or choice == 2:
      bookId = util.getValidIntInput("Enter book id:")
      selected = None
      for book in books:
        if book[0] == bookId:
          selected = book
          break
      if selected:
        if choice == 2:
          printBook(selected)
        if choice == 1:
          cartItem = None
          cartQuantity = 0
          for item in cart:
            if item[0]==selected[0]:
              cartItem = item
              quantity = cartItem[6]
              break
          stock = selected[6] - cartQuantity
          quantity = util.getValidIntInput("Enter quantity:",1,stock)
          if cartItem == None:
            cartItem = list(selected[:6])
            cartItem.append(quantity)
            cart.append(cartItem)
          else:
            cartItem[6]+=quantity
          print("Book added to cart.")
          printCart(cart, customer)

def printCart(cart, customer):
  if len(cart) == 0:
    print("Cart is empty.")
    return
  print("Cart contents:")
  table = PrettyTable(["Book ID","ISBN","Author","Title","Genre","Price","Quantity"])
  total = 0
  for row in cart:
      table.add_row(row)
      total+=row[5]*row[6]
  print(table)
  print("Total:",total)
  choice = menu.getUChoiceCartMenu()
  if choice == 2:
    cart.clear()
  elif choice == 1:
    if customer == None:
      print("ERROR: You must be logged in before checking out a book.")
    else:
      checkOut(customer, cart)

def checkOut(customer, cart):
  choice = util.getValidIntInput("""Checkout options
  1. Use default billing and shipping info 
  2. Use different billing and shipping info
  3. Add new billing and shipping info
  0. Return to previous menu
  Choice:""",0,3)
  
  try:
    
    bsId = None
    if choice == 0:
      return
    elif choice == 1:
      bsi = db.getBillingShipping(customer[0],True)
      bsId = bsi[0][0]
    elif choice == 2:
      bsilist = db.getBillingShipping(customer[0],False)
      table = PrettyTable([
        "BSID","Address Line 1","Address Line 2",
        "City","Province/State","Country","Postal Code",
        "Card No.","Exp.","CCN","Card Name"
      ])
      for bsi in bsilist:
        table.add_row(bsi[:11])
      print(table)
      bsId = util.getValidIntInput("Select BSID:")
    elif choice == 3:
      bsId = addBillingAndShipping(customer)

    orderId = db.addCustomerOrder(bsId,customer[0],cart)
    cart.clear()
    print("Order id:", orderId)

  except psycopg2.Error as e:
    print(e.pgerror)




def searchBook(cart, customer):
  searchChoice = menu.getUChoiceSearchColl()

  books = []
  if searchChoice == 0:
    return
  elif searchChoice < 6: #text searches allowing for partial matches
    textAttr = ["ISBN","Author","Title","Genre","Publisher"]
    searchVals = ["","","","",""]
    searchVals[searchChoice-1] = "%" + input(textAttr[searchChoice-1]+" (partial) :") + "%"
    books = db.searchBooksByText(searchVals[0],searchVals[1],searchVals[2], searchVals[3], searchVals[4])
  elif searchChoice == 6: #price range
    range = menu.getUChoiceRange("Price")
    books = db.searchBooksByPriceRange(range[0],range[1])
  elif searchChoice == 7: #stock range
    range = menu.getUChoiceRange("Stock")
    books = db.searchBooksByStockRange(range[0],range[1])

  printSelectBooks(books, cart, customer)

def loginOrRegister():
  choice = menu.getUChoiceMakeAcctLogIn()
  if choice == 0:
    return
  uname = input("User name:")
  password = getpass.getpass("Password:")
  customer = None
  if choice == 2:
    customer = db.getCustomer(uname)
    if customer == None:
      print("ERROR:Invalid login!")
    else:
      vfyPassword = customer[2]
      if security.vfyPassword(password, vfyPassword) == False:
        customer = None
        print("ERROR:Invalid login!")
      else:
        print("You are now logged in as:",uname)
  elif choice == 1:
    email = input("Email:")
    lname = input("Last name:")
    fname = input("First name:")
    db.addCustomer(uname, security.genHash(password),email,lname,fname)
    customer = db.getCustomer(uname)
    if customer != None:
      print("Account succesfully created. Please enter billing information.")
      addBillingAndShipping(customer)
  return customer

def addBillingAndShipping(customer:str):
  while True:
    try:
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
      bsid = db.addBillingShipping(customer[0],True,addressl1,addressl2,city,provst,country,pcode,ccardno,ccexp,ccn,ccname)
      print("New billing and shipping info added.")
      return bsid
    except psycopg2.Error as e:
      print(e.pgerror)

def trackOrder(customer):
  if customer==None:
    print("ERROR: You must be logged in to view your orders")
    return
  orderId = util.getValidIntInput("Order id:",0)
  try:
    order = db.getCustomerOrder(orderId,customer[0])
    if order==None:
      print("ERROR: Order not found.")
      return
    printOrder(order)
  except psycopg2.Error as e:
    print(e.pgerror)

def main():
  cart = []
  customer = None
  while True:
    choice = menu.getUChoiceMainMenu()
    if choice == 0:
      exit()
    elif choice == 1:
      books = db.getAllBooks()
      printSelectBooks(books, cart, customer)
    elif choice == 2:
      searchBook(cart, customer)
    elif choice == 3:
      printCart(cart, customer)
    elif choice == 4:
      customer = loginOrRegister()
    elif choice == 5:
      trackOrder(customer)

if __name__ == "__main__":
  main()
