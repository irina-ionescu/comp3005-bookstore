#This module provides user and store interface to console




def getBookViewMenu()->int :
  try:
    choice = input("""Choose an option:
                1. View book by id
                2. Add book to cart by id
                0. Return to previous menu
            Choice: """)
    if int(choice) >= 0 and int(choice) <=4:
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


def getUChoiceSearchColl()->int :
  try:
    choice = input("""Choose search parameters, one number or multiple separated by space:
                              1. by ISBN
                              2. by author
                              3. by title
                              4. by genre
                              5. by publisher
                              6. by price
                              7. books in stock
                              0. return to previous menu
                      Choice: """)
           
    if int(choice) < 0 or int(choice) > 7:
      print ("%s is an invalid choice", choice)
    return int(choice)
  except:
    print("Not a valid integer")
    return 0

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
  


