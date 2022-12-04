import customer_menu as menu
import db
from prettytable import PrettyTable

def printBooks(books):
    table = PrettyTable(["Book ID","ISBN","Author","Title","Genre"])
    for row in books:
      table.add_row(row[:5])
    print(table)
    
#menu.printBook(12345, "Amazing book", "Stephen King", 200, 2, "Random Books")

#print("your choice was: " + str(menu.getUChoiceMainMenu()))

while True:
  choice = menu.getUChoiceMainMenu()
  if choice == 0:
    exit()
  elif choice == 1:
    books = db.getAllBooks()
    printBooks(books)
  elif choice == 2:
    search_choices = menu.getUChoiceSearchColl()
    search_attributes = ["ISBN","Author","Title","Genre"]
    search_vals = ["","","",""] 
    for sc in search_choices:
      search_vals[sc-1] = "%" + input(search_attributes[sc-1]+":") + "%"
    books = db.searchBooks(search_vals[0],search_vals[1],search_vals[2], search_vals[3])
    printBooks(books)
