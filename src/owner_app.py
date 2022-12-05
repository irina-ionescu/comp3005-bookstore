import owner_menu as menu
import db
import util
from prettytable import PrettyTable

def listAllBooks(books):
  util.printBookList(books)


while True:
  choice = menu.getOChoiceMainMenu()
  if choice == 0:
    exit()
  elif choice == 1:
    books = db.getAllBooks()
    listAllBooks(books)