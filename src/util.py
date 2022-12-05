from prettytable import PrettyTable

def getValidIntInput(message, min=0, max=9999)->int :
  while True:
    try:
      val = int(input(message))
      if int(val) >= min and int(val) <=max:
        return val
      else:
        print ("Invalid choice")
    except:
      print("Not a valid integer")

def printBookList(books):
  table = PrettyTable(["Book ID","ISBN","Author","Title","Genre","Price","Stock","No. Pages","Publisher"])
  for row in books:
    table.add_row(row)
  print(table)