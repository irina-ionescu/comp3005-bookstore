#This module provides user interface to console

import util as util


def getUChoiceCartMenu()->int:
  choice = util.getValidIntInput("""Choose an option:
  1. Checkout
  2. Clear cart
  0. Return to previous menu
  Choice:""",0,2)
  return choice

def getUChoiceBookViewMenu()->int :
  choice = util.getValidIntInput("""Choose an option:
  1. Add book to cart by id
  2. View book by id
  0. Return to previous menu
  Choice: """,0,2)
  return choice

def getUChoiceMainMenu()->int :
  choice = util.getValidIntInput("""
  ---------------------------
  Main Menu. Choose an option:
  1. See all available books
  2. Search collection by title, author, etc.
  3. View cart
  4. Make an account/log in
  5. Track an order
  0. Exit
  Choice: """,0,5)
  return choice
   

def getUChoiceSearchColl()->int :
  choice = util.getValidIntInput("""Choose search parameters, one number or multiple separated by space:
  1. By ISBN
  2. By author
  3. By title
  4. By genre
  5. By publisher
  6. By price
  7. Books in stock
  0. Return to previous menu
  Choice: """,0,7)
  return choice

def getUChoiceMakeAcctLogIn()->int :
  choice = util.getValidIntInput("""What would you like to do?
  1. Make a new account
  2. Log in with existing account
  0. Return to previous menu 
  Choice: """,0,2)
  return choice

def getUChoiceRange(attrName)->list:
  while True:
    try:
      choice = [int(c) for c in input(attrName+" range min,max: ").split(",")]
      isValid = True
      if len(choice) != 2:
        print("Invalid range length")
        isValid = False
      for c in choice:                  
        if int(c) < 0:
          print ("%s is an invalid value", str(c))
          isValid = False
      if isValid:
        return choice
    except:
      print("Not a valid integer")


  



