import util as util      

  
def getOChoiceMainMenu()->int :
    choice = util.getValidIntInput("""
    ---------------------------
    What would you like to do?
    1. List all books
    2. Add new book
    3. Remove book
    4. List publishers
    5. Add publisher
    6. Generate reports
    0. Exit 
    Choice: """, 0,6)
    return choice

def getOChoiceReports()->int:
  choice = util.getValidIntInput("""
  ---------------------------
  What would you like to do?
  1. Sales vs. expenditures
  2. Sales by parameter (example: author, genre, ...)
  3. Summary of automated orders sent to publishers
  0. Return to previous menu 
  Choice: """, 0,3)
  return choice
  
