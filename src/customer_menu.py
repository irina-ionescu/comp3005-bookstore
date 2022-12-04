#This module provides user and store interface to console


def printBook(ISBN:int , title:str, author:str, price:int, currQuantity:int, publisher:str):
  print ( str(ISBN) + "\t" + title + "\t" + author + "\t" + str(price) + "\t" + str(currQuantity) + "\t" + publisher )

def printOrder(oNum:int , shipAddress:str, billAddress:str, name:str, trackingInfo:str, cost:int, datePlaced:str):
  print(str(oNum) + "\t" + shipAddress + "\t" + billAddress + "\t" + name + "\t" + trackingInfo + "\t" + "$" + str(cost) + datePlaced)
  


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

def getUChoiceSearchColl()->list :
  try:
    choice = [int(c) for c in input("""Choose search parameters, one number or multiple separated by space :
                              1. by ISBN
                              2. by author
                              3. by title
                              4. by genre
                              5. by price
                              6. by publisher
                              7. books in stock
                              0. return to previous menu
                              Example: 2 3 means search by title or author 
                      Choice: """).split()]
    for c in choice:                  
      if int(c) < 0 or int(c) >7:
        print ("%s is an invalid choice", str(c))
    return choice
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

#choices = getUChoiceSearchColl() 
#print(choices) 
  


