import util as util      

  
def getOChoiceMainMenu()->int :
    choice = util.getValidIntInput("""What would you like to do?
                              1. List all books
                              2. Add new books
                              3. Remove books
                              4. List publishers
                              5. Add publisher
                              6. Generate reports
                              0. return to previous menu 
                              Choice: """, 0,6)
    return choice

def getOChoiceReports()->int:
  choice = util.getValidIntInput("""What would you like to do?
                              1. Sales vs. expenditures
                              2. Sales by parameter (example: author, genre, ...)
                              3. Get orders placed to publishers
                              0. return to previous menu 
                              Choice: """, 0,3)
  return choice
  
