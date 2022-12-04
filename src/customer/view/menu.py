#This module provides user and store interface to console


def printBook(ISBN:int , title:str, author:str, price:int, currQuantity:int, publisher:str):
  print ( str(ISBN) + "\t" + title + "\t" + author + "\t" + str(price) + "\t" + str(currQuantity) + "\t" + publisher )

def printOrder(oNum:int , shipAddress:str, billAddress:str, name:str, trackingInfo:str, cost:int, datePlaced:str):
  print(str(oNum) + "\t" + shipAddress + "\t" + billAddress + "\t" + name + "\t" + trackingInfo + "\t" + "$" + str(cost) + datePlaced)
  

 
def getChoiceUserOrStore()->int:
  try:
    choice = input("""Hello! Who are you?
                1. I'm an user
                2. I'm a store employee
                0. Exit
            Choice: """)
    if int(choice) >= 0 and int(choice) <=2:
      return int(choice)
    else:
      print ("Invalid choice")
  except:
    print("Not a valid integer")


def getUChoiceMainMenu()->int :
  try:
    choice = input("""Hello! Choose an option:
                1. See all available books
                2. Search collection by title, author, etc.
                3. Make an account/log in
                4. Track an order
                0. Exit
            Choice: """)
    if int(choice) >= 0 and int(choice) <=4:
      return int(choice)
    else:
      print ("Invalid choice")
  except:
    print("Not a valid integer")

def getUChoiceSearchColl()->int :
  try:
    choice = input("""Choose search parameter:
                              1. by title
                              2. by author
                              3. by ISBN
                              4. by genre
                              5. by price
                              6. by publisher
                              7. books in stock
                              0. return to previous menu 
                      Choice: """)
    if int(choice) >= 0 and int(choice) <=7:
      return int(choice)
    else:
      print ("Invalid choice")                  
  except:
    print("Not a valid integer")

def getUChoiceMakeAcctLogIn()->int :
  try:
    choice = input("""What would you like to do?
                              1. Make a new account
                              2. Log in with existing account
                              0. return to previous menu 
                      Choice: """)
    if int(choice) >= 0 and int(choice) <=2:
      return int(choice)
    else:
      print ("Invalid choice")                  
  except:
    print("Not a valid integer")


def getSChoiceMainMenu()->int :
  try:
    choice = input("""What would you like to do?
                              1. List orders
                              2. List publishers 
                              3. Add new books
                              4. Remove books
                              5. Generate reports
                              6. Search books
                              7. Pay publisher
                              0. return to previous menu 
                      Choice: """)
    if int(choice) >= 0 and int(choice) <=7:
      return int(choice)
    else:
      print ("Invalid choice")                  
  except:
    print("Not a valid integer")
  
def getSChoiceReports()->int :
  try:
    choice = input("""What would you like to do?
                              1. 
                              2. List publishers 
                              3. Add new books
                              4. Remove books
                              5. Generate reports
                              6. Search books
                              7. Pay publisher
                              0. return to previous menu 
                      Choice: """)
    if int(choice) >= 0 and int(choice) <=7:
      return int(choice)
    else:
      print ("Invalid choice")                  
  except:
    print("Not a valid integer")
  
  


